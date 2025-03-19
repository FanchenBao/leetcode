#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int longestNiceSubarray(vector<int> &nums) {
    /*
     * LeetCode 2401
     *
     * Use bit manipulation and binary search
     *
     * For example, given nums = [1, 3, 8, 48, 10], their binary representations
     * are
     * nums[0] = 1  => 000001
     * nums[1] = 3  => 000011
     * nums[2] = 8  => 001000
     * nums[3] = 48 => 110000
     * nums[4] =  10 => 001010
     *
     * The set_bits matrix would be
     * [
     *  [1, 3],
     *  [1, 4],
     *  [],
     *  [2, 4],
     *  [],
     *  [],
     * ]
     *
     * O(NlogN), 1033 ms, 5.04%
     */
    std::vector<std::vector<int>> set_bits(32, std::vector<int>());
    for (int i = 0; i < nums.size(); i++) {
      int n = nums[i];
      int j = 0;
      while (n > 0) {
        if (n & 1)
          set_bits[j].push_back(i);
        n >>= 1;
        j++;
      }
    }
    int res = 0;
    for (int i = 0; i < nums.size(); i++) {
      int cur = nums.size();
      for (int j = 0; j < 32; j++) {
        int mask = (1 << j);
        int k = std::upper_bound(set_bits[j].begin(), set_bits[j].end(), i) -
                set_bits[j].begin();
        int length;
        if (nums[i] & mask) {
          length =
              k < set_bits[j].size() ? set_bits[j][k] - i : nums.size() - i;
        } else {
          length = k + 1 < set_bits[j].size() ? set_bits[j][k + 1] - i
                                              : nums.size() - i;
        }
        cur = std::min(cur, length);
      }
      res = std::max(res, cur);
    }
    return res;
  }
};

int main() {
  std::vector<int> nums{904163577, 321202512, 470948612, 490925389, 550193477,
                        87742556,  151890632, 655280661, 4,         263168,
                        32,        573703555, 886743681, 937599702, 120293650,
                        725712231, 257119393};
  Solution sol;
  std::cout << sol.longestNiceSubarray(nums) << std::endl;
}
