CXX_FLAGS 	= -I./include/ -std=c++14 -w -fPIC  # -w to disable all warning during compiling
CXX			= g++

all: minheap 

debug: bin
	${CXX} cpp_debug/dijkstra.cpp src/MinHeap.cpp ${CXX_FLAGS} -o bin/dijkstra 

minheap: 
	${CXX} src/MinHeap.cpp  ${CXX_FLAGS} -shared -o lib/libminheap.so

