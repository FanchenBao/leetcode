#include <iostream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  string robotWithString(string s) {
    /*
     * The idea originates from the editorial. Essentially, we keep track of
     * the smallest letter in the remaining s, and compare the top of t to
     * that smallest letter. If the top of t is smaller or equal to the
     * smallest letter in the remaining s, we use it. Otherwise, we keep
     * pushing new letter to the stack.
     *
     * The ingenious part is that instead of using a priority queue to keep
     * track of the smallest letter, we use a counter, because we always know
     * what letter is the smallest. We start from 'a'. Once a letter's count
     * decreases to zero, we move on to the next letter with a positive count.
     *
     * O(N), 51 ms, 54.41%
     */
    std::vector<int> counter(26);
    for (char c : s)
      counter[c - 'a']++;
    int ci = 0;
    std::stack<char> st;
    std::string res;
    for (char c : s) {
      st.push(c);
      counter[c - 'a']--;
      while (ci < 26 && counter[ci] == 0)
        ci++;
      while (!st.empty() && st.top() - 'a' <= ci) {
        res.push_back(st.top());
        st.pop();
      }
    }
    while (!st.empty()) {
      res.push_back(st.top());
      st.pop();
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
