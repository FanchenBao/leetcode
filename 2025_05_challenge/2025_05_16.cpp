#include <climits>
#include <cstddef>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;
using Graph = std::unordered_map<int, std::vector<int>>;

class Solution {
public:
  bool hamming_is_1(const std::string &w1, const std::string &w2) {
    if (w1.size() != w2.size())
      return false;
    int res = 0;
    for (int i = 0; i < w1.size(); i++) {
      res += w1[i] != w2[i];
      if (res > 1)
        return false;
    }
    return res == 1;
  }

  std::vector<int> dfs(int idx, const Graph &graph,
                       std::vector<std::vector<int>> &dp) {
    if (!dp[idx].empty())
      return dp[idx];
    if (!graph.contains(idx)) {
      dp[idx] = std::vector<int>{idx};
      return dp[idx];
    }
    std::vector<int> res;
    for (int child : graph.at(idx)) {
      std::vector<int> tmp = dfs(child, graph, dp);
      if (tmp.size() > res.size())
        res = std::move(tmp);
    }
    res.insert(res.begin(), idx);
    dp[idx] = std::move(res);
    return dp[idx];
  }

  std::vector<int> helper(const std::vector<int> &indices,
                          const std::vector<string> &words,
                          const std::vector<int> &groups) {
    Graph graph;
    for (int i = 0; i < indices.size(); i++) {
      int ii = indices[i];
      for (int j = i + 1; j < indices.size(); j++) {
        int jj = indices[j];
        if (hamming_is_1(words[ii], words[jj]) && groups[ii] != groups[jj])
          graph[ii].push_back(jj);
      }
    }
    std::vector<std::vector<int>> dp(words.size());
    std::vector<int> res;
    for (int idx : indices) {
      std::vector<int> tmp = dfs(idx, graph, dp);
      if (tmp.size() > res.size())
        res = std::move(tmp);
    }
    return res;
  }

  vector<string> getWordsInLongestSubsequence(vector<string> &words,
                                              vector<int> &groups) {
    /*
     * LeetCode 2901
     *
     * The words in the longest subsequence must be of the same length. This
     * is the first filtering we can do.
     *
     * Among the words of the same length, we build a directed graph, where
     * an edge from words[i] to words[j] is valid if and only if the two words
     * have hamming distance of 1 and they are from different groups.
     *
     * Finally, we do DFS to find the longest path in the graph.
     *
     * Update: make hamming computation faster by early exist.
     * O(N^2 * M), where M is the average length of each word, 92 ms, 37.50%
     */
    std::unordered_map<int, std::vector<int>> sizes;
    for (int i = 0; i < words.size(); i++)
      sizes[words[i].size()].push_back(i);
    std::vector<int> res_indices;
    for (const auto &[_, indices] : sizes) {
      std::vector<int> tmp = helper(indices, words, groups);
      if (tmp.size() > res_indices.size())
        res_indices = std::move(tmp);
    }
    std::vector<string> res;
    for (int idx : res_indices)
      res.emplace_back(words[idx]);
    return res;
  }
};

class Solution2 {
public:
  bool hamming_is_1(const std::string &w1, const std::string &w2) {
    if (w1.size() != w2.size())
      return false;
    int res = 0;
    for (int i = 0; i < w1.size(); i++) {
      res += w1[i] != w2[i];
      if (res > 1)
        return false;
    }
    return res == 1;
  }

  vector<string> getWordsInLongestSubsequence(vector<string> &words,
                                              vector<int> &groups) {
    /*
     * Following the editorial, the same DP solution as Solution1 but with
     * much better performance.
     *
     * 32 ms, 94.53%
     */
    int N = words.size();
    std::vector<int> dp(N); // dp[i] is the size of the longest subsequence.
    std::vector<int> nex(N, -1); // nex[i] is the next index words[i] leads to.
    int res_idx = 0;
    for (int i = N - 1; i >= 0; i--) {
      dp[i] = 1;
      for (int j = i + 1; j < N; j++) {
        if (hamming_is_1(words[i], words[j]) && groups[i] != groups[j] &&
            dp[i] < dp[j] + 1) {
          dp[i] = dp[j] + 1;
          nex[i] = j;
        }
      }
      if (dp[i] > dp[res_idx])
        res_idx = i;
    }
    std::vector<std::string> res;
    while (res_idx >= 0) {
      res.emplace_back(words[res_idx]);
      res_idx = nex[res_idx];
    }
    return res;
  }
};

int main() {
  std::vector<std::string> words{"bab", "dab", "cab"};
  std::vector<int> groups{1, 2, 2};
  Solution sol;
  sol.getWordsInLongestSubsequence(words, groups);
};
