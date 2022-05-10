#include <vector>
#include <queue>
#include <iostream>
#include <string> 
#include <sstream>
#include <MinHeap.hpp>

using namespace std;

const int inf = 100000000;
const string input_string = "7 13 \
A B 1 \
A C 3 \
B C 1 \
B G 2 \
B E 5 \
B D 7 \
C D 9 \
C E 3 \
D E 2 \
D G 12 \
D F 1 \
E F 2 \
F A 10";

int main() {
    int n, m;
    istringstream input(input_string);
    cin.rdbuf(input.rdbuf());
    cin >> n >> m;

    vector< vector< pair<int, int> > > adj(n, vector< pair <int, int> >());
    for (int i = 0; i < m; ++i) {
        char u, v;
        int w;
        cin >> u >> v >> w;
        adj[(int)(u - 'A')].push_back(pair<int, int>((int)(v - 'A'), w));
        adj[(int)(v - 'A')].push_back(pair<int, int>((int)(u - 'A'), w));
    }

    vector<int> d(n, 0);
    vector<int> mask(n, 0);
    for (int i = 0; i < n; ++i) {
        d[i] = inf;
        mask[i] = 0;
    }
    d[0] = 0;

    int count = 0;
    MinHeap heap;
    heap.push(d[0], 0);

    while (true) {
        Node top = heap.top(); 
        int u = top.vertex;
        int dist = top.key;
        heap.pop();
        
        if (dist != d[u])
            continue;

        mask[u] = 1;
        count += 1;
        if (count == n)
            break;

        for (int i = 0; i < adj[u].size(); ++i) {
            int v = adj[u][i].first;
            if (mask[v] == 1)
                continue;
            int w = adj[u][i].second;
            if (dist + w < d[v]) {
                d[v] = dist + w;
                heap.push(d[v], v);
            }
        }
    }

    for (int i = 0; i < n; ++i)
        std::cout << "Distance From A to " << (char)(i + 'A') << ": " << d[i] << endl;
}
