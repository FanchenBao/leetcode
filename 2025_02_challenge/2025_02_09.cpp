#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  long long countBadPairs(vector<int> &nums) {
    /*
     * LeetCode 2364
     *
     * All numbers that can form good pairs must have the same nums[i] - i.
     *
     * O(N), 64 ms , 75.68%
     */
    std::unordered_map<int, int> counter;
    long long N = (long long)nums.size();
    for (int i = 0; i < N; i++)
      counter[nums[i] - i]++;
    long long res = N * (N - 1) / 2;
    for (auto const &p : counter) {
      long long n = (long long)p.second;
      res -= (long long)(n * (n - 1) / 2);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
