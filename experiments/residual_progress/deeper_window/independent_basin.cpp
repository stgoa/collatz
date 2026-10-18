// Complete finite-origin classification. A resource/overflow failure aborts.
// Compact exact-key cache may forget proven states; it never infers a status.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <unordered_map>
#include <vector>
using I = std::int64_t;
constexpr I D=7153, ROOT=899841;
struct Hit { int depth=0,cost=0; };
struct Cache { I key=0; unsigned char state=0; };
constexpr std::size_t CACHE_SIZE=1<<21;
I bound;
std::vector<unsigned char> small;
std::vector<Cache> large(CACHE_SIZE);
std::unordered_map<I,Hit> hit_data;
std::size_t slot(I u) { return (std::uint64_t(u)*11400714819323198485ULL)>>(64-21); }
int get(I u) {
    if(u<bound) return (small[u/8] >> (2*((u/2)%4)))&3;
    const auto &c=large[slot(u)];
    return c.key==u?c.state:0;
}
void put(I u,int state) {
    if(u<bound) {
        auto &b=small[u/8]; int shift=2*((u/2)%4);
        b=(b&~(3<<shift))|(state<<shift);
    } else large[slot(u)]={u,static_cast<unsigned char>(state)};
}
int order(I x) {
    if(!x) throw std::runtime_error("zero valuation argument");
    if(x<0) x=-x;
    return __builtin_ctzll(static_cast<unsigned long long>(x));
}
std::pair<I,int> normalize(I u) {
    int e=0;
    while(u%8==3) {u=(u+D)/4;e+=2;}
    if(u%4==1) {
        int a=order(u-D); I t=(D-u)/(I(1)<<a);
        if((t%4+4)%4==(a%2?3:1)) {u=(u+D)/2;++e;}
    }
    return {u,e};
}
std::pair<I,int> step(I u) {
    if(u>(std::numeric_limits<I>::max()-D)/3)
        throw std::runtime_error("integer overflow guard");
    I v=3*u-D;int e=order(v);v>>=e;
    if(v<=D) return {v,e};
    auto n=normalize(v);return {n.first,n.second+e};
}
int main(int argc,char **argv) {
    try {
        bound=argc>1?std::stoll(argv[1]):741545113;
        if(bound<=ROOT || bound>741545113) throw std::runtime_error("invalid origin bound");
        small.resize(bound/8+1);
        put(ROOT,2);hit_data[ROOT]={0,0};
        std::vector<std::pair<I,int>> path;
        std::unordered_map<I,int> seen;
        std::vector<std::pair<I,Hit>> hits;
        I count=0,escapes=0,cycles=0,largest=0,transitions=0;
        std::size_t longest=0;
        std::uint64_t fp=14695981039346656037ULL;
        for(I start=D+2;start<bound;start+=2) {
            if(start%23==0 || start%311==0 || normalize(start).first!=start) continue;
            ++count;I u=start;int status;Hit h;
            path.clear();seen.clear();
            while(true) {
                largest=std::max(largest,u);
                if(u<=D) {status=1;++escapes;break;}
                status=get(u);
                if(status) {if(status==2) h=hit_data.at(u);break;}
                if(seen.count(u)) {status=1;++cycles;break;}
                if(path.size()>=100000) throw std::runtime_error("path resource cap; unresolved");
                seen[u]=path.size();auto [v,e]=step(u);
                path.push_back({u,e});u=v;++transitions;
            }
            longest=std::max(longest,path.size());
            for(auto it=path.rbegin();it!=path.rend();++it) {
                if(status==2) {++h.depth;h.cost+=it->second;hit_data[it->first]=h;}
                put(it->first,status);
            }
            if(status==2) hits.push_back({start,h});
            for(I value : {start,I(status==2?2:0),I(h.depth),I(h.cost)})
                fp=(fp^std::uint64_t(value))*1099511628211ULL;
            if(count%10000000==0) std::cerr<<"classified "<<count<<" origins through "<<start<<"; hits "<<hits.size()<<'\n';
        }
        std::cout<<"{\"bound\":"<<bound<<",\"candidates\":"<<count<<",\"hits\":[";
        bool comma=false;for(auto [u,h]:hits) {
            if(comma) std::cout<<',';comma=true;
            std::cout<<'['<<u<<','<<h.depth<<','<<h.cost<<']';
        }
        std::cout<<"],\"escape_trees\":"<<escapes<<",\"cycles\":"<<cycles<<",\"largest_u\":"<<largest
                 <<",\"transitions\":"<<transitions<<",\"longest_path\":"<<longest<<",\"cap_hits\":0,\"classification_fingerprint\":\"";
        std::cout<<std::hex;std::cout.width(16);std::cout.fill('0');std::cout<<fp<<"\"}\n";
    } catch(const std::exception &e) {std::cerr<<e.what()<<'\n';return 2;}
}
