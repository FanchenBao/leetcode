#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, int k) {
    /*
     * LeetCode 2962
     *
     * Two pointers. O(N), 0 ms
     */
    int max_num = 0;
    for (int n : nums)
      max_num = std::max(n, max_num);
    long long res = 0;
    int lo = 0, N = nums.size(), cnt = 0;
    for (int hi = 0; hi < N; hi++) {
      cnt += nums[hi] == max_num;
      while (lo <= hi && cnt == k) {
        res += (long long)(N - hi);
        cnt -= nums[lo++] == max_num;
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
