#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  void setZeroes(vector<vector<int>> &matrix) {
    /*
     * LeetCode 73
     *
     * This solution does not use constant space, but O(M + N) space.
     *
     * Go through the matrix to record which rows and cols have at least one
     * zero. Those rows and cols will later be filled by zeroes.
     *
     * O(MN) time and O(M + N) space.
     */
    int M = matrix.size(), N = matrix[0].size();
    std::vector<bool> rows(M), cols(N);
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (matrix[i][j] == 0) {
          rows[i] = rows[i] || true;
          cols[j] = cols[j] || true;
        }
      }
    }
    for (int i = 0; i < M; i++) {
      if (rows[i]) {
        for (int j = 0; j < N; j++)
          matrix[i][j] = 0;
      }
    }
    for (int j = 0; j < N; j++) {
      if (cols[j]) {
        for (int i = 0; i < M; i++)
          matrix[i][j] = 0;
      }
    }
  }
};

class Solution2 {
public:
  void setZeroes(vector<vector<int>> &matrix) {
    /*
     * This is the O(1) extra space solution inspired by the hints.
     *
     * We will use the row and col of the first zero as the storage space
     * for all the other rows and cols that should be turned into zeros.
     *
     * O(MN) time but O(1) space.
     */
    int M = matrix.size(), N = matrix[0].size();
    int ri = -1, ci = -1;
    for (int i = 0; i < M && ri < 0; i++) {
      for (int j = 0; j < N && ci < 0; j++) {
        if (matrix[i][j] == 0) {
          ri = i;
          ci = j;
        }
      }
    }
    // prep row at ri and col at ci for recording
    for (int j = 0; j < N; j++) {
      if (matrix[ri][j] == 0)
        matrix[ri][j] = 1;
      else
        matrix[ri][j] = 0;
    }
    for (int i = 0; i < M; i++) {
      if (matrix[i][ci] == 0)
        matrix[i][ci] = 1;
      else
        matrix[i][ci] = 0;
    }
    // go through the entire matrix
    for (int i = 0; i < M; i++) {
      if (i == ri)
        continue;
      for (int j = 0; j < N; j++) {
        if (j == ci)
          continue;
        if (matrix[i][j] == 0) {
          matrix[i][ci] = 1;
          matrix[ri][j] = 1;
        }
      }
    }
    // fill in the zeros
    for (int i = 0; i < M; i++) {
      if (matrix[i][ci] == 1) {
        for (int j = 0; j < N; j++)
          matrix[i][j] = 0;
      }
    }
    for (int j = 0; j < N; j++) {
      if (matrix[ri][j] == 1) {
        for (int i = 0; i < M; i++)
          matrix[i][j] = 0;
      }
    }
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
