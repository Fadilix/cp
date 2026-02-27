#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> arr(n);
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  int count = 0;

  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] > 10) {
      count += arr[i] - 10;
    }
  }

  cout << count << endl;

  return 0;
}
