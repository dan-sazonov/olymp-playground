#include "testlib.h"
#include <string>

using namespace std;

int maxn[8] = {3, 10, 1000, 10, 1000, 7, 10, 1000}; 
int maxt[8] = {1, 1, 1, 1, 1, 10000, 10000, 10000};
int zero[8] = {0, 0, 1, 2, 9, 44, 265, 1854};

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    int g = 7;
    if (validator.group() != "") {
        g = stoi(validator.group());
    }

    int n = inf.readInt(2, maxn[g], "n");
    inf.readSpace();
    int t = inf.readInt(1, maxt[g], "t");
    inf.readEoln();
    inf.readEof();

    if (g == 1 || g == 2) {
        ensuref(n % 2 == 0, "n must be even");
    }
    if (g == 3 || g == 4) {
        ensuref(n % 2 == 1, "n must be odd");
    }
    if (g == 5) {
        ensuref(t == zero[n], "t must be equal to the number of zero-fixed permutations");
    }
    ensuref(n * t <= 100000, "n * t must be up to 10^5");

    return 0;
}