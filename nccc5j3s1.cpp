#include <bits/stdc++.h>
using namespace std;

int numCact, median, good;

int rec(vector<int> left, vector<int> done) {
	if (done.size() == 3 || done.size() == numCact) {
		int m;

		if (done.size() == 1) {
			m = done[0]
		}
		else if {
			m = sum(done) / 2;
		}
		else {
			m = 
		}


	}
	else {
		for (int i = 0; i < left.size(); i++) {
			vector<int> l = left;
			vector<int> d = done;

			d.push_back(left[i]);
			l.erase(i);



		}
	}
}

int main() {
	cin >> numCact >> median;

	vector<int> a;
	vector<int> b;

	for (int i = 0; i < numCact; i++) {
		a.push_back(i);
	}

	rec(a, b);

	cout << good << endl;
}
