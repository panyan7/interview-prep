#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<long long,long long>

int tt = 1, n, m, k;

void solve() {
    cin >> n;
    set<int> st;
    for (int i = 0; i < n; i++)
        st.insert(i);
    while (st.size() > 1) {
        int i = 0;
        set<int> st_new;
        for (int x : st) {
            if (i % 2 == 0)
                st_new.insert(x);
            i++;
        }
        if (st.size() % 2 == 1)
            st_new.erase(st_new.begin());
        st = st_new;
    }
    cout << *st.begin() << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // cin >> tt;
    while (tt--) {
        solve();
    }
    return 0;
}
