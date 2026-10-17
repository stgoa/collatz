"""Reproduce exact two-run and canonical-return certificates and counts."""
import argparse
import csv
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import run_bridge as R

HERE=Path(__file__).resolve().parent

def digest(table):
    return hashlib.sha256(''.join(f'{x},{c}\n' for x,c in sorted(table.items())).encode()).hexdigest()

def run():
    seed_checks=0
    for x in range(3,32768,4):
        if R.H.selected(x):continue
        data=R.normalized_bridge(x)
        a,t,d,w=R.parameters(x)
        residue,period=R.cylinder(a,d)
        assert x%period==residue
        assert data['target']<=data['raw_target']
        seed_checks+=1
    parameter_checks=0
    for a in range(2,33):
        for d in range(2,33):
            residue,period=R.cylinder(a,d)
            for offset in (0,1,7):
                x=residue+period*offset
                data=R.normalized_bridge(x)
                aa,t,dd,w=R.parameters(x)
                assert (aa,dd)==(a,d)
                C=3**(d//2);A=C*3**(a-1)
                left=(2**(a+d)-(A if d%2 else 2*A))*t
                right=2**d-C if d%2 else 2**(d+1)-2*C
                assert (R.target(x)<x)==(left>right)
                if d%2 and a<=5:assert R.target(x)<x
                parameter_checks+=1

    cutoffs=[*range(8,513,8),768,1024,1536,6144]
    profiles=[]
    for N in cutoffs:
        raw=R.selected_profile(N);normalized=R.normalized_profile(N)
        assert set(raw)<=set(normalized)
        raw_mass=R.mass_formula(N)
        normal_mass=R.normalized_mass_formula(N)
        assert raw_mass==sum(raw.values())
        assert normal_mass==sum(normalized.values())
        old=R.H.COMPLEMENT.residual_mass_formula(N)-R.H.selected_mass_formula(N)
        profiles.append(dict(N=N,prior_complement_mass=old,raw_removed=raw_mass,
                             normalized_removed=normal_mass,remaining=old-normal_mass,
                             normalized_weight2_roots=sum(c==2 for c in normalized.values())))

    alpha_low,alpha_high=R.leading_interval(64)
    beta_low,beta_high=R.normalized_leading_interval(64)
    assert 0<alpha_low<alpha_high<beta_low<beta_high<F(25,576)
    series=[]
    last_low,last_high=F(0),F(1)
    for K in (4,8,16,32,64):
        low,high=R.normalized_leading_interval(K)
        assert last_low<=low<high<=last_high
        last_low,last_high=low,high
        series.append(dict(K=K,lower=str(low),upper=str(high)))
    for row in profiles:
        N=row['N'];A=(3*N//2).bit_length()-1;K=3*A
        error=F(7*(K-3)*(K-2),2)+1
        assert alpha_low*N-error <= row['raw_removed'] <= alpha_high*N+error

    conversions=[];stored=None
    for N in (24,32,96,168,384,768,6144):
        lower=R.H.LOCAL.FORCING.absorption_current(R.H.LOCAL.count(N),cap=1000)
        data=R.certify_normalized(N,lower)
        assert sum(data['removed'].values())==R.normalized_mass_formula(N)
        conversions.append(dict(N=N,input_rows=len(lower),input_sha256=digest(lower),
                                removed_mass=sum(data['removed'].values()),
                                remaining_mass=sum(data['remaining'].values()),
                                output_rows=len(data['current']),output_sha256=digest(data['current']),
                                new_explicit_rows=len(data['new_rows'])))
        if N==168:
            assert data['removed'][187]==2 and R.target(187)==211 and R.normal_target(187)==105
            stored=R.H.COMPLEMENT.extract_exact({187:2},{x:R.step(x) for x in data['current']})
        if N in (96,768):
            geo=R.H.LOCAL.geometry(N)
            inner=R.H.COMPLEMENT.extract_exact(geo['inner'],{x:R.step(x) for x in lower})
            r17=R.H.COMPLEMENT.improve_packet(N,inner)
            r23=R.H.certify_selected(N,lower)
            upgraded=R.combine((1,r17['packet_current']),(-1,r23['current']),(-1,data['current']))
            assert R.combine((1,R.divergence(upgraded)),(-1,data['remaining']))==geo['packet']
            conversions[-1]['full_packet_upgrade_verified']=True

    escape=[]
    for a in (7,23,39,71,135,263):
        x=2**a-1;N=12*2**(a-4)
        data=R.normalized_bridge(x)
        assert R.H.TRANSFER.residual_coefficient(N,x)==1
        assert R.parameters(x)[2]==3
        assert data['target']==data['raw_target']==(3**a-3)//8
        assert data['target']%8==1 and data['target']>x
        escape.append(dict(a=a,N=N,root=x,canonical_return=data['target']))
    cycle=[]
    for x in (27,31,91):
        a,t,d,w=R.parameters(x)
        cycle.append(dict(root=x,a=a,d=d,raw_return=R.target(x),canonical_return=R.normal_target(x)))
    assert cycle[0]['canonical_return']==31 and cycle[1]['canonical_return']==91
    assert (cycle[0]['a'],cycle[0]['d'])==(cycle[2]['a'],cycle[2]['d'])==(2,2)
    example=R.normalized_bridge(187)
    return dict(status='PASS',scope='Complete two-run/canonical rule with explicit residual; universal closure open',
                complementary_seed_range=[3,32767,4],complementary_seeds_checked=seed_checks,
                parameter_domain=dict(a=[2,32],d=[2,32],offsets=[0,1,7],cases=parameter_checks),
                profile_cases=profiles,raw_leading_bounds=[str(alpha_low),str(alpha_high)],
                normalized_leading_bounds=[str(beta_low),str(beta_high)],
                normalized_remaining_bounds=[str(F(25,576)-beta_high),str(F(25,576)-beta_low)],
                nested_series_enclosures=series,finite_absorption_input_cap=1000,
                actual_conversions=conversions,normalized_unbounded_returns=escape,
                parameter_label_cycle=cycle,coefficient_two_example=dict(N=168,root=187,
                    raw_return=211,canonical_return=105,arithmetic_prefix=example['arithmetic']['left'],
                    normalization_left=example['normalization']['left_prefix'],
                    normalization_right=example['normalization']['right_prefix'],
                    current_rows=len(stored),current_sha256=digest(stored))),stored

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    receipt,current=run()
    receipt_path=HERE/'run_bridge_audit.json';table_path=HERE/'outer_187_double_current.csv'
    if args.write_receipt:
        receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
        with table_path.open('w',newline='') as output:
            writer=csv.writer(output,lineterminator='\n');writer.writerow(('state','current'))
            writer.writerows(sorted(current.items()))
    else:
        assert json.loads(receipt_path.read_text())==receipt
        with table_path.open(newline='') as source:
            saved={int(row['state']):int(row['current']) for row in csv.DictReader(source)}
        assert saved==current
    print(f"PASS: {receipt['complementary_seeds_checked']} seeds; "
          f"{receipt['parameter_domain']['cases']} parameter branches; "
          f"{len(receipt['profile_cases'])} exact normalized counts; "
          f"{len(receipt['actual_conversions'])} supplied-input conversions")

if __name__=='__main__':main()
