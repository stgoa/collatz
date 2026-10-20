"""Read-only certificate replay and bounded checks for the inverse scope theorem."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import inverse_scope as I

HERE=Path(__file__).resolve().parent
CERTIFICATES=HERE/'anchor_certificates.json'
RECEIPT=HERE/'inverse_scope_audit.json'


def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit():
    fixtures=json.loads(CERTIFICATES.read_text())
    assert [item['anchor'] for item in fixtures]==[39,135]
    proofs={item['anchor']:I.verify_certificate(item) for item in fixtures}
    anchors=[]
    for item in fixtures:
        b=item['anchor']; row=proofs[b]
        anchors.append(dict(anchor=b,critical_index=b//3,
                            smaller_origins=len(row['smaller']),
                            quotient_states=len(row['bases']),
                            maximum=max(row['bases']),
                            lower_current_rows=len(row['lower_current']),
                            pair_current_rows=len(row['pair_current']),
                            first_entry=row['forward']['path'],
                            discovery_caps=item['discovery_caps']))

    # Every inverse branch is exercised at short depth, with ray indices0/1.
    # The theorem's arbitrary ray quantifier comes from its affine proof.
    words=[]
    for b in proofs:
        q=I.lifted_witness(b,4)['q']
        frontier=[(b,[])]
        for depth in range(1,4):
            following=[]
            for shadow,word in frontier:
                for kind in I.C.BASES[shadow%3]:
                    for index in ((0,) if kind=='point' else (0,1)):
                        newword=word+[(kind,index)]
                        checked=I.shadow_lift(b,proofs[b]['edges'],q,newword)
                        following.append((checked['states'][-1]['shadow'],newword))
                        words.append([b,depth,[[kind,index] for kind,index in newword],digest(checked)])
            frontier=following

    # The exact word checker accepts arbitrary supplied ray indices and
    # depth. These samples test both long words and long individual rays.
    long_words=[]
    for b in proofs:
        for D in (4,8,32,128):
            for index in (0,8,128,1024):
                q=I.lifted_witness(b,D)['q']
                shadow,word=b,[]
                for depth in range(1,D+1):
                    kind='point' if depth>1 and shadow%3==2 else 'ray0'
                    ray_index=index if depth==1 else 0
                    shadow,_,_=I.C.inverse_step(shadow,kind,ray_index)
                    word.append((kind,ray_index))
                checked=I.shadow_lift(b,proofs[b]['edges'],q,word)
                long_words.append([b,D,index,digest(checked)])

    # Independent, complete origin enumeration at four finite targets:
    # no inverse branch truncation is involved in these checks.
    origins=[]
    for b,D in ((39,2),(39,3),(135,4),(135,5)):
        q=I.lifted_witness(b,D)['q']
        canonical_count=ordinary_count=0
        for p in range(1,q+1,2):
            y=p
            for depth in range(1,D+1):
                y=I.NORMAL.step(y)
                assert y!=q
            ordinary_count+=1
            if I.NORMAL.canonical(p):
                canonical_count+=1
                y=p
                for depth in range(1,D+1):
                    y=I.NORMAL.quotient_step(y)
                    assert y!=q
        origins.append(dict(anchor=b,D=D,q=q,canonical_origins=canonical_count,
                            ordinary_origins=ordinary_count))

    cylinders=[]
    for base,period in ((13,256),(45,128)):
        for index in range(64):
            w=base+period*index
            row=I.forward_plan(w)
            assert row['rho']==3*w
            assert I.divergence(row['forward']['current'])==I.atoms((1,3*w),(-1,row['forward']['target']))
            cylinders.append([w,row['forward']['path'],I.table(row['coefficients']),
                              digest(row['current'])])

    lifts=[]
    for b in proofs:
        for D in (4,5,8,16,32,64,128):
            for index in (1,2,3,7):
                row=I.lifted_witness(b,D,index)
                assert I.C.valuation3(row['q']-b)==D+I.C.valuation3(index)
                lifts.append([b,D,index,row['ternary_valuation'],row['forward']['target'],
                              digest(row['forward']['current'])])

    # Exact ray witnesses used by the infinite absorbed-minima proof.
    absorbed_ray=[]
    for index in range(32):
        r=(16*64**index-7)//9
        assert I.NORMAL.canonical(r) and I.NORMAL.quotient_step(r)==1
        absorbed_ray.append(r)

    rejected=0
    def rejects(fn):
        nonlocal rejected
        try:
            fn()
        except (ValueError,AssertionError):
            rejected+=1
        else:
            raise AssertionError('Malformed certificate or domain was accepted')
    original=fixtures[0]
    for mutation in ('omit_origin','wrong_arrow','insert_anchor','wrong_current','wrong_path'):
        bad=copy.deepcopy(original)
        if mutation=='omit_origin':
            bad['quotient_edges']=[r for r in bad['quotient_edges'] if r[0]!=7]
        elif mutation=='wrong_arrow':
            bad['quotient_edges'][1][1]=1
        elif mutation=='insert_anchor':
            bad['quotient_edges'].append([39,I.NORMAL.quotient_step(39)])
        elif mutation=='wrong_current':
            bad['pair_current'][0][1]+=1
        else:
            bad['forward_path'][-1]=1
        rejects(lambda bad=bad:I.verify_certificate(bad))
    rejects(lambda:I.from_table([[1,1],[1,1]]))
    rejects(lambda:I.lifted_witness(135,3))
    rejects(lambda:I.shadow_lift(39,proofs[39]['edges'],47,[('ray0',0)]))
    rejects(lambda:I.forward_plan(5))

    return dict(status='PASS',scope='Finite certificates plus bounded checks; universal quantifiers are proved in INVERSE_SCOPE.md',
                source_sha256=file_digest(HERE/'inverse_scope.py'),
                checker_sha256=file_digest(Path(__file__)),
                certificates_sha256=file_digest(CERTIFICATES),anchors=anchors,
                short_inverse_words=dict(count=len(words),sha256=digest(words),depths=[1,2,3],ray_indices=[0,1]),
                long_inverse_words=dict(count=len(long_words),rows=long_words),
                complete_origin_checks=origins,
                forward_cylinder_plans=dict(count=len(cylinders),sha256=digest(cylinders),indices=[0,63]),
                lifted_forward_witnesses=dict(count=len(lifts),sha256=digest(lifts),maximum_D=128),
                absorbed_ray=dict(count=len(absorbed_ray),sha256=digest(absorbed_ray)),
                rejected_inputs=rejected)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    parser.add_argument('--rebuild-certificates',action='store_true')
    args=parser.parse_args()
    if args.rebuild_certificates:
        fixtures=[I.build_certificate(b) for b in (39,135)]
        CERTIFICATES.write_text(json.dumps(fixtures,indent=2)+'\n')
    result=audit()
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(result,indent=2)+'\n')
    else:
        assert result==json.loads(RECEIPT.read_text()), 'Stored receipt mismatch'
    print('PASS: 2 complete all-depth exclusions; '+str(result['short_inverse_words']['count'])+
          ' short inverse words; '+str(result['long_inverse_words']['count'])+
          ' long words; 4 complete-origin checks; 128 forward plans; '+
          str(result['rejected_inputs'])+' rejected invalid inputs')


if __name__=='__main__':
    main()
