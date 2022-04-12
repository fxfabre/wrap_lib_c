#include "cpp_lib.h"

myProcessor::myProcessor(int exp_in, int size_in) {
    this->exp = exp_in;
    this->size = size_in;
}

int myProcessor::process(double *d, int size) {
    for (int i=0; i<size; i++) {
        d[i] = d[i] * d[i];
    }
    return 0;
}
