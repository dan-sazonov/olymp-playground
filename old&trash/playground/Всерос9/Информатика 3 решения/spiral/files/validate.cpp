#include "testlib.h"
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    registerValidation(argc, argv);

    inf.readInt(1, 1000, "n");
    inf.readSpace();
    inf.readInt(1, 100, "d");
    inf.readSpace();
    inf.readInt(2, 5, "k");
    inf.readEoln();
    inf.readEof();

    return 0;
}