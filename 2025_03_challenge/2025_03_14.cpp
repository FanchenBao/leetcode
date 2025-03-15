#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maximumCandies(vector<int> &candies, long long k) {
    /*
     * LeetCode 2226
     *
     * Use binary search
     * O(NlogN), 19 ms 84.93%
     */
    int lo = 0, hi = 0;
    long long s = 0;
    for (int c : candies) {
      s += (long long)c;
      hi = std::max(hi, c);
    }
    if (s < k)
      return 0;
    if (s == k)
      return 1;
    // binary search
    hi++;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      s = 0;
      for (int c : candies)
        s += c / mid;
      if (s < k)
        hi = mid;
      else
        lo = mid + 1;
    }
    return lo - 1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
