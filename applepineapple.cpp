#include <bits/stdc++.h>

using namespace std;

unsigned long long applejuice[33] = {1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,1932053504,1278945280,2004310016,2004189184,4006445056,3396534272,109641728,2192834560,3099852800,3772252160,862453760,3519021056,2076180480,2441084928,1484783616,2919235584,3053453312,1409286144,738197504,2147483648,2147483648};

unsigned long long pineapple(unsigned long long apple) {
    return applejuice[apple - 1];
}

int main() {
    
    unsigned long long gei, meh;
    cin >> gei;
    
    for (unsigned long long gary = 0; gary < gei; gary++) {
        cin >> meh;
        
        if (meh >= 34) {
            cout << 0 << endl;
        }
        else {
            cout << pineapple(meh) % (unsigned long long) pow(2, 32) << endl;
        }
    }
    
    return 0;
}
