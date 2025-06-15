#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimizeMax(vector<int> &nums, int p) {
    /*
     * Here is my new idea. We produce a counter of nums. For each element
     * that have even count, we can produce count / 2 number of pairs with
     * min difference. For each element that has odd count, we also can
     * produce count / 2 pairs, but we will have one left. Thus, after this
     * round of getting zeros in difference, we will be left with just single
     * values. Then we can go through them and pick the pair with the smallest
     * difference.
     *
     * O(NlogN)
     */
    std::map<int, int> counter;
    for (int n : nums)
      counter[n]++;
    for (const auto &pa : counter) {
      int zero_pairs = pa.second / 2;
      p -= zero_pairs;
      if (p <= 0)
        return 0;
      counter[pa.first] -= zero_pairs;
    }
    std::vector<std::pair<int, int>> diffs;
    int pre = -1;
    for (const auto &pa : counter) {
      if (pa.second == 0)
        continue;
      if (pre != -1) {
        diffs.push_back({pa.first - pre, pre});
      }
      pre = pa.first;
    }
    std::sort(diffs.begin(), diffs.end());
    int res = 0, pi = -1;
    for (int i = 0; i < diffs.size() && p > 0; i++) {
      if (pi >= 0 && diffs[pi].first + diffs[pi].second == diffs[i].second)
        // we have used diffs[i].second already
        continue;
      p--;
      res = diffs[i].first;
      pi = i;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
