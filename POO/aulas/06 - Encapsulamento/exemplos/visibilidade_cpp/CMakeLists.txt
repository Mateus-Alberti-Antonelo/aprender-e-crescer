cmake_minimum_required(VERSION 3.23)
project(visibilidade_cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_executable(visibilidade_cpp
        main.cpp
        src/contabancaria.cpp)
