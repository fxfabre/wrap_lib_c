#include <iostream>
#include "cpp_lib.h"

typedef unsigned int uint;


int main()
{
  int exp = 2;
  int size = 10;
  double data[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  myProcessor* processor;

  processor = new myProcessor(exp, size);
  processor->process(data, size);

  std::cout << "\ndata processed {" << data[0];
  for (int j=1; j<size; j++) {
    std::cout << ", "<< data[j];
  }
  std::cout << "}\n";

  return 0;
}
