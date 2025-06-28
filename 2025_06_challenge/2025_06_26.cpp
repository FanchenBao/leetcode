#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string longestSubsequenceRepeatedK(string s, int k) {
    /*
    This is a copy and paste, but I understand what the solution
    does. In fact, I left a comment under the editorial, questioning
    the time complexity of the total number of permutations.

    The solution essentially brute force the problem. It finds
    the letters that appear at least k times in s. Then it produces
    all possible permutations of strings of all possible lengths,
    allowing repetition of each character. Then it checks whether the
    produced string can serve as a subsequence that occurs at least
    k times in s.

    The generation of permutation is straightforards. Each time a previous
    permutation is good, we use that as the base to produce the next
    round by appending each candidate to the end.

    The check whether a string appears at least k times in s as
    subsequence is done in a greedy way. We scan s from left to right
    and always try to match the string as early as possible. Once we
    have k matches, that means the string is good.

    The time complexity, in my book, should be O(n * m^m), where
    m = n // k, which in this problem does not exceed 7.
    */
    vector<int> freq(26);
    for (char ch : s) {
      freq[ch - 'a']++;
    }
    vector<char> candidate;
    for (int i = 25; i >= 0; i--) {
      if (freq[i] >= k) {
        candidate.push_back('a' + i);
      }
    }
    queue<string> q;
    for (char ch : candidate) {
      q.push(string(1, ch));
    }

    string ans = "";
    while (!q.empty()) {
      string curr = q.front();
      q.pop();
      if (curr.size() > ans.size()) {
        ans = curr;
      }
      // generate the next candidate string
      for (char ch : candidate) {
        string next = curr + ch;
        if (isKRepeatedSubsequence(s, next, k)) {
          q.push(next);
        }
      }
    }

    return ans;
  }

  bool isKRepeatedSubsequence(const string &s, const string &t, int k) {
    int pos = 0, matched = 0;
    int n = s.size(), m = t.size();
    for (char ch : s) {
      if (ch == t[pos]) {
        pos++;
        if (pos == m) {
          pos = 0;
          matched++;
          if (matched == k) {
            return true;
          }
        }
      }
    }

    return false;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
