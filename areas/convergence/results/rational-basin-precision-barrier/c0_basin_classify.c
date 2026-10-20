/* Sidekick probe: classify the c0 = -899841/7153 basin of the signed canonical quotient T on rationals
 * -u/D (D = 7153), for all odd u in (D, U) with gcd(u, D) = 1 and -u/D canonical.
 * Conventions follow R91 (main shadow_precision/SHADOW_PRECISION.md, Section 2), positive magnitudes:
 *   z = (3u - D)/2^v2(3u - D); while -z/D = 5 mod 8 (z = 3 mod 8): z = (z + D)/4 (e += 2);
 *   then if -z/D is selected: z = (z + D)/2 (e += 1). e also includes v. New u = z.
 * Each origin is followed until it hits c0 (u = 899841), enters x > -1 (u < D), meets an already
 * classified origin (memo over odd u < U), or closes another cycle (Brent). For c0 hits the first-hit
 * depth d0 and exponent sum E0 are recorded; the weighted slope mu = 2^E0/3^d0 * (3^12/2^19)^k,
 * k = max(0, ceil((d0-5)/12)), must be >= 1 (R91). Usage: ./c0b U   (R91 universe: U = 7277133;
 * main's deeper-window candidate (8): U = 741545113). Prints counts and every c0-basin origin. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

typedef long long i64;
static const i64 D = 7153, C0 = 899841;

static int selected_neg(i64 z) {         /* is x = -z/D selected? */
    if (((z % 4) + 4) % 4 != 1) return 0; /* x = 3 mod 4  <=>  z = 1 mod 4 */
    i64 w = D - z;                        /* x + 1 = (D - z)/D */
    if (w == 0) return 0;
    i64 aw = w < 0 ? -w : w;
    int a = __builtin_ctzll((unsigned long long)aw);
    i64 t = w / ((i64)1 << a);            /* exact */
    int tm = (int)(((t % 4) + 4) % 4);
    return tm == ((a % 2 == 0) ? 1 : 3);
}
static int canonical_neg(i64 u) {
    if (u % 8 == 3) return 0;            /* -u/D = 5 mod 8 */
    return !selected_neg(u);
}
static i64 Tstep(i64 u, int *e) {
    __int128 z = (__int128)3 * u - D;    /* > 0 since u > D */
    int v = 0;
    while ((z & 1) == 0) { z >>= 1; v++; }
    int ee = v;
    while ((i64)(z % 8) == 3) { z = (z + D) / 4; ee += 2; }
    if (selected_neg((i64)z)) { z = (z + D) / 2; ee += 1; }
    if (z > (__int128)4000000000000000000LL) { fprintf(stderr, "overflow risk at u=%lld\n", u); exit(3); }
    *e = ee;
    return (i64)z;
}

/* memo for odd u < U: 0 unknown, 1 not in basin, 2 in basin (details in arrays) */
static unsigned char *memo;
static int *bd; static int *be;           /* first-hit depth/exponent for basin origins (index u/2) */

int main(int argc, char **argv) {
    i64 U = argc > 1 ? atoll(argv[1]) : 7277133;
    size_t n = (size_t)(U / 2 + 1);
    memo = calloc(n, 1); bd = calloc(n, sizeof(int)); be = calloc(n, sizeof(int));
    if (!memo || !bd || !be) { fprintf(stderr, "alloc\n"); return 1; }
    /* c0 cycle: mark its states (all have u < U for the R91 universe; keep a separate list) */
    i64 cyc[12]; int cyce[12]; { i64 u = C0; for (int i = 0; i < 12; i++) { cyc[i] = u; u = Tstep(u, &cyce[i]); } if (u != C0) { printf("c0 not 12-cycle\n"); return 2; } }
    long eligible = 0, basin = 0, other = 0, inv = 0, memohits = 0, maxlen = 0; i64 maxnum = 0;
    double minmu = 1e300; i64 path_u[4096]; int path_e[4096];
    for (i64 u0 = D + 2; u0 < U; u0 += 2) {
        if (u0 % 23 == 0 || u0 % 311 == 0 || !canonical_neg(u0)) continue;   /* gcd(u, 7153 = 23*311) = 1 */
        eligible++;
        if (memo[u0 / 2]) continue;
        /* follow the orbit */
        int len = 0; i64 u = u0; int status = 0; int hd = 0, he = 0;
        i64 brent_pow = 1, brent_lam = 0, brent_x = u;
        for (;;) {
            if (u == C0) { status = 2; hd = 0; he = 0; break; }
            if (u < D) { status = 1; break; }
            if (u < U && u != u0 && memo[u / 2]) { status = memo[u / 2]; if (status == 2) { hd = bd[u / 2]; he = be[u / 2]; } memohits++; break; }
            if (len >= 4096) { fprintf(stderr, "path cap at u0=%lld\n", u0); return 4; }
            int e; i64 nu_ = Tstep(u, &e);
            path_u[len] = u; path_e[len] = e; len++;
            if (nu_ > maxnum) maxnum = nu_;
            u = nu_;
            /* Brent cycle detection against non-c0 cycles */
            brent_lam++;
            if (u == brent_x) { status = 1; break; }       /* closed a cycle without meeting c0 */
            if (brent_lam == brent_pow) { brent_x = u; brent_pow *= 2; brent_lam = 0; }
        }
        if (len > maxlen) maxlen = len;
        /* propagate backwards along the path */
        for (int i = len - 1; i >= 0; i--) {
            i64 w = path_u[i];
            if (status == 2) { hd += 1; he += path_e[i]; }
            if (w < U && w > D && (w & 1)) {
                if (!memo[w / 2]) { memo[w / 2] = (unsigned char)status; if (status == 2) { bd[w / 2] = hd; be[w / 2] = he; } }
            }
        }
        if (u0 == C0) { memo[u0 / 2] = 2; bd[u0 / 2] = 0; be[u0 / 2] = 0; }
    }
    /* report basin origins among eligible */
    printf("U=%lld eligible=%ld memohits=%ld maxpath=%ld maxnum=%lld\n", U, eligible, memohits, maxlen, maxnum);
    double lg = 12*log(3.0) - 19*log(2.0);
    long relevant = 0, mbad = 0;
    for (i64 u0 = D + 2; u0 < U; u0 += 2) {
        if (u0 % 23 == 0 || u0 % 311 == 0 || !canonical_neg(u0)) continue;   /* gcd(u, 7153 = 23*311) = 1 */
        if (memo[u0 / 2] == 2) {
            basin++;
            int d = bd[u0 / 2], E = be[u0 / 2];
            int k = d <= 5 ? 0 : (d - 5 + 11) / 12;
            double logmu = E*log(2.0) - d*log(3.0) + k*lg;
            if (logmu < log(minmu)) minmu = exp(logmu);
            int rel = (d % 12 == 5);
            int m = rel ? E - 19*((d - 5)/12) : 0;
            if (rel) { relevant++; if (m < 8 || m > 14) mbad++; }
            if (rel) printf("relevant u=%lld d0=%d E0=%d k0=%d m=%d mu=%.6f%s\n", u0, d, E, (d - 5)/12, m, exp(logmu),
                            (m >= 8 && m <= 14) ? "  <-- candidate cost list" : "");
        } else if (memo[u0 / 2] == 1) other++;
    }
    printf("basin=%ld not_basin=%ld unknown=%ld relevant(d0=5 mod 12)=%ld m_outside_8_14=%ld min_mu=%.9f\n",
           basin, other, eligible - basin - other, relevant, mbad, minmu);
    return 0;
}
