#include <algorithm>
#include <deque>
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
  int get_swap_cnt(std::deque<TreeNode *> &row, int pos[]) {
    std::vector<int> vals;
    int i = 0;
    for (auto node : row) {
      vals.push_back(node->val);
      pos[node->val] = i;
      i++;
    }
    std::vector<int> sorted_vals{vals.begin(), vals.end()};
    std::sort(sorted_vals.begin(), sorted_vals.end());
    int res = 0;
    for (i = 0; i < vals.size(); i++) {
      int v = vals[i];
      int sv = sorted_vals[i];
      if (pos[v] != pos[sv]) {
        int tmp = pos[v];
        pos[v] = pos[sv];
        pos[sv] = tmp;
        res++;
        vals[pos[v]] = v;
        vals[pos[sv]] = sv;
      }
    }
    return res;
  }

public:
  int minimumOperations(TreeNode *root) {
    /*
     * LeetCode 2471
     *
     * BFS, and for each level, we find the min number of swaps to sort its
     * values. To get the min number of swaps, we simply go through the level
     * and swap whenever needed.
     *
     * O(NlogN) 50 ms, faster than 93.55%
     */
    std::deque<TreeNode *> queue;
    queue.push_back(root);
    int res = 0;
    int pos[100001];
    while (!queue.empty()) {
      res += get_swap_cnt(queue, pos);
      int N = queue.size();
      for (int i = 0; i < N; i++) {
        auto node = queue.front();
        queue.pop_front();
        if (node->left != nullptr)
          queue.push_back(node->left);
        if (node->right != nullptr)
          queue.push_back(node->right);
      }
    }
    return res;
  }
};

class Solution2 {
private:
  int get_swap_cnt(std::deque<TreeNode *> &row, int pos[]) {
    // Use the technique of the official solution, where we combine values and
    // their original indices, sort them, and then count the number of steps
    // to revert the sorted version back to its original.
    std::vector<std::pair<int, int>> vals;
    int i = 0;
    for (auto node : row) {
      vals.push_back({node->val, i});
      i++;
    }
    std::sort(vals.begin(), vals.end());
    int res = 0;
    for (i = 0; i < vals.size(); i++) {
      if (vals[i].second != i) {
        std::swap(vals[i],
                  vals[vals[i].second]); // put vals[i] to its right position
        res++;
        i--; // check this position again
      }
    }
    return res;
  }

public:
  int minimumOperations(TreeNode *root) {
    /*
     * This is essentially the same solution as Solution1, except that we use
     * the method in the official solution to count the number of swaps.
     *
     * O(NlogN), 47 ms, faster than 94.13%
     */
    std::deque<TreeNode *> queue;
    queue.push_back(root);
    int res = 0;
    int pos[100001];
    while (!queue.empty()) {
      res += get_swap_cnt(queue, pos);
      int N = queue.size();
      for (int i = 0; i < N; i++) {
        auto node = queue.front();
        queue.pop_front();
        if (node->left != nullptr)
          queue.push_back(node->left);
        if (node->right != nullptr)
          queue.push_back(node->right);
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
