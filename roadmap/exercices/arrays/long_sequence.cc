#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int main() {
  int n, x;

  cin >> n;

  vector<int> arr(n);

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  cin >> x;

  int sum_one_arr = accumulate(arr.begin(), arr.end(), 0);

  int repeats = x / sum_one_arr;
  int count = repeats * n;
  int sum = repeats * sum_one_arr;

  for (int i = 0; i < arr.size(); i++) {
    if (sum > x) {
      break;
    }

    sum += arr[i];
    count++;
  }

  cout << count << endl;

  return 0;
}
