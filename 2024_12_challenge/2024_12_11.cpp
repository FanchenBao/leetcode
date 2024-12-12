#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maximumBeauty(vector<int> &nums, int k) {
    /*
     * LeetCode 2779
     *
     * First sort nums and then sliding window to find the longest subarray
     * whose ranges of k share the same overlapping number.
     *
     * O(NlogN), 51 ms, faster than 60.73%
     */
    int N = nums.size();
    std::sort(nums.begin(), nums.end());
    int i = 0, res = 0;
    for (int j = 0; j < N; j++) {
      while (i < j && nums[i] + k < nums[j] - k)
        i++;
      res = std::max(res, j - i + 1);
    }
    return res;
  }
};

class Solution2 {
public:
  int maximumBeauty(vector<int> &nums, int k) {
    /*
     * This is the line sweep solution. For each number in nums, we have a
     * range. The question is to find the count of most overlapped ranges.
     * This can be solved by line sweep where we +1 on all the starts and -1
     * on all the ends. This way, we will be able to identify the most
     * overlapped part.
     *
     * O(N + max(nums)), 5 ms, faster than 99.09%
     */
    int max_num = 0;
    for (int n : nums)
      max_num = std::max(n, max_num);
    std::vector<int> linesweep(max_num + 1, 0);
    for (int n : nums) {
      linesweep[std::max(0, n - k)]++;
      linesweep[std::min(max_num, n + k + 1)]--;
    }
    int res = std::max(1, linesweep[0]);
    for (int i = 1; i < max_num; i++) {
      // produce the number of overlaps at each position
      linesweep[i] += linesweep[i - 1];
      res = std::max(res, linesweep[i]);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
