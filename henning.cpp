#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second

int N, dists[110]; // Da actual distances
vector<pair<int, int>> G[110]; // Graph
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> Q; // Search Queue

int main(){
    cin.sync_with_stdio(0); cin.tie(0); // Fast loading stuff

    for(int i = 0; i < 110; i++) dists[i] = -1; // Reset all sheits to -1
    cin >> N; // Gets number of nodes
    for(int i = 0; i < N; i++){ // Input stuff
        for(int q = 0; q < N; q++){ 
            int V1; // Actual value
            cin >> V1;
            if(V1 != 0){ 
                G[i].push_back({V1,q}); // Adds to queue
            }
        }
    }

    Q.push({0,0}); // Starts searching
    while(!Q.empty()){
        pair<int, int> k = Q.top(); // Pops first thing out of queue
        Q.pop();

        if(dists[k.s] == -1){ 
            dists[k.s] = k.f;
            for(int i = 0; i < G[k.s].size(); i++){
                if(dists[G[k.s][i].s] == -1){
                    Q.push({k.f + G[k.s][i].f, G[k.s][i].s});
                }
            }
        }
    }
    cout << dists[N-1];
}
