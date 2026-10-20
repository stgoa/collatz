#!/usr/bin/env python3
"""Check finite currents WITHOUT solving any new hitting-time problem.

Only exact source-cylinder formulas and arrows inside the stored current are
used. No call to construct_current or an orbit-to-1 routine is made.
"""
from pathlib import Path
from fractions import Fraction
import csv,json
from certificate import source_packets,exact_current_check,initial,push,add,negative
from update_exit_profiles import exit_profiles
from finite_source_bounds import ceil_fifth
ROOT=Path(__file__).resolve().parent


def read(name):
    with (ROOT/'data'/name).open() as f:
        rows=list(csv.DictReader(f))
    data={int(r['state']):int(r['weight']) for r in rows}
    assert len(data)==len(rows)
    return data


def main():
    out=[]
    for N in (4096,262144):
        b=(N-1).bit_length();d=2*b//9
        expected,*_=source_packets(N,d)
        packet=read(f'packets_{N}.csv');J=read(f'current_{N}.csv')
        assert expected==packet
        up,down=exact_current_check(packet,J)
        lo,hi,profiles=exit_profiles(J)
        stored=json.loads((ROOT/f'data/exit_profiles_{N}.json').read_text())
        assert profiles==stored
        mu=initial(N);prefix=[0]
        for j in range(d):prefix.append(prefix[-1]+sum(mu.values()));mu=push(mu)
        residual=add(mu,negative(packet))
        rp=sum(c for c in residual.values() if c>0)
        rn=-sum(c for c in residual.values() if c<0)
        T=ceil_fifth((b+1)**5*N)
        lower=min(min(prefix),prefix[-1]+lo-(T-d)*rn)
        upper=max(max(prefix),prefix[-1]+hi+(T-d)*rp)
        result=dict(N=N,depth=d,packet_atoms=len(packet),current_atoms=len(J),
            uniform_upper=up,uniform_lower=-down,exit_count=len(profiles),
            exit_profile_upper=hi,exit_profile_lower=lo,
            anchor_remainder_positive=rp,anchor_remainder_negative=rn,
            target_horizon=T,full_3E_lower=lower,full_3E_upper=upper)
        cpp=json.loads((ROOT/f'independent_{N}.json').read_text())
        for k,v in result.items():assert cpp[k]==v,(k,cpp[k],v)
        out.append(result)
    (ROOT/'stored_verification.json').write_text(json.dumps(dict(status='PASS',
        no_unverified_tail_followed=True,independent_fields_agree=True,results=out),indent=2)+'\n')
    print(json.dumps(out,indent=2))
    print('All stored identities verified; no unresolved exit continuation was followed.')

if __name__=='__main__':main()
