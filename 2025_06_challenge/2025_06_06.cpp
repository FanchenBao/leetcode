#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  string robotWithString(string s) {
    /*
     * LeetCode 2434
     *
     * The idea is that we put all the letters in s in a min heap that first
     * compares the letter size, and if the letters are the same, compare the
     * indices. We put the smallest index with the smallest letter at the top.
     * Then we compare that smallest letter with the top of string t. If the
     * top of the min heap is smaller, we keep pushing new letters into t
     * until the min is encountered in the min heap. Otherwise, we pop t.
     *
     * O(NlogN). 529 ms, 9.9%
     */
    auto cmp = [&](int a, int b) {
      if (s[a] == s[b]) // same letter, choose smaller index
        return a > b;
      return s[a] > s[b]; // different letter, choose smaller letter
    };

    std::priority_queue<int, std::vector<int>, decltype(cmp)> min_heap(cmp);
    std::stack<int> stack;
    std::string res;
    int top_idx_in_res = -1;
    for (int i = 0; i < s.size(); i++)
      min_heap.push(i);
    while (!min_heap.empty()) {
      if (stack.empty()) {
        stack.push(top_idx_in_res + 1);
        continue;
      }
      if (min_heap.top() <= stack.top()) {
        min_heap.pop();
        continue;
      }
      if (s[stack.top()] <= s[min_heap.top()]) {
        res.push_back(s[stack.top()]);
        top_idx_in_res = std::max(top_idx_in_res, stack.top());
        stack.pop();
      } else if (stack.top() + 1 == min_heap.top()) {
        res.push_back(s[min_heap.top()]);
        top_idx_in_res = std::max(top_idx_in_res, min_heap.top());
        min_heap.pop();
      } else if (std::max(stack.top(), top_idx_in_res) + 1 < s.size()) {
        stack.push(std::max(stack.top(), top_idx_in_res) + 1);
      }
    }
    while (!stack.empty()) {
      res.push_back(s[stack.top()]);
      stack.pop();
    }
    return res;
  }
};

int main() {
  std::string s = "zazazaaa";
  Solution sol;
  std::cout << sol.robotWithString(s) << std::endl;
}
