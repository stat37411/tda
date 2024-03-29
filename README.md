# tda
Algorithms for Topological Data Analysis

This repository will contain algorithms we cover in this class.  

## Environment Setup

For the sake of dependency management, you can create a conda environment if you're using Anaconda Python.
```
conda create -n tda Python=3
```

To use with a jupyter notebook, you should
```
conda install ipykernel
```

## Running C++ code

First, make sure you have `gcc` installed (including `g++`) in order to compile C++.

Headers are in the `include/` folder.  The folder `demo/` contains `.cpp` files, which can be compiled
using the `Makefile`.  Open a terminal
```
$ cd demo
$ make # compiles union_find.out
$ ./union_find.out # runs the executable
```
