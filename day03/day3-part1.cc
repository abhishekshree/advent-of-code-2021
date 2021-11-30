#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization ("unroll-loops")
#pragma GCC optimize ("-ffloat-store")

#include <bits/stdc++.h>

using namespace std;

// Data types.
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using vvl = vector<vll>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vpll = vector<pll>;
using mii = map<int, int>;
using mll = map<ll, ll>;

// No REPs please.
#define endl            "\n"
#define sz(x)           (int)((x).size())
#define all(v)          v.begin(), v.end()
#define rev_all(v)      v.rbegin(), v.rend()
#define srt(v)          sort(all(v))
#define rev_srt(v)      sort(rev_all(v))
#define unq(v)          (v).erase(unique(all(v)), v.end())

// Not so amazing, but it helps.
#define mp              make_pair
#define pb              push_back
#define pc(x)           __builtin_popcount(x)
#define pcl(x)          __builtin_popcountll(x)

// Magic.
template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }

// Debugging.
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }

#ifndef ONLINE_JUDGE 
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

// Constants.
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;
const double pi=acos(-1.0);


// #define MULTITESTS
void solve(){
    freopen("input.txt", "r", stdin);
    vector<string> v;
    while (true) {
        string s;
        cin >> s;
        v.push_back(s);
        if(  cin.eof() ) break;
    }
    string gamma = "";
    for (int i = 0; i < sz(v[0]); ++i) {
        int count_one = 0, count_zero = 0;
        for (int j = 0; j < sz(v); ++j) {
            if(v[j][i] == '1') count_one++;
            else count_zero++;
        }
        if(count_one > count_zero) gamma += "1";
        else gamma += "0";
    }
    string eps = "";
    for (int i = 0; i < sz(gamma); ++i) {
        if(gamma[i] == '1') eps += "0";
        else eps += "1";
    }
    cout << stoi(gamma, 0, 2) * stoi(eps, 0, 2) << endl;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifdef MULTITESTS
    int tc; cin >> tc;
    for(int i = 1; i <= tc; i++) {
        // cout << "Case #" << i << ": ";
        solve();
    }
    #else
    solve();
    #endif

    return 0;
}