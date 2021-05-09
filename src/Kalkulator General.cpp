#include <iostream>
#include <conio.h>
using namespace std;

int main() {
  float x,y;
  char ops, lagi;
  while (true) {
  // user input
  cout << "Kalkulator C++ \n" << "============== \n \n" << "Masukkan angka pertama: ";
  cin >> x;
  cout << "Masukkan operasi: ";
  cin >> ops;
  cout << "Masukkan angka kedua: ";
  cin >> y;

  switch(ops) {

    case '/':
    cout << x / y << endl;
    break;

    case '*':
    cout << x * y << endl;
    break;

    case '-':
    cout << x - y << endl;
    break;

    case '+':
    cout << x + y << endl;
    break;

    default:
    cout << "operasi yang anda masukkan salah!";
    break;
  }
    cout << "Lagi? (y/n) ";
    cin >> lagi;
    if (lagi == 'Y'){}
    else if (lagi == 'y'){}
    else {
        cout << "Terimakasih!";
            break;
    }

  }
   _getch();
  return 0;
}
