CXXFLAGS = -Wall -std=c++17 -Wextra -march=native
OUTFLAGS = -O3 -fopenmp
PROFFLAGS = -pg -O3
DBFLAGS = -g -Og
CXX ?= g++
IFLAGS = -I../include

default: union_find.out

%.out: %.cpp
	$(CXX) -o $@ $< $(IFLAGS) $(CXXFLAGS) $(OUTFLAGS)

%.prof: %.cpp
	$(CXX) -o $@ $< $(IFLAGS) $(CXXFLAGS) $(PROFFLAGS)

%.db: %.cpp
	$(CXX) -o $@ $< $(IFLAGS) $(CXXFLAGS) $(DBFLAGS)

%: %.out %.prof %.db

.PHONY: clean
clean:
	rm -f *.out *.prof *.db
