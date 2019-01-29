#include <bits/stdc++.h>

using namespace std;

int main() {
	int len, sum;

	cin >> len;

	string prev = "0";
	sum = 0;

	string in;
	cin >> in;

	for (int i = 0; i < len; i++) {
		char current = in[i];

		if (current == '-') {
			prev = prev.substr(0, prev.size() - 1);
		}
		else {
			prev = prev + current;
		}

		sum += atoi(prev.c_str());
	}

	cout << sum << endl;

	return 0;
}
