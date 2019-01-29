#include <bits/stdc++.h>

using namespace std;

int main() {
    int numBlocks;
    cin >> numBlocks;
    int blocks[numBlocks] = {};

    for (int i = 0; i < numBlocks; i++) {
        cin >> blocks[i];
    }

    sort(blocks, blocks + sizeof(blocks)/sizeof(blocks[0]));

    int maxWidth = 0;
    int maxCount = 0;

    for (int a = 0; a < numBlocks; a++) {
        for (int b = 0; b < a; b++) {
	    if (blocks[a] + blocks[b] > maxWidth) {
	        maxWidth = blocks[a] + blocks[b];
		maxCount = 1;
	    }
	    else if (blocks[a] + blocks[a] == maxWidth) {
		maxCount++;
	    }
	}
    }

    cout << maxWidth << " " << maxCount << endl;
}
