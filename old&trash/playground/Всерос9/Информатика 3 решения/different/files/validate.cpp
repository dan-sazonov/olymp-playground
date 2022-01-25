#include "testlib.h"
#include <string>

using namespace std;

long long maxn[5] = {100, 1000, 1000000000, 1000000000000, 1000000000000000000}; 

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    int g = 4;
    if (validator.group() != "") {
        g = stoi(validator.group());
    }

    inf.readLong(1, maxn[g], "n");
    inf.readEoln();
    inf.readEof();

    return 0;
}