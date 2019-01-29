#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int main() {
  int numCases, width, height;
  bool broken;

  cin >> numCases;

  for (int c = 0; c < numCases; c++) {
    cin >> width >> height;

    string grid[width][height] = {};

    vector<int[2]> solved;
    queue<int[3]> q = {};
    q.push({0, 0, 1});

    broken = false;

    for (int x = 0; x < width; x++) {
      for (int y = 0; y < height; y++) {
          cin >> grid[x][y];
      }
    }

    while(!q.empty) {
      int val[3] = q.pop();
      int x, y, c = val[0], val[1], val[2];

      solved = insert(solved, {x, y});

      string char = grid[x][y];

    }

    if (!broken) {
        cout << -1 << endl;
    }
  }
}
