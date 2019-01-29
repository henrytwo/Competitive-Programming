#include <iostream>
#include <string>

using namespace std;

int main() {
    
    string in;
    int w, h, numRooms;
    cin >> w >> h;
    pair<int, int> start;
    
    numRooms = 0;
    
    int grid[1000][1000] = {0};
    
    for (int y = 0; y < h; y++) {
        cin >> in;
        
        for (int x = 0; x < w; x++) {
            if (in[x] != '0' && in[x] != '#') {
                numRooms += 1;
            }    
        
            if (in[x] == 'i') {
                start = pair(y, x)
            }
        }
    }
    
    
    return 0;
}
