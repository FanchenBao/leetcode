#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool divideArray(vector<int> &nums) {
    /*
     * LeetCode 2206
     *
     * Count each number. If there exists a number whose frequency is odd,
     * return false.
     *
     * O(N), 1 ms, 69.22%
     */
    std::vector<int> counter(501, 0);
    for (int n : nums)
      counter[n]++;
    for (int c : counter) {
      if (c % 2 == 1)
        return false;
    }
    return true;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
