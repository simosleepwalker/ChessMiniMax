cmake_minimum_required(VERSION 3.15)
project(Progetto)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(pieces)

add_executable(Progetto
        pieces/Piece.cpp
        pieces/Piece.h
        pieces/Pieces.cpp
        pieces/Pieces.h
        Chess.cpp
        Chess.h
        main.cpp)
