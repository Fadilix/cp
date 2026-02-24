#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, w;
  cin >> n >> w;

  vector<vector<int>> arr(n);

  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;

    arr.push_back({a, b});
  }

  sort(arr.rbegin(), arr.rend());

  int result = 0;
  for (int i = 0; i < n; i++) {
    int d = arr[i][0];
    int g = arr[i][1];
    int take = min(g, w);
    result += take * d;
    w -= take;
  }

  cout << result << endl;

  return 0;
}
