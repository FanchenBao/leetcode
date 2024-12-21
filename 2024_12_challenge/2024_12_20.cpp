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
  void reverse(std::vector<TreeNode *> row) {
    int i = 0, j = row.size() - 1;
    while (i < j) {
      int tmp = row[i]->val;
      row[i]->val = row[j]->val;
      row[j]->val = tmp;
      i++;
      j--;
    }
  }

public:
  TreeNode *reverseOddLevels(TreeNode *root) {
    /*
     * LeetCode 2415
     *
     * BFS. O(N), 5 ms, faster than 30.56%
     */
    std::vector<TreeNode *> queue;
    queue.push_back(root);
    int lvl = 0;
    while (!queue.empty()) {
      std::vector<TreeNode *> tmp;
      if (lvl % 2 == 1)
        reverse(queue);
      for (auto node : queue) {
        if (node->left != nullptr)
          tmp.push_back(node->left);
        if (node->right != nullptr)
          tmp.push_back(node->right);
      }
      lvl++;
      queue = tmp;
    }
    return root;
  }
};

class Solution2 {
private:
  void dfs(TreeNode *left, TreeNode *right, int lvl) {
    if (left == nullptr || right == nullptr)
      return;
    if (lvl % 2 == 1) {
      int tmp = left->val;
      left->val = right->val;
      right->val = tmp;
    }
    dfs(left->left, right->right, lvl + 1);
    dfs(left->right, right->left, lvl + 1);
  }

public:
  TreeNode *reverseOddLevels(TreeNode *root) {
    /*
     * This is the DFS solution from the official solution. It is really
     * really smart. The DFS happen on two nodes. If the level is odd, we
     * swap the values of the two nodes. Then the magic happens. For the
     * next level, we dfs(node1.left, node2.right) and dfs(node1.right,
     * node2.left) This ensures that each call picks two symmetric nodes and
     * their subsequent calls also involve symmetric nodes on either sides. O(N)
     *
     * 0 ms, faster than 100.00%
     */
    dfs(root->left, root->right, 1);
    return root;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
