#include <iostream>

using namespace std;

int main() {
	int numGate, numPlane, numFill, num, cap;
	cin >> numGate >> numPlane;
	int gates[numGate] = {};
	bool gud;

	numFill = 0;
	cap = numGate - 1;

	for (int p = 0; p < numPlane; p++) {
		cin >> num;

		gud = false;

		for (int g = min(num - 1, cap); g > -1; g--) {
			if (gates[g] == 0) {
				numFill++;
				gates[g] = num;
				gud = true;
				
				if (g == cap -1) {
					cap = g;
				}

				break;
			}
		}

		if (!gud) {
			break;
		}
	}

	cout << numFill << endl;
}
