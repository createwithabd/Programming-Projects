#include <iostream>

using namespace std;

int32_t main() {
    bool GameOn = true;
    int num;
    cout << "Welcome to Fizz Buzz Game. " << endl;
    while (GameOn){
        cout << "Enter an whole number: \n";
        cin >> num;
        if (num%3 ==0 and num%5==0){
            cout << "Fizz Buzz" << endl;
        } else if (num%3==0){
            cout << "Fizz" << endl;
        } else if (num%5 ==0) {
            cout << "Buzz" << endl;
        } else {
            cout <<"You Lose! Game Over" << endl;
            GameOn = false; // can use break here as well.
        }
    }


    return 0; 

}