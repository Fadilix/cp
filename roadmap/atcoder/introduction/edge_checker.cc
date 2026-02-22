#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  cout << ((abs(a - b) == 1 || abs(a - b) == 9) ? "Yes" : "No") << endl;
}

