#include <iostream>

using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */


class Solution {
public:
    void helper(TreeNode* node, int low, int high, int* res) {
        if (node == nullptr || low > high) {return;}
        if (node->val < low) {
            helper(node->right, low, high, res);
        } else if (node->val > high) {
            helper(node->left, low, high, res);
        } else {
            *res += node->val;
            helper(node->left, low, node->val - 1, res);
            helper(node->right, node->val + 1, high, res);  
        }
    }

    /*
    69% ranking.
    I think this is a standard solution, where at each node, we decide whether
    to go left branch, right branch, or both.
    */
    int rangeSumBST(TreeNode* root, int low, int high) {
        int res = 0;
        helper(root, low, high, &res);
        return res;
    }
};
 
 
int main() {
    cout<<"life is lonly\n";
    return 0;
}