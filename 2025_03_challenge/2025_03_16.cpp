#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long repairCars(vector<int> &ranks, int cars) {
    /*
     * LeetCode 2594
     *
     * Binary search again.
     * O(NlogN), 16 ms, 90.77%
     */
    long long lo = 1, hi = 1e14 + 1;
    while (lo < hi) {
      long long mid = lo + (hi - lo) / 2;
      long long cnt = 0;
      for (int r : ranks) {
        cnt += (int)std::sqrt((double)mid / r);
        if (cnt >= cars)
          break;
      }
      if (cnt >= cars)
        hi = mid;
      else
        lo = mid + 1;
    }
    return lo;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
