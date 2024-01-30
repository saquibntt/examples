# examples of Gtest 

BUild using 
 
 1) cmake -Bbuild
 2) cmake --build build 
 3)  Run using ./build/a.out
 
Go in build directory and then ctest -V or -VV to see verbose


# Requirement is Gtest should be installed. Follow below steps if its not:

Download Gtest from Github and then do the above 1 and 2 steps
Finally use "sudo cmake --build build --target install", this installs it at /usr/local/lib