#include <iostream>
using namespace std;

#define ll long long

ll get_total(ll m, ll k) {
  if (m <= k) {
    return m * (m + 1) / 2;
  }

  ll left = k * (k + 1) / 2;
  ll rows = m - k;
  ll rem = k - 1 - rows;
  ll right = ((k - 1) * k / 2) - (rem * (rem + 1) / 2);

  return left + right;
}

void solve() {
  ll k, x;
  cin >> k >> x;

  ll lo, hi;
  lo = 1;
  hi = 2 * k - 1;
  ll ans = hi;

  while (lo <= hi) {
    ll mid = (lo + hi) / 2;

    if (get_total(mid, k) >= x) {
      hi = mid - 1;
      ans = mid;
    } else {
      lo = mid + 1;
    }
  }
  cout << ans << "\n";
}

int main() {
  ll t;
  cin >> t;

  while (t--) {
    solve();
  }
  return 0;
}
