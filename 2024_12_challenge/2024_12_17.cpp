#include <functional>
#include <iostream>
#include <queue>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

class Solution1 {
public:
  string repeatLimitedString(string s, int repeatLimit) {
    /*
     * LeetCode 2182
     *
     * Sort s in descend and then two pointers. The right pointer points to
     * the next biggest char after the left pointer. Each time when a left
     * pointer encounters more repeats than allowed, we swap the left and
     * right.
     *
     * One trick is to add an indicator of end of string so that when the
     * right pointer exhausts the string, we can use the indicator to signify
     * the end of the processed string.
     *
     * O(NlogN), 59 ms, faster than 35.70%
     */
    std::vector<char> chars(s.begin(), s.end());
    std::sort(chars.begin(), chars.end(), std::greater<>());
    chars.push_back('*');
    int cnt = 1, i = 1, j = 1, N = s.size();
    while (i < N && j <= N) {
      if (i == j) {
        j++;
        // j points to the next biggest char after chars[i]
        while (j < N && chars[j] == chars[j - 1])
          j++;
      }
      if (chars[i] == chars[i - 1]) {
        cnt++;
        if (cnt > repeatLimit) {
          char tmp = chars[i];
          chars[i] = chars[j];
          chars[j] = tmp;
          j++;
          continue;
        }
        i++;
      } else {
        cnt = 1;
        i++;
      }
    }
    return std::string(chars.begin(),
                       std::find(chars.begin(), chars.end(), '*'));
  }
};

class Solution2 {
public:
  string repeatLimitedString(string s, int repeatLimit) {
    /*
     * This is the max heap solution inspired by the hint from the official
     * solution. However, I did not read the official one yet.
     *
     * 82 ms, faster than 12.66%
     */
    std::priority_queue<std::pair<int, int>> pq;
    std::vector<int> counter(26);
    for (char c : s)
      counter[c - 'a']++;
    for (int i = 0; i < 26; i++) {
      if (counter[i] > 0)
        pq.push({i, counter[i]});
    }
    std::stringstream res;
    int cnt = 0;
    char pre = ' ';
    while (!pq.empty()) {
      auto ele = pq.top();
      pq.pop();
      char le = ele.first + 'a';
      if (le == pre) {
        cnt++;
        if (cnt > repeatLimit) {
          if (pq.empty())
            break;
          auto next_ele = pq.top();
          pq.pop();
          char next_le = next_ele.first + 'a';
          cnt = 1;
          pre = next_le;
          res << next_le;
          if (next_ele.second - 1 > 0)
            pq.push({next_ele.first, next_ele.second - 1});
          pq.push(ele);
        } else {
          res << le;
          if (ele.second - 1 > 0)
            pq.push({ele.first, ele.second - 1});
        }
      } else {
        cnt = 1;
        pre = le;
        res << le;
        if (ele.second - 1 > 0)
          pq.push({ele.first, ele.second - 1});
      }
    }
    return res.str();
  }
};

class Solution3 {
public:
  string repeatLimitedString(string s, int repeatLimit) {
    /*
     * This is the max heap solution from the official solution. I don't know
     * why I didn't think of this myself in solution2. We don't have to include
     * the count in the max heap. We can keep them in a separate counter.
     */
    std::priority_queue<char> pq;
    std::vector<int> counter(26);
    for (char c : s)
      counter[c - 'a']++;
    for (int i = 0; i < 26; i++) {
      if (counter[i] > 0)
        pq.push(i + 'a');
    }
    std::stringstream res;
    int cnt = 0;
    char pre = ' ';
    while (!pq.empty()) {
      char cur = pq.top();
      pq.pop();
      if (cur == pre) {
        cnt++;
        if (cnt > repeatLimit) {
          if (pq.empty())
            break;
          char nex = pq.top();
          pq.pop();
          cnt = 1;
          pre = nex;
          res << nex;
          if (counter[nex - 'a'] - 1 > 0) {
            pq.push(nex);
            counter[nex - 'a']--;
          }
          pq.push(cur);
        } else {
          res << cur;
          if (counter[cur - 'a'] - 1 > 0) {
            pq.push(cur);
            counter[cur - 'a']--;
          }
        }
      } else {
        cnt = 1;
        pre = cur;
        res << cur;
        if (counter[cur - 'a'] - 1 > 0) {
          pq.push(cur);
          counter[cur - 'a']--;
        }
      }
    }
    return res.str();
  }
};

int main() {
  std::string s("cczazcc");
  int repeatLimit = 3;
  Solution sol;
  std::cout << sol.repeatLimitedString(s, repeatLimit) << std::endl;
}
