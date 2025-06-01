#include <deque>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int snakesAndLadders(vector<vector<int>> &board) {
    /*
     * LeetCode 909 (Fail)
     *
     * The solution is basically BFS, but I was not able to come up with it
     * last night (I blamed the sleepiness!) Using a smart trick, we can avoid
     * the complication of no-double-jumping by making sure that each node we
     * visit must take a step. A step can be size 1 to 6, as if we have six
     * children for the current node.
     */
    // turn the 2-D board into 1-D to make BFS easier
    std::vector<int> flatboard{0};
    int N = board.size(), di = 1, j = 0;
    for (int i = N - 1; i >= 0; i--) {
      while (j >= 0 && j < N) {
        flatboard.push_back(board[i][j]);
        j += di;
      }
      di *= (-1);
      j += di;
    }
    std::vector<bool> visited(N * N + 1, false);
    std::deque<int> queue;
    visited[1] = true;
    queue.push_back(1);
    int steps = 0;
    while (!queue.empty()) {
      int queue_size = queue.size();
      while (queue_size > 0) {
        int cur = queue.front();
        queue.pop_front();
        if (cur == N * N)
          return steps;
        for (int ds = 1; ds <= 6 && cur + ds <= N * N; ds++) {
          int next = cur + ds;
          if (flatboard[next] != -1)
            next = flatboard[next];
          if (!visited[next]) {
            queue.push_back(next);
            visited[next] = true;
          }
        }
        queue_size--;
      }
      steps++;
    }
    return -1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
