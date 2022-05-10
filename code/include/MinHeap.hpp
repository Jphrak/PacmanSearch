#pragma once
using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>

struct Node {
    int key;
    int vertex;
    Node(int key, int vertex);
};

class MinHeap {
    private:
        std::vector<Node> heap;

    public:
        MinHeap();
        ~MinHeap();
        void push(int key, int vertex);
        Node top();
        void pop();
        void print();
};

extern "C" {
    void* createMinHeap();
    void push(void *tree, int vertex, int distance);
    void pop(void *tree);
    int getMinDistance(void *tree);
    int getMinVertex(void *tree);
    void releaseMinHeap(void *tree);
};
