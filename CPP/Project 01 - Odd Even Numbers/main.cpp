#include <iostream>

using namespace std;

int32_t main() {
    int a;
    cout<<"Please ENTER any number between 1 - 100:" << endl;
    cin >> a;
    if (a%2==0) {
        cout << a << " is an even number." << endl;
    } else {
        cout << a << " is an odd number." << endl;
    }

    return 0; 

}