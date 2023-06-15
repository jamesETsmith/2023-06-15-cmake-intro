
add_executable(test_1 ${CMAKE_CURRENT_SOURCE_DIR}/test_1.cpp)
target_link_libraries(test_1 PUBLIC simple_lib)
add_test(NAME test_1_fancy_name COMMAND test_1)

# This test is written to fail
add_executable(test_2 ${CMAKE_CURRENT_SOURCE_DIR}/test_2.cpp)
target_link_libraries(test_2 PUBLIC simple_lib)
add_test(NAME test_2_fancy_name COMMAND test_2)

# Add a third test called test_3