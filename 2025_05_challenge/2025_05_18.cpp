#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int get_max_state(int N) {
    // find the max trinary number with N digits.
    int max = 0;
    for (int i = 0; i < N; i++)
      max += 2 * (int)pow(3, i);
    return max;
  }

  bool is_eligible(int color, int N) {
    int pre = -1;
    while (N) {
      int cur = color % 3;
      if (cur == pre)
        return false;
      pre = cur;
      color /= 3;
      N--;
    }
    return true;
  }

  std::vector<int> find_eligible_rows(int N, int max_state) {
    // use trinary number to represent each coloring. Select the ones that are
    // eligible.
    std::vector<int> res;
    for (int i = 0; i <= max_state; i++) {
      if (is_eligible(i, N))
        res.push_back(i);
    }
    return res;
  }

  bool can_be_adjacent(int r1, int r2, int N) {
    // decide whether the two rows r1 and r2 can be adjacent.
    // Since each row itself is eligible, they can be adjacent if vertically
    // the colors are different.
    while (N) {
      int c1 = r1 % 3, c2 = r2 % 3;
      if (c1 == c2)
        return false;
      r1 /= 3;
      r2 /= 3;
      N--;
    }
    return true;
  }

  int colorTheGrid(int m, int n) {
    /*
     * LeetCode 1931 (Hint)
     *
     * Choose n = min(m, n), m = max(m, n).
     *
     * We can easily find all eligible coloring for 1 x n. Since the max min
     * of m and n is 5, the max eligible coloring count is 48.
     *
     * For each coloring, we can also find all possible next row. We can
     * create this mapping.
     *
     * An important insight is that each new row only depends on the previous
     * row. Thus, once we solve 2 x n, we have essentially solved m x n.
     * For each new row, from the mapping we know how many other rows can
     * lead to the current new row. We keep a DP mapping to track the number
     * of ways to yield each row. Then the number of ways to yield the
     * current row is the sum of all the number of ways to yield the rows
     * that are eligible to be the previous row.
     *
     * To simplify the mapping, we can use trinary number to represent each
     * row.
     *
     * O(2^(2N) * M), where N = min(m, n), and M = max(m, n).
     * 27 ms, 86.78%
     */
    int MOD = 1e9 + 7;
    int M = std::max(m, n), N = std::min(m, n);
    int MAX_STATE = get_max_state(N);
    // step 1: find all the eligible rows
    std::vector<int> rows = find_eligible_rows(N, MAX_STATE);
    if (M == 1)
      return rows.size();
    // step 2: find the mapping from one eligible row to the another
    std::vector<std::vector<int>> row_map(MAX_STATE + 1);
    for (int i = 0; i < rows.size(); i++) {
      for (int j = i + 1; j < rows.size(); j++) {
        if (can_be_adjacent(rows[i], rows[j], N)) {
          row_map[rows[i]].push_back(rows[j]);
          row_map[rows[j]].push_back(rows[i]);
        }
      }
    }
    // step 3: Get the counter to keep track of the number of ways to yield
    // each eligible row as the last row in the grid.
    std::vector<int> counter(MAX_STATE + 1);
    for (int r : rows)
      counter[r]++;
    // Dynamic programming
    for (int i = 1; i < M; i++) {
      std::vector<int> tmp(MAX_STATE + 1);
      for (int row : rows) {
        for (int pre_row : row_map[row]) {
          tmp[row] = ((long long)tmp[row] + counter[pre_row]) % MOD;
        }
      }
      counter = std::move(tmp);
    }
    int res = 0;
    for (int v : counter)
      res = ((long long)res + v) % MOD;
    return res;
  }
};

int main() {
  int m = 5, n = 4;
  Solution sol;
  std::cout << sol.colorTheGrid(m, n) << std::endl;
}
