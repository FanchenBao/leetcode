#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maximumDifference(vector<int> &nums) {
    /*
     * LeetCode 2016
     *
     * Use monotonic array
     *
     * O(N)
     */
    std::vector<int> stack;
    int res = -1;
    for (int n : nums) {
      while (!stack.empty() && stack[stack.size() - 1] >= n)
        stack.pop_back();
      if (!stack.empty())
        res = std::max(res, n - stack[0]);
      stack.push_back(n);
    }
    return res;
  }
};

class Solution2 {
public:
  int maximumDifference(vector<int> &nums) {
    /*
     * Use prefix min from the editorial
     */
    int res = -1, premin = nums[0];
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] > premin)
        res = std::max(res, nums[i] - premin);
      else
        premin = nums[i];
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
