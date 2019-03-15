# Some problem about *Modern C++ Programming with Test-Driven Development*

On Ubuntu

## 1. installing of GoogleMock

### 1.1 download

When I access `http://code/google.com/p/googlemock/downloads/list`, I have been redriected to `https://github.com/google/googlemock`, and this page tells that * the googlemock project has been absorbed into the GoogleTest project. * .

Then I open `https://github.com/google/googletest`, found it contains both gooletest and googlemock, so I use `git clone https://github.com/google/googletest.git` to download them all.

Here is what I get:
```bash
git clone https://github.com/google/googletest.git
cd googletest
ll
```

Output:

```bash
总用量 96
drwxr-xr-x  6 eric eric 4096 3月  12 20:07 ./
drwxr-xr-x 33 eric eric 4096 3月  15 12:18 ../
-rw-r--r--  1 eric eric 5093 3月   5 21:39 appveyor.yml
-rw-r--r--  1 eric eric 5512 3月   5 21:39 BUILD.bazel
drwxr-xr-x  2 eric eric 4096 3月   5 21:39 ci/
-rw-r--r--  1 eric eric  116 3月   5 21:39 .clang-format
-rw-r--r--  1 eric eric  796 3月   5 21:39 CMakeLists.txt
-rw-r--r--  1 eric eric  461 3月   5 21:39 configure.ac
-rw-r--r--  1 eric eric 6801 3月   5 21:39 CONTRIBUTING.md
-rw-r--r--  1 eric eric 1561 3月   5 21:39 .gitignore
drwxr-xr-x 12 eric eric 4096 3月  12 20:08 googlemock/
drwxr-xr-x 15 eric eric 4096 3月  12 20:09 googletest/
-rw-r--r--  1 eric eric 1960 3月   5 21:39 library.json
-rw-r--r--  1 eric eric 1475 3月   5 21:39 LICENSE
-rw-r--r--  1 eric eric  290 3月   5 21:39 Makefile.am
drwxr-xr-x  6 eric eric 4096 3月  12 20:07 mybuild/
-rw-r--r--  1 eric eric 1173 3月   5 21:39 platformio.ini
-rw-r--r--  1 eric eric 5438 3月   5 21:39 README.md
-rw-r--r--  1 eric eric 2824 3月   5 21:39 .travis.yml
-rw-r--r--  1 eric eric  283 3月   5 21:39 WORKSPACE

```

### 1.2installing

The book suggests creating the envirement `GMOCK_HOME` first:

```bash
export GMOCK_HOME=/home/jeff/gmock-1.6.0

mkdir mybuild
cd mybuild
cmake ..
make
```

So I goto `googletest/googlemock`:

```bash
cd googletest/googlemock

export GMOCK_HOME=/home/eric/googletest/googlemock

mkdir mybuild
cd mybuild
cmake ..
make
```

It works well.

Then gtest. the book suggests:

```bash
cd $GMOCK_HOME/gtest
mkdir mybuild
cd mybuild
cmake ..
make
```

I do found a filefolder named `gtest` in `$GMOCK_HOME`, but it does not contains any file to let me run `cmake`.

```bash
eric@eric-vm:~/googletest/googlemock/mybuild$ cd gtest/
eric@eric-vm:~/googletest/googlemock/mybuild/gtest$ ll
总用量 24
drwxr-xr-x 3 eric eric 4096 3月  12 20:08 ./
drwxr-xr-x 6 eric eric 4096 3月  12 20:08 ../
drwxr-xr-x 4 eric eric 4096 3月  12 20:08 CMakeFiles/
-rw-r--r-- 1 eric eric 1122 3月  12 20:08 cmake_install.cmake
-rw-r--r-- 1 eric eric 7183 3月  12 20:08 Makefile
eric@eric-vm:~/googletest/googlemock/mybuild/gtest$ mkdir mybuild
eric@eric-vm:~/googletest/googlemock/mybuild/gtest$ cd mybuild/
eric@eric-vm:~/googletest/googlemock/mybuild/gtest/mybuild$ cmake ..
CMake Error: The source directory "/home/eric/googletest/googlemock/mybuild/gtest" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.

```

But it contains a `Makefile`, so i run `make`:

```bash
eric@eric-vm:~/googletest/googlemock/mybuild/gtest$ make
[ 50%] Built target gtest
[100%] Built target gtest_main
```

I don't know is this enough so I install googletest too:

```bash
 cd ~/googletest/googletest/

 mkdir mybuild
 cd mybuild

 cmake ..
 make
 ```

I noticed the `googletest` filefolder also contains a `CMakeLists.txt`.so i done the same operations:

```bash
cd googletest/
mkdir mybuild
cd mybuild

cmake ..
make
```
Here is what i done to installing the GoogleMock, i am not sure is there any wrong operation.

## 2. run some chapter2's code

Here I use `c2/4/SoundexTest.cpp` to make a test.

```bash
# CMakeLists.txt
project(chapterFirstExample)
cmake_minimum_required(VERSION 2.6)

include_directories($ENV{GMOCK_HOME}/include $ENV{GMOCK_HOME}/gtest/include)
link_directories($ENV{GMOCK_HOME}/mybuild $ENV{GMOCK_HOME}/gtest/mybuild)
add_definitions(-std=c++0x)
set(CMAKE_CXX_FLAGS "${CMAXE_CXX_FLAGS} -Wall")

set(sources 
   main.cpp 
   SoundexTest.cpp)
add_executable(test ${sources})
target_link_libraries(test pthread)
target_link_libraries(test gmock)
target_link_libraries(test gtest)
```

```C++
// main.cpp
#include "gmock/gmock.h"

int main(int argc, char** argv) {

   testing::InitGoogleMock(&argc, argv);

   return RUN_ALL_TESTS();
}
```

```C++
// SoundexTest.cpp
#include <string>

class Soundex
{
public:
   std::string encode(const std::string& word) const {
      return "";
   }
};


#include "gmock/gmock.h"

TEST(SoundexEncoding, RetainsSoleLetterOfOneLetterWord) {
   Soundex soundex;
   
   auto encoded = soundex.encode("A");
}
```

In the last step, when i run `export GMOCK_HOME=/home/eric/googletest/googlemock`, it suouldn't be a permanent operation. so when i use `GMOCK_HOME` in `CMakeLists.txt`, it can't find this path unless i run this command first.

So i write it in `~/bashrc`:

```bash
# added by GoogleTest
export GTEST_HOME="/home/eric/googletest/googletest"

# added by GoogleMock
export GMOCK_HOME="/home/eric/googletest/googlemock"
```

Then start to compile:

```bash
cd lotdd-code/code/c2/4/
cmake .
```

Output:

```bash
-- The C compiler identification is GNU 8.2.0
-- The CXX compiler identification is GNU 8.2.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/eric/Projects/C++/lotdd-code/code/c2/4
```

Then:

```bash
make
```

The output is very long:

```bash
...

make[2]: *** [CMakeFiles/test.dir/build.make:63：CMakeFiles/test.dir/main.cpp.o] 错误 1
make[1]: *** [CMakeFiles/Makefile2:73：CMakeFiles/test.dir/all] 错误 2
make: *** [Makefile:84：all] 错误 2
```

Then I modify these two lines in `CMakeLists.txt`:

```bash
include_directories($ENV{GMOCK_HOME}/include $ENV{GTEST_HOME}/include)
link_directories($ENV{GMOCK_HOME}/mybuild $ENV{GTEST_HOME}/mybuild)
```

Compile again:

```bash
cmake .
make
```

Output:

```bash
Scanning dependencies of target test
[ 33%] Building CXX object CMakeFiles/test.dir/main.cpp.o
[ 66%] Building CXX object CMakeFiles/test.dir/SoundexTest.cpp.o
[100%] Linking CXX executable test
/usr/bin/ld: 找不到 -lgmock
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/test.dir/build.make:99：test] 错误 1
make[1]: *** [CMakeFiles/Makefile2:73：CMakeFiles/test.dir/all] 错误 2
make: *** [Makefile:84：all] 错误 2
```

Still unsuccessful, then I can't find any solutions with google.