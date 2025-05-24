#include <climits>
#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  long long dp(int node, int should_xor, int k, const std::vector<int> &nums,
               std::vector<std::vector<long long>> &memo) {
    if (node == nums.size())
      return should_xor == 1
                 ? LONG_MIN
                 : 0; // the choice of LONG_MIN is to forbid the node
                      // nums.size() - 1 to reverse its should_xor.
    if (memo[node][should_xor] >= 0)
      return memo[node][should_xor];
    // option 1, do not XOR node. If should_xor == 1, then this decision means
    // the edge including the current node must be picked to reverse should_xor
    // = 1. Our DP requires that we must compute node + 1 as the next step.
    // In order to do so, we must ensure that all the other nodes' values
    // remain unchanged. The only way possible is to propagate should_xor = 1
    // through the path from node to node + 1. In other words, we pass on the
    // should_xor state from node to node + 1. The same analysis also works
    // if the current should_xor = 0.
    int op1 = nums[node] + dp(node + 1, should_xor, k, nums, memo);
    // option 2, do XOR node. If should_xor == 1, we need to propagate 0.
    // If should_xor == 0, we also need to propagate 1.
    int op2 = nums[node] ^ k + dp(node + 1, should_xor ^ 1, k, nums, memo);
    memo[node][should_xor] = std::max(op1, op2);
    return memo[node][should_xor];
  }

  long long maximumValueSum(vector<int> &nums, int k,
                            vector<vector<int>> &edges) {
    /*
     * LeetCode 3068 (Fail)
     *
     * It was very bad. I couldn't solve it using the hint. Nor could I
     * understand the solution I put up one year ago. It took me so long to
     * finally understand what the solution means. Here is my current
     * understanding.
     *
     * Each node has two possible state: shoud XOR or should not XOR.
     * So our dp(node, shoudXOR) computes the max sum for nums[node:] given
     * its XOR state.
     *
     * When a node should be XORed, it does not have to be XORed, because if
     * its edge is selected to be XORed, its original XOR state would be
     * negated. Hence, for a dp(node, 1) condition, the node still has two
     * choices: either not be XORed or be XORed. When the node is not XORed,
     * its edge must be picked up, which means the original shouldXOR = 1 must
     * be passed on to node's child. And since there always exists a path from
     * node to node + 1, essentially we are passing the shouldXOR state from
     * node to node + 1. In this case, we can compute dp(node + 1, 1) to find
     * the max possible sum of nums[node + 1:] under XOR condition.
     *
     * Similarly, we can choose to XOR the current node. This decision means
     * that the edge including the current node cannot be selected, or a not
     * XOR state must be passed to the other nodes. Hence we can compute
     * dp(node + 1, 0) to find the max possible sum of nums[node + 1:] under
     * NO XOR condition.
     *
     * The larger of the two scenarios determine the max value for dp(node, 1).
     *
     * The same analysis also applies to dp(node, 0).
     */
    int N = nums.size();
    std::vector<std::vector<long long>> memo(N, std::vector<long long>(2, -1));
    return dp(0, 0, k, nums, memo);
  }
};

int main() {
  std::vector<int> nums{24, 78, 1, 97, 44};
  int k = 6;
  std::vector<std::vector<int>> edges{{0, 2}, {1, 2}, {4, 2}, {3, 4}};
  Solution sol;
  std::cout << sol.maximumValueSum(nums, k, edges) << std::endl;
}
