#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution1 {
public:
  vector<bool> isArraySpecial(vector<int> &nums, vector<vector<int>> &queries) {
    /*
     * LeetCode 3152
     *
     * Get all the bad patches, which are defined as subarrays of nums whose
     * adjacent pairwise parities are identical. The goal is to see if a
     * query range overlap at least two numbers in any bad patch. If such
     * overlap exists, the query should be false.
     *
     * We sort querys by start, and then use two pointers to go through the
     * bad patches and queries. We first eliminate all the bad pathes whose
     * end is smaller or equal to the current query's start, because these
     * bad patches are impossible to have more than two overlapping numbers.
     *
     * Then, for the first bad patch that has the potential to produce a
     * two-number overlap, we check it and report the result. Then we move on
     * to the next query.
     *
     * O(MlogM + N) where M is the number of queries, 132 ms, faster than 8.99%
     */
    int N = nums.size();
    int M = queries.size();
    for (int i = 0; i < M; i++)
      queries[i].push_back(i);
    std::sort(queries.begin(), queries.end());
    std::vector<std::vector<int>> bad_patches;
    int bad_st = 0;
    for (int i = 1; i < N; i++) {
      if (nums[i] % 2 != nums[i - 1] % 2) {
        if (i - bad_st > 1)
          bad_patches.push_back(std::vector<int>{bad_st, i - 1});
        bad_st = i;
      }
    }
    if (N - bad_st > 1)
      bad_patches.push_back(std::vector<int>{bad_st, N - 1});
    std::vector<bool> res(M);
    int j = 0;
    int bad_len = bad_patches.size();
    for (auto query : queries) {
      while (j < bad_len && bad_patches[j][1] <= query[0])
        j++;
      if (j == bad_len || std::min(bad_patches[j][1], query[1]) -
                                  std::max(bad_patches[j][0], query[0]) + 1 <=
                              1) // check overlap
        res[query[2]] = true;
      else
        res[query[2]] = false;
    }
    return res;
  }
};

class Solution2 {
public:
  vector<bool> isArraySpecial(vector<int> &nums, vector<vector<int>> &queries) {
    /*
     * This is the prefix sum solution from the official solution.
     *
     * The idea is to produce a prefix sum of the number of violative numbers
     * in nums[:i + 1]. Then for each query, we check the number of violative
     * numbers from query[0] to query[1]
     * O(M + N), 6 ms, faster than 75.00%
     */
    int N = nums.size();
    int M = queries.size();
    std::vector<int> psum(N, 0);
    for (int i = 1; i < N; i++) {
      if (nums[i] % 2 == nums[i - 1] % 2)
        psum[i] = psum[i - 1] + 1;
      else
        psum[i] = psum[i - 1];
    }
    std::vector<bool> res(M, false);
    for (int i = 0; i < M; i++) {
      int st = queries[i][0];
      int ed = queries[i][1];
      res[i] = psum[ed] - psum[st] ==
               0; // we don't care about the first number, only the remaining
                  // numbers shall not contain any violative number
    }
    return res;
  }
};

int main() {
  std::vector<int> nums{3, 4, 1, 2, 6};
  std::vector<std::vector<int>> queries{{0, 4}};
  Solution2 sol;
  sol.isArraySpecial(nums, queries);
}
