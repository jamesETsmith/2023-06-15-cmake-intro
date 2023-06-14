cmake_minimum_required(VERSION 3.20)

project(simple_app)

add_library(simple_lib STATIC simple_lib.cpp)
target_include_directories(simple_lib PUBLIC include)

add_executable(simple_app simple_app.cpp)
target_link_libraries(simple_app PUBLIC simple_lib)