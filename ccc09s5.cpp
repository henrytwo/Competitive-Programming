#include <bits/stdc++.h>

using namespace std;

int main() {
	int numX, numY, numS, x, y, r, b, topValue, topCount;

	topValue = 0;
	topCount = 0;

	cin >> numY >> numX >> numS;

	int grid[numX][numY] = {};

	for (int i = 0; i < numS; i++) {
		cin >> x >> y >> r >> b;

		x -= 1;
		y -= 1;

		for (int j = max(-1 * r, -1 * x); j <= min(numX - 1 - x, r * 2); j++) {
			int sx = min(max(j + x, 0), numX - 1);

			double rise =  pow((pow(r, 2) - pow(j, 2)), 0.5);
			int riseInt = int (rise);

		        int sy1 = riseInt + y;
                        int sy2 = y - riseInt;

			if ((0 <= sy1 && sy1 < numY) || (0 <= sy2 && sy2 < numY)) {
				sy1 = min(sy1, numY - 1);
				sy2 = max(sy2 - 1, -1);

				grid[sx][sy1] += b;

				if (sy2 >= 0) {
					grid[sx][sy2] += -1 * b;
				}
			}
		}
	}

	for (int a = 0; a < numX; a++) {
		for (int b = numY - 2; b != -1; b--) {

			grid[a][b] += grid[a][b + 1];

			if (grid[a][b] > topValue) {
				topValue = grid[a][b];
				topCount = 1;
			}
			else if(grid[a][b] == topValue) {
				topCount ++;
			}
		}

                if (grid[a][numY - 1] > topValue) {
                        topValue = grid[a][numY - 1];
                        topCount = 1;
                }
                else if(grid[a][numY - 1] == topValue) {
                        topCount ++;
                }
	}
	/*
	for (int z = 0; z < numX; z++) {
		for (int y = 0; y < numY; y++) {
			cout << grid[z][y] << " ";
		}
		cout << endl;
	}
	*/
	cout << topValue << endl;
	cout << topCount << endl;

	return 0;
}
