#include <iostream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  string clearDigits(string s) {
    /*
     * LeetCode 3174
     *
     * Use stack
     *
     * O(N), 0 ms, 100%
     */
    std::vector<char> st;
    for (char c : s) {
      if (std::isdigit(c)) {
        if (!st.empty())
          st.pop_back();
      } else {
        st.push_back(c);
      }
    }
    std::string res(st.begin(), st.end());
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
