#include "simple_lib/simple_lib.hpp"

int main() {
  int i = 10;
  int ii = square(i);
  bool test_failure = !((i * i) == ii);
  return test_failure;
}