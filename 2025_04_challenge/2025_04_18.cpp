#include <iostream>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

class Solution {
public:
  string countAndSay(int n) {
    /*
     * LeetCode 38
     *
     * Basic recursion.
     *
     * 2 ms, 89.33%
     */
    if (n == 1)
      return "1";
    std::string next = countAndSay(n - 1);
    std::stringstream ss;
    int cnt = 1;
    for (int i = 1; i < next.size(); i++) {
      if (next[i] == next[i - 1]) {
        cnt++;
      } else {
        ss << cnt << next[i - 1];
        cnt = 1;
      }
    }
    ss << cnt << next[next.size() - 1];
    return ss.str();
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
