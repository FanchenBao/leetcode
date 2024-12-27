#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solution {
private:
  int compute(int mask, std::vector<int> &nums) {
    int sum = 0;
    int N = nums.size();
    for (int i = 0; i < N; i++) {
      if ((mask & (1 << (N - i - 1))) == 0)
        sum += nums[i];
      else
        sum -= nums[i];
    }
    return sum;
  }

public:
  int findTargetSumWays(vector<int> &nums, int target) {
    /*
     * LeetCode 494
     *
     * Brute force, but use bit manipulation to iterate through all possible
     * operator combinations.
     *
     * O(2^N * N) TLE
     */
    int N = nums.size();
    int res = 0;
    int total_pos = 1 << N;
    for (int i = 0; i < total_pos; i++) {
      int sum = compute(i, nums);
      if (sum == target)
        res++;
    }
    return res;
  }
};

class Solution2 {
private:
  int compute(int mask, std::vector<int> &nums, int lo, int hi) {
    int sum = 0;
    for (int i = lo; i <= hi; i++) {
      if ((mask & (1 << (hi - lo - i))) == 0)
        sum += nums[i];
      else
        sum -= nums[i];
    }
    return sum;
  }

public:
  int findTargetSumWays(vector<int> &nums, int target) {
    /*
     * LeetCode 494
     *
     * Do the brute force for half of nums, then match the other half for
     * target.
     *
     * O(2^N * N)
     */
    int N = nums.size();
    int left_size = N / 2, right_size = N - left_size;
    int res = 0;
    int left_pos = 1 << left_size, right_pos = 1 << right_size;
    std::map<int, int> left_counter;
    for (int i = 0; i < left_pos; i++) {
      int sum = compute(i, nums, 0, left_size - 1);
      left_counter[sum]++;
    }
    for (int i = 0; i < right_pos; i++) {
      int tmp = target - compute(i, nums, left_size, N - 1);
      res += left_counter[tmp];
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
