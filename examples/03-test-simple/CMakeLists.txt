cmake_minimum_required(VERSION 3.20)

project(simple_lib)

# src/CMakeLists.txt creates library target
add_subdirectory(src)

enable_testing()
# test/CMakeLists.txt creates test targets and registers them
add_subdirectory(test)
