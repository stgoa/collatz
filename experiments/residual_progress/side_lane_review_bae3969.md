# Pinned review: the backward negative-cycle word

Date: 2026-10-17. External pin:
`bae3969e5b7f1fde6518586ca5386a1884f729cd`, especially the23:32 feed entry
and `sidekick/probes/backward_word_rule.py`. Repository base:
`87641585b7fbf84d26ce9f5b062cddc71006f33b`; the local R55–R57 additions
were also read for overlap. The external branch was not modified.

**Assessment:** the displayed backward word is correct and its selected-W5
plan decreases rho throughout its exact domain. That domain is precisely
R56's k4 domain, so the feed provides a useful independent interpretation
and check, rather than additional coverage beyond the new batch. Its
random-preimage rate and capped search percentages do not establish a
density theorem or a universal inverse-search obstruction. No new result
number or novelty claim is assigned here.

Merged PR1, `ba6b337`, was checked to be an ancestor of the repository base.
It is the previously integrated PR, whose retained controls and corrected
minimality scope are recorded in the existing
[PR1 review](../../collatz_research_20261017/negative_controls/PR1_REVIEW.md).
The new feed finding must not be presented as a newly merged PR. The
parent's current remote review found no additional merged PR.

## 1. Exact positive word, including the binary precision

Take any **positive odd** q with q=-17 mod2187. Oddness gives exactly

    q=4374n-17,   p=(2048q-2363)/2187=4096n-17,
    n>=1.

Thus p>=4079>0 and q-p=278n>0. Starting from p, the seven ordinary
Syracuse arrows have exact valuations

    (1,1,1,2,1,1,4),

with successive states

    4096n-17, 6144n-25, 9216n-37, 13824n-55,
    10368n-41, 15552n-61, 23328n-91, 4374n-17.

Substitution in3x+1 verifies every division, including the final valuation4:
3(23328n-91)+1=16(4374n-17), whose quotient is odd. Hence S^7(p)=q.
The reversed exponent sequence in the feed is the corresponding inverse
word. The single congruence, together with positive odd q, already supplies
the extra binary bit: p=-17 mod4096. No unproved orbit continuation or
claim about a positive cycle is used.

The negative of these seven arrows has divergence[q]-[p]. The fixed point
-17 explains the affine formula but is not an actual positive source.
The feed's bounded enumeration of negative cycles is a separate finite
observation; it does not prove that no other negative cycle exists.

## 2. The exact current and the stronger rho conclusion

Now assume w in W5 has selected3w and q=nu(3w)=(3w-1)/2 satisfying the
congruence above. Write z=nu(w), let N_x be the elementary current
[x]-[nu(x)], and let H_s be the unchanged formal absorption plan, with
its signed missing W5 currents retained. If I is the positive p-to-q
path current, then

    J=N_(3w)-I+H_p-N_w-H_z

has divergence P(w)-A_p+A_z, where A_s is the signed sum of missing pair
sources in H_s. This agrees with the feed's current signs.

R51 proves sigma(u)<=nu(s) for every request in H_s, so its sigma
argument is valid when sigma(w)=q. Here that equality is automatic:
w=-11 mod729, hence w=1 mod3 and is not in the returning row.

For this particular word **rho also decreases universally**, not merely
in the12 tested cases. The ancestor p is canonical7 mod8. If p=0 or1
mod3, its leading critical input is in W5 and has rank exactly p; all
remaining requests have smaller rank. If p=2 mod3, the first free inverse
step gives bound(3p+1)/4<p. Consequently every request in H_p has
rho<=p<q. Also z< w/4, so every H_z request has rank at most
(9z+5)/8<q. Thus J is a strict-rho conditional plan. Missing input
currents remain premises, and no mixed rho/sigma induction is needed.

This strengthening concerns the displayed seven-arrow word. An arbitrary
smaller ancestor can still yield a sigma-valid plan that fails rho; the
probe's wider selected-unit1 sample itself records31 sigma successes but
only30 rho successes. Do not insert all such search results into the rho
dispatcher without its validator.

## 3. Exact overlap with R56

On selected W5 inputs,

    q=-17 mod2187  iff  w=718 mod729.                 (1)

This is exactly the k4 accepted domain of
[R56](selected_inverse/SELECTED_INVERSE.md), including its selection
hypothesis. To identify the paths, set t=(q+17)/2187 and use R56's v:

    v=(32q-23)/81=864t-7,
    4v+1=27(128t-1),
    h=v3(4v+1)>=3.

The feed's ancestor is the R56 endpoint after exactly three inverse
point steps. When h=3, both constructions use the same ordinary word.
When h>3, R56 continues the maximal point block to

    r+1=(2/3)^(h-3)(p+1),

so r<p. The feed uses a valid nonmaximal stopping point, and the existing
R56 rule goes at least as far.

For R54's q=81*2^K*s-17, condition(1) is precisely27|s. Thus its12
published family examples are contained in R56. R56 also has its second,
disjoint selected class w=4255 mod6561. R55's whole forward domains and
R57's exit families remain complementary mechanisms; in particular R57
has a full CRT subprogression with v=0 mod3, where neither R56 base ray
has a positive point depth. Nothing here completes their union.

## 4. What was actually reproduced

Read and inspected the pinned feed, backward-word probe and its receipt;
also inspected the negative-cycle probe and its receipt for scope. Checks
performed locally:

- 256 direct ordinary-word examples, n=1..256, checking positivity,
  strict inequality, canonical p and all seven exact valuations.
- All12 published R54 family records, r in{1,2,3} and
  s in{27,54,81,135}: reproduced the bounded best-first result, sigma
  validation, reported rho status, ancestor equality, depth and request
  count; the resulting records equal the pinned receipt exactly.
- All12 are accepted by R56's k4 rule, whose maximal ancestor is no larger
  than the probe's ancestor.

The probe's900 random-input acceptance survey and negative-cycle/returning
surveys were **not rerun in this review**. Their reported percentages are
external finite evidence, tied to the old continued dispatcher, a4000-node
budget and height cap64q. The larger-budget percentage in the prose was
not independently reproduced. None of these caps means permanent failure.

The following compact reproduction, run from the repository root, reads
the pinned inspected probe without invoking its file-writing `main`:

```python
import importlib.util, json, subprocess
from pathlib import Path
root = Path.cwd()
ref = 'bae3969e5b7f1fde6518586ca5386a1884f729cd'
def read(path):
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], text=True)
ns = {'__name__': 'reviewed_probe',
      '__file__': str(root/'sidekick/probes/backward_word_rule.py')}
exec(compile(read('sidekick/probes/backward_word_rule.py'), 'pinned_probe', 'exec'), ns)
receipt = json.loads(read('sidekick/probes/backward_word_rule.json'))
spec = importlib.util.spec_from_file_location('new', root/
    'experiments/residual_progress/selected_inverse/selected_inverse.py')
new = importlib.util.module_from_spec(spec)
spec.loader.exec_module(new)
for n in range(1, 257):
    q, p = 4374*n-17, 4096*n-17
    assert 0 < p < q and new.NORMAL.canonical(p)
    x = p
    for a in (1, 1, 1, 2, 1, 1, 4):
        assert new.NORMAL.valuation2(3*x+1) == a
        x = new.NORMAL.step(x)
    assert x == q
records = []
for r in (1, 2, 3):
    for s in (27, 54, 81, 135):
        q = 81*2**(11*r+6)*s-17
        w = (2*q+1)//3
        path = ns['smaller_ancestor'](q)
        plan = ns['plan'](w, path)
        records.append(dict(r=r, s=s, depth=plan['depth'],
            ancestor_is_minus17_word=path[0] == (2048*q-2363)//2187,
            rho_decreasing=plan['rho_decreasing'],
            requests=len(plan['coefficients'])))
        assert w % 729 == 718 and new.recognized(w)
        assert new.pair_plan(w, 4)['parameters']['endpoint'] <= path[0]
assert records == receipt['r54_subfamily_27_divides_s']
print('PASS:256 exact words and12 reproduced family records')
```

Pinned SHA256 values:

| Source | SHA256 |
|---|---|
|`sidekick/FEED.md`|`a464d4ef51bdc44ae8a8c1b842e23f3f93eede8c8f5bd73a09576c39ec3fd06e`|
|`sidekick/probes/backward_word_rule.py`|`be010e694c057236f80473da60d4b6be9a2d47b8e913a058b45697c960aecb19`|
|`sidekick/probes/backward_word_rule.json`|`22238566dc203d7bdece9b8663e61b49145f26f77fdecccc479d8034f8046249`|

## 5. Heuristic scope and direction

For the stated random-residue model, the algebraic moment factor

    M(theta)=3^(theta-1)/(2^theta-1)

has the stated minimum
c^c/[2^c*(c-1)^(c-1)] with c=log_2(3), approximately0.9465.
The model assumption is not a theorem about the correlated inverse trees
of actual integer roots. Nor does an exponentially decaying expected
number of deep smaller ancestors, by itself, prove positive probability
of having none at any depth: that needs a separate non-hitting argument.
There is no justified positive-density or universal search-barrier
conclusion here. R49's proved permanent exclusions remain a separate,
precisely scoped result; no density assertion is imported from the model.

**Recommendation:** continue the combined forward/inverse current programme.
The new feed supports that direction and provides a concise interpretation
of an already proved branch. Keep the useful negative controls and the
corrected PR1 scope. Prioritize full remaining domains or a terminating
compatible comparison, preserving signed premises and one justified rank.
More bounded acceptance samples cannot replace universal input supply.
Collatz remains open in the repository.
