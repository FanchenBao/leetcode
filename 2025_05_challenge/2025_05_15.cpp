#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> getLongestSubsequence(vector<string> &words,
                                       vector<int> &groups) {
    /*
     * LeetCode 2900
     *
     * Always take the first element in groups, and then build the alternating
     * array. A bit greedy here.
     *
     * O(N)
     */
    std::vector<string> res;
    res.push_back(words[0]);
    int pre = 0;
    for (int i = 1; i < groups.size(); i++) {
      if (groups[i] != groups[pre]) {
        res.emplace_back(words[i]);
        pre = i;
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
