#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  void sortColors(vector<int> &nums) {
    /*
     * LeetCode 75
     *
     * Counts the frequency of 0, 1, and 2, and put them back in the nums in
     * sorted order.
     *
     * O(N)
     */
    int zero = 0, one = 0, two = 0;
    for (int n : nums) {
      zero += n == 0;
      one += n == 1;
      two += n == 2;
    }
    int i = 0;
    while (zero) {
      nums[i++] = 0;
      zero--;
    }
    while (one) {
      nums[i++] = 1;
      one--;
    }
    while (two) {
      nums[i++] = 2;
      two--;
    }
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
