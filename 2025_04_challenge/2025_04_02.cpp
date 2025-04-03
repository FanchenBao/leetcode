#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long maximumTripletValue(vector<int> &nums) {
    /*
     * LeetCode 2873
     *
     * Use suffix max and then brute force.
     *
     * O(N^2), 0 ms.
     */
    int N = nums.size();
    std::vector<int> sufmax(N);
    sufmax[N - 1] = nums[N - 1];
    for (int i = N - 2; i >= 0; i--) {
      sufmax[i] = std::max(nums[i], sufmax[i + 1]);
    }
    long long res = 0;
    for (int i = 0; i <= N - 3; i++) {
      for (int j = i + 1; j <= N - 2; j++) {
        res = std::max(res, (long long)(nums[i] - nums[j]) *
                                (long long)sufmax[j + 1]);
      }
    }
    return res;
  }
};

class Solution2 {
public:
  long long maximumTripletValue(vector<int> &nums) {
    /*
     * Use prefix and suffix max.
     *
     * O(N)
     */
    int N = nums.size();
    std::vector<int> sufmax(N);
    std::vector<int> prefmax(N);
    prefmax[0] = nums[0];
    sufmax[N - 1] = nums[N - 1];
    for (int i = 1; i < N; i++)
      prefmax[i] = std::max(nums[i], prefmax[i - 1]);
    for (int i = N - 2; i >= 0; i--)
      sufmax[i] = std::max(nums[i], sufmax[i + 1]);
    long long res = 0;
    for (int i = 1; i <= N - 2; i++) {
      // iterate through the mid value
      res = std::max(res, (long long)(prefmax[i - 1] - nums[i]) *
                              (long long)sufmax[i + 1]);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
