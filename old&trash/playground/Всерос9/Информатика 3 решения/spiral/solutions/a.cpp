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

    int n, d, k;
    cin >> n >> d >> k;

    int MAX = 2 * n + 1;
    vector<vector<char>> a(MAX, vector<char>(MAX, '.'));

    int x = n;
    int y = n;
    int dx = 0;
    int dy = 1;
    a[x][y] = '*';
    int c = 0;
    int q = d;
    int minx = n;
    int maxx = n;
    int miny = n;
    int maxy = n;
    while (n > 0) {
        if (q == 0) {
            std::swap(dx, dy);
            dx = -dx;
            c++;
            if (c % 2 == 0) {
                d *= k;
            }
            q = d;
        }
        x += dx;
        y += dy;
        a[x][y] = '*';
        n--;
        q--;
        minx = std::min(x, minx);
        maxx = std::max(x, maxx);
        miny = std::min(y, miny);
        maxy = std::max(y, maxy);
    }

    cout << (maxx - minx + 1) << " " << (maxy - miny + 1) << "\n";
    for (int i = minx; i <= maxx; i++) {
        for (int j = miny; j <= maxy; j++) {
            cout << a[i][j];
        }
        cout << "\n";
    }

    return 0;
}