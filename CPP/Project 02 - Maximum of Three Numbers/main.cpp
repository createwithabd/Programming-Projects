#include <iostream>

using namespace std;

int32_t main() {
    int a, b, c;
    cout << "Enter first number between 1 - 100" << endl;
    cin >> a;
    cout << "Enter first number between 1 - 100" << endl;
    cin >> b;
    cout << "Enter first number between 1 - 100" << endl;
    cin >> c;

    if (a>b){
        if (a>c){
            cout << a << " is the maximum number of all three entered numbers." << endl;
        } else {
            cout << c << " is the maximum number of all three entered numbers." << endl;
        }     
    } else {
        if (b>c){
            cout << b << " is the maximum number of all three entered numbers." << endl;
        } else {
            cout << c << " is the maximum number of all three entered numbers." << endl;
        }
    }
    return 0; 

}