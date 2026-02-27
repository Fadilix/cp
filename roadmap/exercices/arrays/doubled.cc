#include <iostream>
#include <string>

using namespace std;

int main() {
  int n;

  cin >> n;

  int count = 0;

  for (int i = 2; i < n + 1; i++) {
    string x = to_string(i);
    if (x.size() % 2 != 0)
      continue;

    int mid = x.size() / 2;
    string first = x.substr(0, mid);
    string second = x.substr(mid, x.size());

    if (first == second)
      count++;
  }

  cout << count << endl;

  return 0;
}
