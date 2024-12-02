#include <iostream>
#include <set>
#include <vector>

class Solution {
public:
  bool checkIfExist(std::vector<int> &arr) {
    /*
     * LeetCode 1346
     *
     * First C++ in I don't even remember how many years. It will be a very
     * slow journey to pick up the speed on not only the syntax but the
     * general way to doing things in c++.
     *
     * O(N), 0 ms, faster than 100.00%
     */
    std::set<int> seen{};

    for (int v : arr) {
      if (seen.contains(v * 2) || (v % 2 == 0 && seen.contains(v / 2)))
        return true;
      seen.insert(v);
    }
    return false;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
