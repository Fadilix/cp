#include <algorithm>
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

  vector<int> checked(n);

  for (int i = 0; i < n; i++) {
    checked[i] = i + 1;
  }

  sort(arr.begin(), arr.end());

  cout << (checked == arr ? "Yes" : "No");

  return 0;
}
