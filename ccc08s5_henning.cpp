#include <bits/stdc++.h>
using namespace std;

int mem[31][31][31][31];

int rec(int a,int b,int c,int d){
    if(a < 0 || b < 0 || c < 0 || d < 0) return 1;
    if(mem[a][b][c][d] != -1) return mem[a][b][c][d];
    return mem[a][b][c][d] = !(rec(a-2,b-1,c,d-2) && rec(a-1,b-1,c-1,d-1) && rec(a,b,c-2,d-1) && rec(a,b-3,c,d) && rec(a-1,b,c,d-1));
}

int N;

int main(){
    memset(mem, -1, sizeof mem);
    freopen("input.txt","r",stdin);
    cin >> N;
    int V1,V2,V3,V4;
    for(int i = 0; i < N; i++){
        cin >> V1 >> V2 >> V3 >> V4;
        if(rec(V1,V2,V3,V4) == 1) cout << "Patrick" << endl;
        else cout << "Roland" << endl;
    }
}
