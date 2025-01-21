#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int firstCompleteIndex(vector<int> &arr, vector<vector<int>> &mat) {
    /*
     * LeetCode 2661
     *
     * First we record the matrix positions of each value in arr. Then we use
     * two counters to keep track of the number of cells that have been painted
     * on each row and col.
     *
     * As we go through the values in arr, we use the position matrix to find
     * the i, j, and update the count of painted cells in the ith row and jth
     * col. Once one of them shows that the entire row or col has been fully
     * painted, we have found the answer.
     *
     * O(MN), 104 ms, 47.26%
     */
    int M = mat.size(), N = mat[0].size();
    std::vector<std::vector<int>> positions(M * N + 1, std::vector<int>(2));
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        positions[mat[i][j]][0] = i;
        positions[mat[i][j]][1] = j;
      }
    }
    std::vector<int> cell_count_row(M);
    std::vector<int> cell_count_col(N);
    for (int k = 0; k < arr.size(); k++) {
      int i = positions[arr[k]][0], j = positions[arr[k]][1];
      cell_count_row[i]++;
      cell_count_col[j]++;
      if (cell_count_row[i] == N || cell_count_col[j] == M)
        return k;
    }
    return -1; // should never reach here
  }
};

class Solution2 {
public:
  int firstCompleteIndex(vector<int> &arr, vector<vector<int>> &mat) {
    /*
     * LeetCode 2661
     *
     * First we record the matrix positions of each value in arr. Then we use
     * two counters to keep track of the number of cells that have been painted
     * on each row and col.
     *
     * As we go through the values in arr, we use the position matrix to find
     * the i, j, and update the count of painted cells in the ith row and jth
     * col. Once one of them shows that the entire row or col has been fully
     * painted, we have found the answer.
     *
     * O(MN). Use std::pair<int, int> to significantly improve run time.
     * The run time dropped from 104 ms to 3 ms, 97.87%
     */
    int M = mat.size(), N = mat[0].size();
    std::vector<std::pair<int, int>> positions(M * N + 1);
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        positions[mat[i][j]] = {i, j};
      }
    }
    std::vector<int> cell_count_row(M);
    std::vector<int> cell_count_col(N);
    for (int k = 0; k < arr.size(); k++) {
      auto [i, j] = positions[arr[k]];
      cell_count_row[i]++;
      cell_count_col[j]++;
      if (cell_count_row[i] == N || cell_count_col[j] == M)
        return k;
    }
    return -1; // should never reach here
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
