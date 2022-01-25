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

long gcd(long a, long b) {
    while (b > 0) {
        long c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int main() {
    std::ios::sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    vector<long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<pair<long, long>> s1;
    vector<pair<long, long>> s2;
    s1.push_back({0, 0});
    s2.push_back({0, 0});
    for (int i = 0; i < k; i++) {
        s1.push_back({a[i], gcd(a[i], s1.back().second)});
    }
    long res = s1.back().second;
    for (int i = 0; i + k < n; i++) {
        s1.push_back({a[i + k], gcd(a[i + k], s1.back().second)});
        if (s2.size() == 1) {
            while (s1.size() > 1) {
                long x = s1.back().first;
                s1.pop_back();
                s2.push_back({x, gcd(x, s2.back().second)});
            }
        }
        s2.pop_back();
        res = std::max(res, gcd(s1.back().second, s2.back().second));
    }
    cout << res << "\n";

    return 0;
}