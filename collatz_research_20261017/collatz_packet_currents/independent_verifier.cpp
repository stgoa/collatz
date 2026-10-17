// C++17. Reconstructs packets by grouping actually iterated source histories;
// verifies the current using one-step arithmetic only. No stopping-time table.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using U=std::uint64_t;
using I=std::int64_t;
using Measure=std::map<U,I>;
struct Entry { U source,endpoint; };

std::pair<U,unsigned> step(U x) {
  if(x<=0 || !(x&1) || x>(std::numeric_limits<U>::max()-1)/3)
    throw std::runtime_error("invalid odd state or overflow");
  U z=3*x+1;unsigned a=0;
  do {z/=2;++a;} while(!(z&1));
  return {z,a};
}
void clean(Measure& m) {
  for(auto it=m.begin();it!=m.end();) {
    if(it->second==0)it=m.erase(it);else ++it;
  }
}
Measure read(const std::string& path) {
  std::ifstream f(path); if(!f)throw std::runtime_error("cannot open "+path);
  std::string line;std::getline(f,line);if(line!="state,weight\r"&&line!="state,weight")throw std::runtime_error("bad header");
  Measure m;
  while(std::getline(f,line)) {
    auto comma=line.find(','); if(comma==std::string::npos)throw std::runtime_error("bad row");
    U y=std::stoull(line.substr(0,comma));I w=std::stoll(line.substr(comma+1));
    if(y<=1 || !(y&1)||!w||m.count(y))throw std::runtime_error("invalid row");
    m[y]=w;
  }
  return m;
}
int main(int argc,char**argv) {
  if(argc!=4){std::cerr<<"args: N depth data_directory\n";return 2;}
  U N=std::stoull(argv[1]);unsigned depth=std::stoul(argv[2]);std::string dir=argv[3];
  if(N<8||N>(1ULL<<24)||depth<1||depth>32)throw std::runtime_error("audit domain");
  unsigned b=0;U z=N-1;while(z){b++;z/=2;}
  std::map<std::string,std::vector<Entry>> groups;
  U steps=0,triples=0;
  Measure actual;std::vector<I> early(depth,0);
  for(U x=3;x<=(3*N+1)/2;x+=2) {
    U y=x;unsigned A=0;std::string word;
    I initial=3*I(x%3==2)-1+(x<=(3*N+1)/4 ? 3*I(x%3==1)-1 : 0);
    for(unsigned j=0;j<depth;++j){if(y>1)early[j]+=initial;auto p=step(y);y=p.first;A+=p.second;word.push_back(char(p.second));steps++;}
    if(y>1)actual[y]+=initial;
    if(y==1||A>b)continue;
    groups[std::string("0")+word].push_back({x,y});
    if(x<=(3*N+1)/4)groups[std::string("1")+word].push_back({x,y});
  }
  Measure packet;
  for(const auto& kv:groups) {
    int residue=kv.first[0]=='0'?2:1;
    const auto& v=kv.second;
    for(size_t i=0;i+2<v.size();i+=3){
      I sum=0;
      for(size_t j=0;j<3;j++){
        const auto& e=v[i+j];I c=3*I(e.source%3==U(residue))-1;
        packet[e.endpoint]+=c;sum+=c;
      }
      if(sum) { throw std::runtime_error("nonzero triple sum"); }
      triples++;
    }
  }
  clean(packet);
  auto expected=read(dir+"/packets_"+std::to_string(N)+".csv");
  if(packet!=expected)throw std::runtime_error("independent packet reconstruction mismatch");
  auto current=read(dir+"/current_"+std::to_string(N)+".csv");
  Measure divergence;U positive=0,negative=0;
  for(auto [y,c]:current){
    divergence[y]+=c;U next=step(y).first;
    if(next>1)divergence[next]-=c;
    if(c>0)positive+=U(c);else negative+=U(-c);
  }
  clean(divergence);
  if(divergence!=packet)throw std::runtime_error("current divergence mismatch");
  std::map<U,std::map<U,I>> levels;
  U graph_steps=0;
  for(auto [y,c]:current) {
    U z=y,d=0;
    while(current.count(z)) {
      z=step(z).first;++d;++graph_steps;
      if(d>current.size())throw std::runtime_error("cycle in current support");
    }
    levels[z][d]+=c;
  }
  I profile_upper=0,profile_lower=0;
  for(auto &kv:levels) {
    I running=0,upper=0,lower=0;
    for(auto [d,c]:kv.second){running+=c;upper=std::max(upper,running);lower=std::min(lower,running);}
    profile_upper+=upper;profile_lower+=lower;
  }
  clean(actual);
  Measure rem=actual;
  for(auto [y,c]:packet)rem[y]-=c;
  clean(rem);U rp=0,rn=0;
  for(auto [y,c]:rem){if(c>0)rp+=U(c);else rn+=U(-c);}
  U target=(b+1)*(b+1)*(b+1)*(b+1)*(b+1)*N,T=1;
  while(T*T*T*T*T<target)++T;
  I prefix=0,earlylow=0,earlyhigh=0;
  for(I c:early){prefix+=c;earlylow=std::min(earlylow,prefix);earlyhigh=std::max(earlyhigh,prefix);}
  I totalupper=std::max(earlyhigh,prefix+profile_upper+I((T-depth)*rp));
  I totallower=std::min(earlylow,prefix+profile_lower-I((T-depth)*rn));
  std::cout<<"{\"N\":"<<N<<",\"depth\":"<<depth<<",\"source_steps\":"<<steps
           <<",\"source_history_groups\":"<<groups.size()<<",\"triples\":"<<triples
           <<",\"packet_atoms\":"<<packet.size()<<",\"current_atoms\":"<<current.size()
           <<",\"uniform_upper\":"<<positive<<",\"uniform_lower\":-"<<negative
           <<",\"exit_count\":"<<levels.size()<<",\"exit_profile_upper\":"<<profile_upper
           <<",\"exit_profile_lower\":"<<profile_lower<<",\"current_graph_steps\":"<<graph_steps
           <<",\"anchor_remainder_positive\":"<<rp<<",\"anchor_remainder_negative\":"<<rn
           <<",\"target_horizon\":"<<T<<",\"full_3E_lower\":"<<totallower<<",\"full_3E_upper\":"<<totalupper
           <<",\"status\":\"PASS\"}\n";
}
