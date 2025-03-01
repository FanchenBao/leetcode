#include <deque>
#include <iostream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  string shortestCommonSupersequence(string str1, string str2) {
    /*
     * LeetCode 1092
     *
     * First use longest common subsequence algorithm to find the indices of
     * the LCS for str1 and str2.
     *
     * Then we take all the letters to the left of each LCS index in str1 and
     * str2 and concatenate them togerher.
     *
     * O(N^2), 39 ms, 6%
     */
    int M = str1.size(), N = str2.size();
    std::vector<std::vector<int>> lcs_len(M + 1, std::vector<int>(N + 1, -1));
    std::vector<std::vector<int>> lcs_pos(M + 1, std::vector<int>(N + 1, -1));
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        if (str1[i - 1] == str2[j - 1]) {
          lcs_pos[i][j] = 2; // diagonal
          lcs_len[i][j] = lcs_len[i - 1][j - 1] + 1;
        } else if (lcs_len[i - 1][j] >= lcs_len[i][j - 1]) {
          lcs_pos[i][j] = 1; // go up
          lcs_len[i][j] = lcs_len[i - 1][j];
        } else {
          lcs_pos[i][j] = 0; // go left
          lcs_len[i][j] = lcs_len[i][j - 1];
        }
      }
    }
    std::stack<int> lcs1;
    std::stack<int> lcs2;
    lcs1.push(M);
    lcs2.push(N);
    int i = M, j = N;
    while (i > 0 && j > 0) {
      if (lcs_pos[i][j] == 2) { // diagonal
        lcs1.push((i--) -
                  1); // don't forget the lcs matrix has one-bigger indices
        lcs2.push((j--) - 1);
      } else if (lcs_pos[i][j] == 1) { // go up
        i--;
      } else { // go left
        j--;
      }
    }
    std::string res = "";
    int pre1 = 0, pre2 = 0;
    while (!lcs1.empty()) {
      // put every letter to the left of the top of lcs1 onto the result str
      for (int i = pre1; i < lcs1.top(); i++)
        res += str1[i];
      for (int j = pre2; j < lcs2.top(); j++)
        res += str2[j];
      if (lcs1.top() < M)
        res += str1[lcs1.top()];
      pre1 = lcs1.top() + 1;
      pre2 = lcs2.top() + 1;
      lcs1.pop();
      lcs2.pop();
    }
    return res;
  }
};

class Solution2 {
public:
  string shortestCommonSupersequence(string str1, string str2) {
    /*
     * Same as solution1, but instead of recording directions in lcs_pos, we
     * directly build the LCS as we go through the LCS algorithm
     *
     * Unfortunately, this solution yields memory limit exceeded.
     */
    int M = str1.size(), N = str2.size();
    std::vector<std::vector<std::string>> lcs(
        M + 1, std::vector<std::string>(N + 1, ""));
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        if (str1[i - 1] == str2[j - 1]) {
          lcs[i][j] = str1[i - 1] + lcs[i - 1][j - 1];
        } else if (lcs[i - 1][j].size() >= lcs[i][j - 1].size()) {
          lcs[i][j] = lcs[i - 1][j];
        } else {
          lcs[i][j] = lcs[i][j - 1];
        }
      }
    }
    // note that this LCS is reversed, and we add a sentinel. The
    // sentinel can help simplify the creation of the supersequence.
    std::string lcs_str = "*" + lcs[M][N];
    std::string res = "";
    int i = 0, j = 0;
    for (int k = lcs_str.size() - 1; k >= 0; k--) {
      while (i < M && str1[i] != lcs_str[k])
        res += str1[i++];
      i++;
      while (j < N && str2[j] != lcs_str[k])
        res += str2[j++];
      j++;
      if (k > 0) // do not include the sentinel itself.
        res += lcs_str[k];
    }
    return res;
  }
};

class Solution3 {
public:
  string shortestCommonSupersequence(string str1, string str2) {
    /*
     * Let's not create stack of lcs1 and lcs2. Instead, we rebuild the LCS
     * string. This will take advantage of the good part from both the first
     * and the second solution.
     *
     * 41 ms, 5.13%
     */
    int M = str1.size(), N = str2.size();
    std::vector<std::vector<int>> lcs_len(M + 1, std::vector<int>(N + 1, -1));
    std::vector<std::vector<int>> lcs_pos(M + 1, std::vector<int>(N + 1, -1));
    for (int i = 1; i < M + 1; i++) {
      for (int j = 1; j < N + 1; j++) {
        if (str1[i - 1] == str2[j - 1]) {
          lcs_pos[i][j] = 2; // diagonal
          lcs_len[i][j] = lcs_len[i - 1][j - 1] + 1;
        } else if (lcs_len[i - 1][j] >= lcs_len[i][j - 1]) {
          lcs_pos[i][j] = 1; // go up
          lcs_len[i][j] = lcs_len[i - 1][j];
        } else {
          lcs_pos[i][j] = 0; // go left
          lcs_len[i][j] = lcs_len[i][j - 1];
        }
      }
    }
    std::string lcs_str = "*"; // with a sentinel
    int i = M, j = N;
    while (i > 0 && j > 0) {
      if (lcs_pos[i][j] == 2) { // diagonal
        lcs_str += str1[i - 1];
        i--;
        j--;
      } else if (lcs_pos[i][j] == 1) { // go up
        i--;
      } else { // go left
        j--;
      }
    }
    std::string res = "";
    i = 0;
    j = 0;
    for (int k = lcs_str.size() - 1; k >= 0; k--) {
      while (i < M && str1[i] != lcs_str[k])
        res += str1[i++];
      i++;
      while (j < N && str2[j] != lcs_str[k])
        res += str2[j++];
      j++;
      if (k > 0) // do not include the sentinel itself.
        res += lcs_str[k];
    }
    return res;
  }
};

int main() {
  std::string str1 = "bbbaaaba";
  std::string str2 = "bbababbb";
  Solution sol;
  std::cout << sol.shortestCommonSupersequence(str1, str2) << std::endl;
}
