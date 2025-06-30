#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int pow(long long b, long long p, long long m) {
    long long res = 1;
    while (p > 0) {
      if (p % 2 == 1) {
        res = (res * b) % m;
      }
      b = (b * b) % m;
      p /= 2;
    }
    return res;
  }

  int numSubseq(vector<int> &nums, int target) {
    /*
     * LeetCode 1498
     *
     * Sort nums. Then go from left to right, for each element, find the largest
     * element such that their sum is not larger than target. Count the number
     * of elements in between. Then the number of subsequences that satisfy
     * the requirement and also start with the element is 2^N, where N is the
     * number of elements in between.
     *
     * O(N), 31 ms, 62,49%
     */
    long long res = 0;
    int MOD = 1000000007;
    std::sort(nums.begin(), nums.end());
    int j = nums.size() - 1;
    for (int i = 0; i < nums.size() && j >= i; i++) {
      while (j >= i && nums[i] + nums[j] > target)
        j--;
      if (j >= i && nums[i] + nums[j] <= target)
        res = (res + pow(2, j - i, MOD)) % MOD;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
