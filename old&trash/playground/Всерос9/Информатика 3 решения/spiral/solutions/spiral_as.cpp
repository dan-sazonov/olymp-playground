#include <bits/stdc++.h>
using namespace std;

vector<vector<char>> c;

const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};

int main() {
    int n, d, k;
    cin >> n >> d >> k;
    c.resize(2 * n + 1);
    for (auto& d : c) {
        d.resize(2 * n + 1, '.');
    }

    int x = n;
    int y = n;
    int r = 0;
    c[x][y] = '*';
    int steps = 0;
    int minx = x;
    int miny = y;
    int maxx = x;
    int maxy = y;


    for (int i = 0; i < n; i++) {
        steps++;
        x += dx[r];
        y += dy[r];
        minx = min(minx, x);
        miny = min(miny, y);
        maxx = max(maxx, x);
        maxy = max(maxy, y);

        c[x][y] = '*';
        if (steps == d) {
            steps = 0;
            r = (r + 1) % 4;
            if (r % 2 == 0) {
                d *= k;
            }
        }
    }

    cout << maxx - minx + 1 << " " << maxy - miny + 1 << "\n";
    for (int i = minx; i <= maxx; i++) {
        for (int j = miny; j <= maxy; j++) {
            cout << c[i][j];
        }
        cout << "\n";
    }


    return 0;
}
