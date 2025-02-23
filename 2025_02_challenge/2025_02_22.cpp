#include <cctype>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

using namespace std;

/* Definition for a binary tree node. */
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
  int build(TreeNode *node, int depth, int idx,
            std::vector<std::pair<int, int>> &parsed) {
    /*
     * node: the node that is being visited now
     * depth: the depth of the current node
     * idx: the index pointing to the next available (depth, val) pair
     * parsed: a list of parsed (depth, val) pair
     */
    if (idx == parsed.size() || parsed[idx].first <= depth)
      return idx;
    node->left = new TreeNode(parsed[idx].second);
    int ni = build(node->left, parsed[idx].first, idx + 1, parsed);
    if (ni == parsed.size() || parsed[ni].first <= depth)
      return ni;
    node->right = new TreeNode(parsed[ni].second);
    return build(node->right, parsed[ni].first, ni + 1, parsed);
  }

public:
  TreeNode *recoverFromPreorder(string traversal) {
    /*
     * LeetCode 1028
     *
     * First, parse travesal to get the order and depth of the nodes.
     * Then reconstruct.
     *
     * O(N), 0 ms, 100%
     */
    std::vector<std::pair<int, int>> parsed; // each ele is [depth, val]
    int depth = 0, val = 0;
    int i = 0;
    while (i < traversal.size()) {
      while (i < traversal.size() && traversal[i] == '-') {
        depth++;
        i++;
      }
      while (i < traversal.size() && std::isdigit(traversal[i])) {
        val = val * 10 + traversal[i++] - '0';
      }
      parsed.push_back({depth, val});
      depth = 0, val = 0;
    }

    TreeNode *root = new TreeNode(parsed[0].second);
    build(root, 0, 1, parsed);
    return root;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
