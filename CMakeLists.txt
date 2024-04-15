cmake_minimum_required(VERSION 3.22)
project("Gtest")

find_package(GTest REQUIRED)

include(${CMAKE_BINARY_DIR}/dependencies/conan_toolchain.cmake)
conan_basic_setup()

add_executable(a.out main.cpp)
target_link_libraries(a.out ${GTEST_LIBRARIES})

#ctest
#enable_testing()
add_test(add a.out)