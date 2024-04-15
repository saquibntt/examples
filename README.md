# examples of Gtest 

BUild using 
 
 1) cmake -Bbuild
 2) cmake --build build 
 3)  Run using ./build/a.out
 
Go in build directory and then ctest -V or -VV to see verbose

## Opt1
# To build with conan

1) Run the script python init.py
2) TODO check where the binary is created which can be run

## Opt2
# Requirement is Gtest should be installed. Follow below steps if its not:

1) Clone Gtest from Github https://github.com/google/googletest.git
2) cmake -Bbuild
3) cmake --build build 
4) sudo cmake --build build --target install
