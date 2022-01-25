#include "testlib.h"
#include <string>

using namespace std;

int maxn[8] = {100, 100, 100, 100, 100, 100, 500000, 500000}; 
int maxk[8] = {100, 2, 2, 2, 100, 100, 500000, 500000};
long long maxv[8] = {100, 100, 1000000000, 1000000000000000000LL, 100, 1000000000000000000LL, 100, 1000000000000000000LL};

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    int g = 7;
    if (validator.group() != "") {
        g = stoi(validator.group());
    }

    int n = inf.readInt(2, maxn[g], "n");
    inf.readSpace();
    int k = inf.readInt(2, maxk[g], "k");
    inf.readEoln();

    ensuref(k <= n, "k <= n");

    for (int i = 0; i < n; i++) {
        inf.readLong(1, maxv[g], format("a[%d]", i + 1));
        if (i < n - 1) {
            inf.readSpace();
        }
    }
    inf.readEoln();
    inf.readEof();

    return 0;
}