#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumOperations(vector<int> &nums) {
    /*
     * LeetCode 3396
     *
     * Use a counter to keep track of the frequency of each number. As we
     * perform the operation, the frequency gets deducted. When frequency
     * becomes zero, we delete the key from the counter. The first time that the
     * size of the counter is equal to the current number size, that indicates
     * all numbers are unique.
     *
     * 7 ms, 32.42%
     */
    std::unordered_map<int, int> counter;
    for (int n : nums)
      counter[n]++;
    int total = nums.size();
    int res = 0, idx = 0;
    while (total > counter.size() && idx < nums.size()) {
      for (int i = idx; i < std::min(idx + 3, (int)nums.size()); i++) {
        counter[nums[i]]--;
        if (counter[nums[i]] == 0)
          counter.erase(nums[i]);
      }
      idx += 3;
      total -= 3;
      res++;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
