// R91 independent finite classifier, using positive numerator u=-D*x.
// Any cap or overflow aborts; neither is classified as nonmembership.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <stdexcept>
#include <unordered_map>
#include <vector>

using Integer = std::int64_t;
constexpr Integer D = 7153, ROOT = 899841, LIMIT = 7277133;
struct Record { int state = 0, depth = 0, cost = 0; };
std::vector<Record> small(LIMIT / 2 + 1);
std::unordered_map<Integer, Record> large;

Record get(Integer u) {
    if (u < LIMIT) return small[u / 2];
    auto found = large.find(u);
    return found == large.end() ? Record{} : found->second;
}
void put(Integer u, Record r) {
    if (u < LIMIT) small[u / 2] = r;
    else large[u] = r;
}
int order(Integer n) {
    if (n < 0) n = -n;
    if (!n) throw std::runtime_error("zero valuation argument");
    return __builtin_ctzll(static_cast<unsigned long long>(n));
}
std::pair<Integer, int> normal(Integer u) {
    int e = 0;
    while (u % 8 == 3) { u = (u + D) / 4; e += 2; }
    if (u % 4 == 1) {
        int a = order(u - D);
        Integer t = (D - u) / (Integer(1) << a);
        int mod = static_cast<int>((t % 4 + 4) % 4);
        if (mod == (a % 2 ? 3 : 1)) { u = (u + D) / 2; ++e; }
    }
    return {u, e};
}
std::pair<Integer, int> next(Integer u) {
    if (u > std::numeric_limits<Integer>::max() / 3 - 1)
        throw std::runtime_error("integer overflow guard");
    Integer q = 3 * u - D;
    int a = order(q);
    q >>= a;
    if (q <= D) return {q, a};
    auto n = normal(q);
    return {n.first, n.second + a};
}

int main() {
    try {
        put(ROOT, {1, 0, 0});
        struct Hit { Integer u; int depth, cost; };
        std::vector<Hit> hits;
        Integer candidates = 0, escaped = 0, cycles = 0, max_u = 0;
        std::uint64_t fingerprint = 14695981039346656037ULL;
        for (Integer start = D + 2; start < LIMIT; start += 2) {
            if (std::gcd(start, D) != 1 || normal(start).first != start) continue;
            ++candidates;
            Integer u = start;
            std::vector<std::pair<Integer, int>> path;
            std::unordered_map<Integer, int> index;
            Record result;
            while (true) {
                max_u = std::max(max_u, u);
                if (u <= D) { result = {-1, 0, 0}; ++escaped; break; }
                result = get(u);
                if (result.state) break;
                if (index.count(u)) { result = {-1, 0, 0}; ++cycles; break; }
                if (path.size() >= 100000)
                    throw std::runtime_error("finite basin path reached the resource cap");
                index[u] = static_cast<int>(path.size());
                auto [v, e] = next(u);
                path.push_back({u, e});
                u = v;
            }
            for (auto it = path.rbegin(); it != path.rend(); ++it) {
                if (result.state == 1) { ++result.depth; result.cost += it->second; }
                put(it->first, result);
            }
            Record r = get(start);
            if (r.state != 1 && r.state != -1)
                throw std::runtime_error("unclassified origin");
            if (r.state == 1) hits.push_back({start, r.depth, r.cost});
            for (Integer value : {start, Integer(r.state + 1), Integer(r.depth), Integer(r.cost)})
                fingerprint = (fingerprint ^ static_cast<std::uint64_t>(value)) * 1099511628211ULL;
        }
        std::cout << "{\"candidates\":" << candidates << ",\"hits\":[";
        bool first = true;
        for (auto h : hits) {
            if (!first) std::cout << ',';
            first = false;
            std::cout << '[' << h.u << ',' << h.depth << ',' << h.cost << ']';
        }
        std::cout << "],\"escape_trees\":" << escaped << ",\"cycles\":" << cycles
                  << ",\"largest_u\":" << max_u << ",\"large_cache\":" << large.size()
                  << ",\"cap_hits\":0,\"classification_fingerprint\":\"";
        std::cout << std::hex;
        std::cout.width(16); std::cout.fill('0'); std::cout << fingerprint;
        std::cout << "\"}\n";
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 2;
    }
}
