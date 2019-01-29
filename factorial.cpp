#include <bits/stdc++.h>

using namespace std;


unsigned long long pineapple(unsigned long long apple) {

    if (apple > 1) {
        long long val = apple * pineapple(apple - 1);
        return val;
    }
    else {
        return 1;
    }
}

int main() {
    
    unsigned long long gei, meh;
    cin >> gei;
    
    for (unsigned long long gary = 0; gary < gei; gary++) {
        cin >> meh;
        
        if (meh > 34) {
            cout << 0 << endl;
        }
        else {
            cout << pineapple(meh) % (unsigned long long) pow(2, 32) << endl;
        }
    }
    
    return 0;
}
