#include <iostream>
#include <set>
#include <vector>

using namespace std;
/**
 * Definition for a binary tree node.
 */
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
private:
  void dfs(TreeNode *node, int lvl, std::vector<int> &res) {
    if (node == nullptr)
      return;
    if (lvl == res.size())
      res.push_back(node->val);
    else
      res[lvl] = std::max(res[lvl], node->val);
    dfs(node->left, lvl + 1, res);
    dfs(node->right, lvl + 1, res);
  }

public:
  vector<int> largestValues(TreeNode *root) {
    /*
     * LeetCode 515
     *
     * Although BFS is more intuitive, let's use DFS for fun.
     *
     * O(N), 0 ms, faster than 100.00%
     */
    std::vector<int> res;
    dfs(root, 0, res);
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
