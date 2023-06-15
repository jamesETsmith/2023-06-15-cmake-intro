add_library(simple_lib STATIC simple_lib.cpp)
target_include_directories(simple_lib PUBLIC ${CMAKE_SOURCE_DIR}/include)