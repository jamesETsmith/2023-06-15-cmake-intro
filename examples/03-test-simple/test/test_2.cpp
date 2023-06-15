#include "simple_lib/simple_lib.hpp"

// Bad test designed to fail
int main() {
  int i = 15;
  int ii = square(i);
  bool test_failure = !(i == ii);
  return test_failure;
}