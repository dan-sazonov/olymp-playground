#include <bits/stdc++.h>
using namespace std;

vector<int> a;
vector<bool> used;
int n, t;

void gen(int p) {
    if (p == n) {
        for (int x : a) {
            cout << x << " ";
        }
        cout << "\n";
        t--;
        return;
    }
    for (int i = 0; i < n; i++) {
        if (!used[i] && i != p) {
            used[i] = true;
            a[p] = i + 1;
            gen(p + 1);
            used[i] = false;
            if (t == 0) {
                break;
            }
        }
    }
}

int main() {
    cin >> n >> t;
    a.resize(n);
    used.resize(n);
    gen(0);
    return 0;
}
