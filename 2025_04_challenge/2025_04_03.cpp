#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long maximumTripletValue(vector<int> &nums) {
    /*
     * LeetCode 2874
     *
     * This is exactly the same as problem 2873, except that the constraint
     * is stronger with much longer nums.
     *
     * We will use the prefx and suffix max.
     * O(N), 6 ms, 47%
     */
    int N = nums.size();
    std::vector<int> sufmax(N, 0);
    sufmax[N - 1] = nums[N - 1];
    for (int i = N - 2; i >= 0; i--)
      sufmax[i] = std::max(sufmax[i + 1], nums[i]);
    int premax = nums[0];
    long long res = 0;
    for (int i = 1; i <= N - 2; i++) {
      res = std::max(res,
                     (long long)(premax - nums[i]) * (long long)sufmax[i + 1]);
      premax = std::max(premax, nums[i]);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
