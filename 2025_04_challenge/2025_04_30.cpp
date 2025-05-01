#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int findNumbers(vector<int> &nums) {
    /*
     * LeetCode 1295
     */
    int res = 0;
    for (int n : nums)
      res += std::to_string(n).size() % 2 == 0;
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
