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

int main() {
    std::ios::sync_with_stdio(false);

    int k, n;
    cin >> k >> n;
    vector<vector<bool>> a(k, vector<bool>(k));
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        a[s[0] - 'a'][s[1] - 'a'] = true;
        a[s[1] - 'a'][s[0] - 'a'] = true;
    }
    vector<string> s(2);
    for (int i = 0; i < 2; i++) {
        cin >> s[i];
    }
    for (int x = 0; x < k; x++) {
        for (int y = x + 1; y < k; y++) {
            if (a[x][y]) continue;
            vector<string> q(2);
            for (int j = 0; j < 2; j++) {
                for (char c : s[j]) {
                    if (c == 'a' + x || c == 'a' + y) {
                        q[j] += c;
                    }
                }
            }
            if (q[0] != q[1]) {
                cout << "NO";
                return 0;
            }
        }
    }
    vector<int> num(k);
    for (char c : s[0]) {
        num[c - 'a']++;
    }
    for (char c : s[1]) {
        num[c - 'a']--;
    }
    for (int i = 0; i < k; i++) {
        if (num[i] != 0) {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}