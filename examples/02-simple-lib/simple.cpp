#include <iostream>

// No return value should trigger compile-time warning
int func() { std::cout << "I'm inside of simple_target" << std::endl; }