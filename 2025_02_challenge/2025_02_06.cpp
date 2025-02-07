#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int tupleSameProduct(vector<int> &nums) {
    /*
     * LeetCode 1726
     *
     * Find the frequency of all products from any two numbers in nums. Then
     * sum up f * (f - 1) * 4, which is the formula to find the total number
     * of ways to arrange a product that can be achieved by f pairs.
     *
     * O(N^2)
     */
    std::map<int, int> counter;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++)
        counter[nums[i] * nums[j]]++;
    }
    int res = 0;
    for (const auto &p : counter)
      res += p.second * (p.second - 1) * 4;
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
