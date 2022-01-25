#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    int k = inf.readInt(2, 10, "k");
    inf.readSpace();
    int n = inf.readInt(0, k * (k - 1) / 2, "n");
    inf.readEoln();

    vector<vector<bool>> a(k, vector<bool>(k));
    for (int i = 0; i < n; i++) {
        string s = inf.readToken();
        inf.readEoln();
        ensuref(s.size() == 2, "not a pair");
        int x = s[0] - 'a';
        int y = s[1] - 'a';
        ensuref(x != y, "pair of equal");
        ensuref(!a[x][y], "duplicate pairs");
        a[x][y] = a[y][x] = true;
    }

    int len = 0;
    for (int i = 0; i < 2; i++) {
        string s = inf.readToken();
        inf.readEoln();
        for (char c : s) {
            int x = c - 'a';
            ensuref(x >= 0 && x < k, "bad char");
        }
        if (i == 0) {
            len = s.size();
        } else {
            ensuref(len == s.size(), "not same length");
        }
    }

    inf.readEof();
}