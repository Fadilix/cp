#include <iostream>
#include <vector>
using namespace std;

int main() {

  int n;
  cin >> n;

  vector<int> arr(n + 1);

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  int count = 0;

  for (int i = 1; i < n + 1; i++) {
    for (int j = i; j < n + 1; j++) {
      if (1 <= i && i < j && j <= n && arr[i - 1] != arr[j - 1]) {
        count++;
      }
    }
  }

  cout << count << endl;
  return 0;
}
