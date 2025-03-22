#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> findAllRecipes(vector<string> &recipes,
                                vector<vector<string>> &ingredients,
                                vector<string> &supplies) {
    /*
     * LeetCode 2115
     *
     * Brute force
     *
     * O(N^2), 1096 ms 5.05%
     */
    std::unordered_set<std::string> sup(supplies.begin(), supplies.end());
    std::vector<string> res;
    std::vector<int> queue;
    int N = ingredients.size();
    for (int i = 0; i < N; i++)
      queue.push_back(i);
    while (!queue.empty()) {
      std::vector<int> tmp;
      for (int i : queue) {
        auto ing = ingredients[i];
        bool contains_all = true;
        for (auto &in : ing) {
          if (!sup.contains(in)) {
            contains_all = false;
            break;
          }
        }
        if (contains_all) {
          res.push_back(recipes[i]);
          sup.insert(recipes[i]);
        } else {
          tmp.push_back(i);
        }
      }
      if (tmp.size() == queue.size()) // cannot make more recipe
        break;
      queue = tmp;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
