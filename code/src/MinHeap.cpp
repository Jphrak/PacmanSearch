#include <MinHeap.hpp>


Node::Node(int key, int vertex) {

    this->key = key;
    this->vertex = vertex;
}

MinHeap::MinHeap() {
    this->heap.clear();
}

MinHeap::~MinHeap() {
    this->heap.clear();
}

void MinHeap::push(int key, int vertex) {
    /* 
     * Insert key and vertex into the binary heap
     */
    
    // YOUR CODE HERE 
    heap.push_back(Node(key, vertex));
    int index = heap.size() - 1;
    while (index > 0) {
        int parent = (index + 1)/2 - 1;
        if (heap[index].key < heap[parent].key) {
            std::swap(heap[index], heap[parent]);
            index = parent;
        } 
        else
            break;
    }
}

void MinHeap::pop() {
    /*
     * Remove the top node in the heap
     */

    // YOUR CODE HERE 
    int N = heap.size();
    heap[0] = heap[N - 1];
    N = N - 1;
    heap.pop_back();
    int index = 0;
    while (2*index+1 < N)
    {
        int child = 2 * index + 1;
        if (heap[child+1].key < heap[child].key)
        {
            child = child + 1;
        }
        if (heap[child].key < heap[index].key)
        {
            std::swap(heap[child], heap[index]);
            index = child;
        }
        else{
            break;
        }
    }
}

Node MinHeap::top() {
    /*
     * Return the top node of the heap (we assume that this function is only called when the heap is not empty)
     */

    // YOUR CODE HERE
    return this->heap[0];
}

void MinHeap::print()
{
    cout << "Printing MinHeap left to right, top to bottom (height)" << endl;
    int size = heap.size() - 1;
    for (int i = 0; i < size; i++)
    {
        cout << heap[i].key << " ";
    }
    cout << endl;
}

/*
 * This code below is used to communicate with Python
 * You do not need to modify these codes
 */

void* createMinHeap() {
    return new(std::nothrow) MinHeap();
}

void push(void* tree, int vertex, int distance) {
    MinHeap* tree_ = reinterpret_cast<MinHeap*>(tree);
    tree_->push(distance, vertex);

}

void pop(void* tree) {
    MinHeap* tree_ = reinterpret_cast<MinHeap*>(tree);
    tree_->pop();
}

int getMinDistance(void* tree) {
    MinHeap* tree_ = reinterpret_cast<MinHeap*>(tree);
    return tree_->top().key;
}

int getMinVertex(void* tree) {
    MinHeap* tree_ = reinterpret_cast<MinHeap*>(tree);
    return tree_->top().vertex; 
}

void releaseMinHeap(void* tree) {
   delete tree;
}

