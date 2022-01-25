#include "testlib.h"
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    inf.readInt(1000, 10000, "w");
    inf.readEoln();
    inf.readInt(1000, 10000, "l");
    inf.readEoln();
    inf.readInt(1000, 10000, "h");
    inf.readEoln();
    inf.readEof();

    return 0;
}