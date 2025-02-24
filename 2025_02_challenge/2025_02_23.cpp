#include <iostream>
#include <set>
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
  TreeNode *build(std::vector<int> &preorder, int prelo, int prehi,
                  std::vector<int> &postorder, int poslo, int poshi) {
    if (prelo == prehi && poslo == poshi)
      return new TreeNode(preorder[prelo]);
    if (prelo > prehi || poslo > poshi)
      return nullptr;
    int i = poslo;
    while (i <= poshi && prelo + 1 <= prehi &&
           postorder[i] != preorder[prelo + 1])
      i++;
    return new TreeNode(
        preorder[prelo],
        build(preorder, prelo + 1, prelo + 1 + i - poslo, postorder, poslo, i),
        build(preorder, prelo + 2 + i - poslo, prehi, postorder, i + 1,
              poshi - 1));
  }

public:
  TreeNode *constructFromPrePost(vector<int> &preorder,
                                 vector<int> &postorder) {
    /*
     * LeetCode 889
     *
     * preorder[0] and postorder[-1] must be the same and the root of the
     * current tree.
     *
     * preorder[1] must be the root of a child tree, maybe a left or a right
     * child. Then we traverse postorder from the start until we encounter
     * the same value as preorder[1]. Then we have a subarray that represents
     * the entire child tree. We can build the tree using the subarray.
     *
     * Then we can build the other child tree with the remaining subarray, IF
     * such a remaining subarray exists.
     *
     * Then we assemble the curren tree.
     *
     * O(NlogN), 0 ms 100%
     */
    return build(preorder, 0, preorder.size() - 1, postorder, 0,
                 postorder.size() - 1);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
