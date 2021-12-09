/* 
** Author : Abhishek Shree (@shree_e)
** There is no Algorithm for Humor.
*/ 

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
using vpii = vector<pii>;
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

vpii dir{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

bool isValid(int rows, int cols, int i, int j)
{
    if (i < 0 || i >= rows) return false;
    if (j < 0 || j >= cols) return false;
    
    return true;
}

// #define MULTITESTS
void solve(){
    freopen("input.txt", "r", stdin);
    string s;
    vector<vi> puzzle;
    while (cin >> s)
    {
        vi curr;
        for (auto x : s) curr.push_back(x - '0');
        puzzle.push_back(curr);
    }

    int rows = puzzle.size();
    int cols = puzzle[0].size();
    
    vpii lowPoints;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            bool low = true;
            for (int k = 0; k < dir.size(); k++) {
                if (isValid(rows, cols, i + dir[k].first, j + dir[k].second) && puzzle[i][j] >= puzzle[i + dir[k].first][j + dir[k].second])
                {
                    low = false;
                }
            }
            if (low) lowPoints.push_back({i, j});
        }
    }

    int sum = 0;
    for (auto x : lowPoints) sum += puzzle[x.first][x.second] + 1;
    cout << sum << endl;

    vi basin;
    for (auto x : lowPoints) {
        // bfs
        queue<pii> q;
        q.push(x);
        int currCount = 1;
        vector<vi> visited(rows, vi(cols, 0));
        visited[x.first][x.second] = 1;
        while (!q.empty()) {
            pii curr = q.front();
            int curr_x = curr.first;
            int curr_y = curr.second;
            q.pop();
            for (int k = 0; k < dir.size(); k++) {
                int next_x = curr_x + dir[k].first;
                int next_y = curr_y + dir[k].second;
                if (isValid(rows, cols, next_x, next_y) && puzzle[curr_x][curr_y] < puzzle[next_x][next_y] && puzzle[next_x][next_y] != 9 && !visited[next_x][next_y])
                {
                    q.push({next_x, next_y});
                    visited[next_x][next_y] = 1;
                    currCount++;
                }
            }
        }
        basin.push_back(currCount);
    }
    sort(rev_all(basin));
    int prod = 1;
    for (int i = 0; i < 3; i++) prod *= basin[i];
    cout << prod << endl;
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