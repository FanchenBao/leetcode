#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  void helper(vector<int> &counter, int index, int cur_num, vector<int> &res) {
    if (index == 3) {
      res.push_back(cur_num);
      return;
    }
    for (int d = 0; d < 10; d++) {
      if (counter[d] > 0) {
        if (index == 0 && d == 0) {
          continue;
        } else if (index == 2 && d % 2 == 1) {
          continue;
        } else {
          counter[d]--;
          helper(counter, index + 1, cur_num * 10 + d, res);
          counter[d]++;
        }
      }
    }
    return;
  }

public:
  vector<int> findEvenNumbers(vector<int> &digits) {
    /*
     * LeetCode 2094
     *
     * Naive solution of backtracking without caching previously computed
     * states. To make this solution more efficient, we need to cache the
     * results computed from each counter state, but I am too lazy to create
     * a hash function to do so.
     *
     */
    std::vector<int> counter(10);
    for (int d : digits)
      counter[d]++;
    std::vector<int> res;
    helper(counter, 0, 0, res);
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
