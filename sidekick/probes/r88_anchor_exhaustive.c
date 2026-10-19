/* Sidekick probe: exhaustive forward check of R88's anchor (m = 0), independent of main's
 * inverse-tree certificate. For Q = 133704987, n = 385940463, y_a = 3^a (n+1)/2^a - 1 (a = 0..3):
 * every canonical p <= Q is iterated under T = nu o S for up to 22 quotient steps, and every hit
 * T^d(p) = y_a with d <= 19 + a is reported. R88 claims the only hits are p = Q at d = 18 + a.
 * Build: cc -O2 -o /tmp/r88 r88_anchor_exhaustive.c ; run prints the hit list and counts. */
#include <stdio.h>
#include <stdint.h>

static int selected(uint64_t x) {
    if ((x & 3) != 3) return 0;
    uint64_t y = x + 1; int a = __builtin_ctzll(y); uint64_t t = y >> a;
    uint64_t pw = (a % 2 == 0) ? 1 : 3;            /* 3^a mod 4 */
    return (t & 3) == pw;
}
static uint64_t nu(uint64_t x) {
    for (;;) {
        if ((x & 7) == 5 && x != 1) x = (x - 1) >> 2;
        else if (x > 1 && selected(x)) x = (x - 1) >> 1;
        else return x;
    }
}
static uint64_t S(uint64_t x) { uint64_t z = 3 * x + 1; return z >> __builtin_ctzll(z); }

int main(void) {
    const uint64_t Q = 133704987ULL, n = 385940463ULL;
    uint64_t y[4]; uint64_t num = n + 1, den = 1;
    for (int a = 0; a < 4; a++) { y[a] = num / den - 1; if (num % den) { printf("nonint\n"); return 1; } num *= 3; den *= 2; }
    long canonical = 0, hits = 0, bad = 0;
    for (uint64_t p = 3; p <= Q; p += 2) {
        if (nu(p) != p) continue;
        canonical++;
        uint64_t x = p;
        for (int d = 1; d <= 22; d++) {
            x = nu(S(x));
            for (int a = 0; a < 4; a++) {
                if (x == y[a] && d <= 19 + a) {
                    hits++;
                    printf("hit p=%llu d=%d a=%d\n", (unsigned long long)p, d, a);
                    if (!(p == Q && d == 18 + a)) bad++;
                }
            }
            if (x == 1) break;
        }
    }
    printf("canonical=%ld hits=%ld unexpected=%ld y=%llu,%llu,%llu,%llu\n", canonical, hits, bad,
           (unsigned long long)y[0], (unsigned long long)y[1], (unsigned long long)y[2], (unsigned long long)y[3]);
    return bad ? 2 : 0;
}
