#!/usr/bin/env python3
"""All-horizon packet bounds and target-window full-error bounds at named cutoffs.
The certificates are finite; no extrapolation to other source sizes is made.
"""
from pathlib import Path
from fractions import Fraction
import csv,json
from certificate import initial,push,add,negative,source_packets,construct_current,norm
from update_exit_profiles import exit_profiles
ROOT=Path(__file__).resolve().parent

def ceil_fifth(v):
    lo,hi=0,1
    while hi**5<v:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**5>=v:hi=mid
        else:lo=mid
    assert (hi-1)**5<v<=hi**5
    return hi

if __name__=='__main__':
    summary=[]
    for N in (4096,262144):
        b=(N-1).bit_length();m=2*b//9
        def read(name):
            return {int(r['state']):int(r['weight'])for r in csv.DictReader(open(ROOT/'data'/name))}
        pi=read(f'packets_{N}.csv');J=read(f'current_{N}.csv')
        assert add(J,negative(push(J)))==pi
        low,high,prof=exit_profiles(J)
        mu=initial(N);sums=[]
        for j in range(m):sums.append(sum(mu.values()));mu=push(mu)
        eta=add(mu,negative(pi));ep=sum(c for c in eta.values()if c>0);en=-sum(c for c in eta.values()if c<0)
        T=ceil_fifth((b+1)**5*N)
        prefix=[0]
        for a in sums:prefix.append(prefix[-1]+a)
        upper=max(max(prefix),prefix[-1]+high+(T-m)*ep)
        lower=min(min(prefix),prefix[-1]+low-(T-m)*en)
        summary.append(dict(N=N,b=b,anchor=m,target_horizon=T,early_signed_totals=sums,
            eta_positive=ep,eta_negative=en,eta_norm=ep+en,
            packet_all_horizons_lower=low,packet_all_horizons_upper=high,
            full_3E_target_window_lower=lower,full_3E_target_window_upper=upper,
            full_E_target_window_lower=str(Fraction(lower,3)),full_E_target_window_upper=str(Fraction(upper,3)),
            proof='finite current identity + exit-prefix bounds + exact anchor residual; future residual is bounded without iteration'))
    (ROOT/'finite_source_error_certificates.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
