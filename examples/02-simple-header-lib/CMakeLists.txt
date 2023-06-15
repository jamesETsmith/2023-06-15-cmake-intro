# For a detailed discussion see 
# https://discourse.cmake.org/t/interface-library-not-getting-installed-and-no-error-reported/2185 
cmake_minimum_required(VERSION 3.20)

project(simple_header_lib)

add_library(simple_header_lib INTERFACE)
target_include_directories(simple_header_lib
                           INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

install(
  DIRECTORY include
  DESTINATION ${CMAKE_INSTALL_PREFIX}
  FILES_MATCHING
  PATTERN *.hpp)
