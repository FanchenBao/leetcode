#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countPairs(vector<int> &nums, int k) {
    /*
     * LeetCode 2176
     *
     * Find all the indices for each number, and then check the number of pairs
     * within each group of indices that satisfy the requirement.
     *
     * O(N^2), 8ms, 3.85%
     */
    std::map<int, std::vector<int>> indices;
    for (int i = 0; i < nums.size(); i++)
      indices[nums[i]].push_back(i);
    int res = 0;
    for (const auto &pair : indices) {
      for (int j = 0; j < pair.second.size(); j++) {
        for (int p = j + 1; p < pair.second.size(); p++)
          res += ((pair.second[j] * pair.second[p]) % k) == 0;
      }
    }
    return res;
  }
};

class Solution2 {
public:
  int countPairs(vector<int> &nums, int k) {
    /*
     * Brute force
     */
    int res = 0;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] == nums[j] && (i * j) % k == 0)
          res++;
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
