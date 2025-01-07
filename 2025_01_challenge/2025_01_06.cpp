#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> minOperations(string boxes) {
    /*
     * LeetCode 1769
     *
     * We find all the indices of '1' in boxes.
     *
     * Then we go from index 0 to boxes.size() - 1, at each index i, we find
     * the sum of the absolute difference between i and each index of '1'.
     *
     * To speed up the computation, we can find the number of '1' indices
     * smaller than i and the number bigger than i. Considering that we start
     * from position 0, the '1' indices smaller than i add to the total steps,
     * whereas the '1' indices larger than i remove from the total steps.
     *
     * O(N), 0 ms 100%
     */
    std::vector<int> balls;
    std::vector<int> res(boxes.size());
    for (int i = 0; i < boxes.size(); i++) {
      if (boxes[i] == '1') {
        balls.push_back(i);
        res[0] += i;
      }
    }
    int j = 0;
    for (int i = 1; i < res.size(); i++) {
      while (j < balls.size() && balls[j] < i)
        j++;
      res[i] = res[i - 1] + j - (balls.size() - j);
    }
    return res;
  }
};

class Solution2 {
public:
  vector<int> minOperations(string boxes) {
    /*
     * This is the official solution, which uses the same idea as solution1
     * BUT it's very smart.
     * We consider going through the boxes twice. In the left to right pass
     * we accumulate the number of moves needed for all the balls to the
     * left of the current index. We then do the same from right to left
     * and accumulate the moves for all the balls to the right of the
     * current index. Add them together, we will have the solution.
     *
     * The brilliant part of the official solution is that we can do these
     * two passes in one go.
     *
     * O(N), 0 ms, 100%
     */
    int N = boxes.size();
    std::vector<int> res(N);
    int balls_from_left = 0, balls_from_right = 0;
    int moves_from_left = 0, moves_from_right = 0;
    for (int i = 0; i < N; i++) {
      // left-to-right pass
      res[i] += moves_from_left;
      balls_from_left += boxes[i] - '0';
      moves_from_left += balls_from_left;
      // right-to-left pass
      res[N - i - 1] += moves_from_right;
      balls_from_right += boxes[N - i - 1] - '0';
      moves_from_right += balls_from_right;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
