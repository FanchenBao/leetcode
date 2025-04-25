#include <iostream>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  int countCompleteSubarrays(vector<int> &nums) {
    /*
     * LeetCode 2799
     *
     * Create an auxiliary array len_consec such that len_consec[i] is the
     * length of the subarray that starts from nums[i] and contains the exact
     * same number.
     *
     * Using len_consec and two pointers method, we can traverse nums once to
     * find the answer.
     *
     * O(N^2), 42 ms, 26.24%
     */
    int N = nums.size();
    std::vector<int> len_consec(N, 1);
    std::unordered_set<int> uniques;
    uniques.insert(nums[N - 1]);
    for (int i = N - 2; i >= 0; i--) {
      if (nums[i] == nums[i + 1])
        len_consec[i] = len_consec[i + 1] + 1;
      uniques.insert(nums[i]);
    }

    int res = 0, lo = 0, hi = 0;
    std::unordered_map<int, int> counter;
    while (lo < N) {
      while (hi < N && counter.size() != uniques.size()) {
        counter[nums[hi]]++;
        hi++;
      }
      std::unordered_map<int, int> cp(counter);
      int marker = hi - 1;
      int valid_repeat = std::min(len_consec[lo], hi - lo);
      while (marker < N && cp.size() == uniques.size()) {
        res += valid_repeat;
        if (++marker < N)
          cp[nums[marker]]++;
      }
      // move lo forward
      counter[nums[lo]] -= valid_repeat;
      if (counter[nums[lo]] == 0)
        counter.erase(nums[lo]);
      lo += valid_repeat;
      if (hi == N && counter.size() < uniques.size())
        break;
    }
    return res;
  }
};

class Solution2 {
public:
  int countCompleteSubarrays(vector<int> &nums) {
    /*
     * This is really embarrassing. The key insight is that once we find a
     * smallest subarray that is complete, we can always extend it to the end
     * of the array and all the subarrays in between are valid as well.
     *
     * O(N), 15 ms, 80.59%
     */
    std::unordered_set<int> uniques;
    for (int n : nums)
      uniques.insert(n);

    int res = 0, lo = 0;
    int N = nums.size();
    std::unordered_map<int, int> counter;
    for (int hi = 0; hi < N; hi++) {
      counter[nums[hi]]++;
      while (lo <= hi && counter.size() == uniques.size()) {
        res += N - hi;
        counter[nums[lo]]--;
        if (counter[nums[lo]] == 0)
          counter.erase(nums[lo]);
        lo++;
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> nums{5, 5, 5, 5};
  Solution sol;
  sol.countCompleteSubarrays(nums);
}
