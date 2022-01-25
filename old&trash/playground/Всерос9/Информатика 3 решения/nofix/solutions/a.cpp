#include <cstdio>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

#define MIN_INT -2147483648
#define MAX_INT 2147483647
#define MIN_LONG -9223372036854775808L
#define MAX_LONG 9223372036854775807L
#define PI 3.141592653589793238462643383279502884L

#define long long long int

using std::vector;
using std::map;
using std::set;
using std::string;
using std::pair;
using std::cin;
using std::cout;
using std::cerr;

// @author: pashka

int n, t;
vector<int> p;
vector<bool> z;

void bt(int i) {
    if (t == 0) return;
    if (i == n) {
        t--;
        for (int j = 0; j < n; j++) {
            cout << p[j] + 1 << " ";
        }
        cout << "\n";
        return;
    }
    for (int j = 0; j < n; j++) {
        if (j != i && !z[j]) {
            p[i] = j;
            z[j] = true;
            bt(i + 1);
            z[j] = false;
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);

    cin >> n >> t;

    p.resize(n);
    z.resize(n);

    bt(0);

    return 0;
}