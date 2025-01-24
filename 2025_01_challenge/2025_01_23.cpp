#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countServers(vector<vector<int>> &grid) {
    /*
     * LeetCode 1267
     *
     * First do row by row. Count the number of computers. If the count is
     * larger than one, we add the count to the result. Also, we mark the
     * counter computers as 2 on the grid.
     *
     * Then do col by col. Count the number of computers and the number of
     * unmarked computers. If the total number of computers is larger than 1,
     * we add the count of unmarked to the result.
     *
     * O(MN), 43 ms, 7.35%
     */
    int M = grid.size(), N = grid[0].size();
    int res = 0;
    for (int i = 0; i < M; i++) {
      int cnt = 0, r = -1, c = -1;
      for (int j = 0; j < N; j++) {
        if (grid[i][j] == 1) {
          r = i, c = j;
          cnt++;
          grid[i][j] = 2;
        }
      }
      if (cnt == 1)
        grid[r][c] = 1;
      else
        res += cnt;
    }
    for (int j = 0; j < N; j++) {
      int cnt1 = 0, cnt2 = 0;
      for (int i = 0; i < M; i++) {
        if (grid[i][j] >= 1) {
          if (grid[i][j] == 1)
            cnt1++;
          cnt2++;
        }
      }
      if (cnt2 > 1)
        res += cnt1;
    }
    return res;
  }
};

class Solution2 {
public:
  int countServers(vector<vector<int>> &grid) {
    /*
     * This solution is from the official solution.
     * Use auxillary space to keep track of the count of computers for each
     * column and rows. Then go through the grid again to check whether a cell
     * belongs to row and column that both have more than one machines.
     *
     * O(MN), 4 ms, 44.09%
     */
    int M = grid.size(), N = grid[0].size();
    std::vector<int> cnt_cols(N, 0);
    std::vector<int> cnt_rows(N, 0);
    int res = 0;
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (grid[i][j] == 1) {
          cnt_rows[i]++;
          cnt_cols[j]++;
        }
      }
    }
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (grid[i][j] == 1)
          res += cnt_rows[i] > 1 || cnt_cols[j] > 1;
      }
    }
    return res;
  }
};

class Solution3 {
public:
  int countServers(vector<vector<int>> &grid) {
    /*
     * This is also from the official solution. It is a bit convoluted but
     * it does reduce the number of operations.
     *
     * Observe that if there are more than 1 computers in a row, we can
     * easily count all of them, and none of them should be counted again
     * when we go for cols.
     *
     * The computer that we should add when we do cols and after we have
     * processed the rows is a single computer in a row that is part of a
     * multi-computer col. Thus, we need to keep count of the number of
     * computers in each col and at the same time mark where the last
     * computer is on a row. If the row has only one computer yet the last
     * computer on the row happens on a col of multiple computers, it should
     * counted.
     *
     * O(MN + M), 0 ms, 100%
     */
    int M = grid.size(), N = grid[0].size();
    std::vector<int> cnt_cols(N, 0);
    std::vector<int> last_comp_row(
        M, -1); // for each row, what is the pos of the last computer
    int res = 0;
    for (int i = 0; i < M; i++) {
      int cnt_row = 0;
      for (int j = 0; j < N; j++) {
        if (grid[i][j] == 1) {
          cnt_row++;
          cnt_cols[j]++;
          last_comp_row[i] = j;
        }
      }
      if (cnt_row > 1) {
        res += cnt_row;
        last_comp_row[i] = -1; // all the computers have been considered already
      }
    }
    for (int i = 0; i < M; i++) {
      if (last_comp_row[i] >= 0) {
        // this row has only one computer, we will count it if its col has more
        // than one computer
        res += cnt_cols[last_comp_row[i]] > 1;
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
