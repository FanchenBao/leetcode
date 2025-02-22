#include <iostream>
#include <set>
#include <unordered_set>
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

class FindElements {
private:
  std::unordered_set<int> vals;

  void dfs(TreeNode *node) {
    if (node == nullptr)
      return;
    vals.insert(node->val);
    if (node->left != nullptr) {
      node->left->val = node->val * 2 + 1;
      dfs(node->left);
    }
    if (node->right != nullptr) {
      node->right->val = node->val * 2 + 2;
      dfs(node->right);
    }
  }

public:
  FindElements(TreeNode *root) {
    /*
     * LeetCode 1261
     *
     * DFS and put all the values in a set.
     */
    root->val = 0;
    dfs(root);
  }

  bool find(int target) { return vals.contains(target); }
};
/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
