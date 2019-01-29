#include <bits/stdc++.h>

using namespace std;

int main() {
	int h, w;

	cin >> h >> w;

	bool grid[h][w];

	for (int y = 0; y < h; y ++) {
		for (int x = 0; x < w; x ++) {
			cin >> grid[h][w];
		}
	}

	cout << grid[0][0];
}
