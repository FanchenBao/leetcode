#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int candy(vector<int> &ratings) {
    /*
     * LeetCode 135
     *
     * Go left to right, each drop in rating we assign 1 candy to the child.
     * Each increase in rating, we add one to the candy relative to the amount
     * to its left.
     *
     * Then we go right to left, following a similar scheme, except that at
     * each child, we will take the max between what has already been assigned
     * and what should be assigned in the current run.
     *
     * O(N), 6ms, 11.45%
     */
    int N = ratings.size();
    std::vector<int> candies(N, 1);
    // left to right
    for (int i = 1; i < N; i++) {
      if (ratings[i] > ratings[i - 1])
        candies[i] = candies[i - 1] + 1;
    }
    // right to left
    for (int i = N - 2; i >= 0; i--) {
      if (ratings[i] > ratings[i + 1])
        candies[i] = std::max(candies[i], candies[i + 1] + 1);
    }
    int res = 0;
    for (int c : candies)
      res += c;
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
