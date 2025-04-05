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
public:
  void dfs(TreeNode *node, std::vector<std::vector<TreeNode *>> &longest_paths,
           std::vector<TreeNode *> &path) {
    if (!node)
      return;
    path.push_back(node);
    std::vector<TreeNode *> cp;

    if (!node->left && !node->right) {
      // leaf
      if (longest_paths.empty() || longest_paths[0].size() == path.size()) {
        for (auto p : path)
          cp.push_back(p);
        longest_paths.push_back(cp);
      } else if (longest_paths[0].size() < path.size()) {
        for (auto p : path)
          cp.push_back(p);
        longest_paths.clear();
        longest_paths.push_back(cp);
      }
    }
    dfs(node->left, longest_paths, path);
    dfs(node->right, longest_paths, path);
    path.pop_back(); // backtracking
  }

  TreeNode *lcaDeepestLeaves(TreeNode *root) {
    /*
     * LeetCode 1123
     *
     * First find the paths for all the deepest leaves. Then compare across
     * all the longest paths to find the first node shared among them all.
     *
     * O(N^2), 0 ms
     */
    std::vector<std::vector<TreeNode *>> longest_paths;
    std::vector<TreeNode *> path;
    dfs(root, longest_paths, path);
    int N = longest_paths[0].size();
    for (int i = N - 1; i >= 0; i--) {
      int j = 0;
      while (j < longest_paths.size() - 1 &&
             longest_paths[j][i]->val == longest_paths[j + 1][i]->val) {
        j++;
      }
      if (j == longest_paths.size() - 1)
        return longest_paths[j][i];
    }
    return new TreeNode(); // we shall never reach here.
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
