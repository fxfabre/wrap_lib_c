#include <iostream>
#include "cpp_lib.h"

#define SIZE 10


int main()
{
  int exp = 2;
  double data[SIZE] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  unsigned int id;

  id = myProcessorInit(exp, SIZE);
  myProcessorProcess(id, data, SIZE);

  std::cout << "\ndata processed {" << data[0];
  for (int j = 1; j < SIZE; j++) {
    std::cout << ", "<< data[j];
  }
  std::cout << "}\n";

  return 0;
}
