#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> pivotArray(vector<int> &nums, int pivot) {
    /*
     * LeetCode 2161
     *
     * Three auxilary vectors to hold the numbers smaller than, equal to, and
     * larger than pivot, respectively.
     *
     * O(N), 4ms, 80%
     */
    std::vector<int> smalls;
    std::vector<int> larges;
    std::vector<int> equals;
    for (int n : nums) {
      if (n < pivot)
        smalls.push_back(n);
      else if (n > pivot)
        larges.push_back(n);
      else
        equals.push_back(n);
    }
    std::vector<int> res;
    res.insert(res.end(), smalls.begin(), smalls.end());
    res.insert(res.end(), equals.begin(), equals.end());
    res.insert(res.end(), larges.begin(), larges.end());
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
