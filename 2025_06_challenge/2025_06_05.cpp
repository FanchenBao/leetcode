#include <iostream>
#include <set>
#include <vector>

using namespace std;

class DSU {
public:
  DSU() {
    for (int i = 0; i < 26; i++)
      par_.push_back(i);
  };

  int find_(int x) {
    if (par_[x] != x) {
      par_[x] = find_(par_[x]);
    }
    return par_[x];
  }

  bool union_(int x, int y) {
    int px = find_(x), py = find_(y);
    if (px == py)
      return false; // already unioned
    if (px < py) {
      par_[py] = px;
    } else {
      par_[px] = py;
    }
    return true;
  }

private:
  std::vector<int> par_;
};

class Solution {
public:
  string smallestEquivalentString(string s1, string s2, string baseStr) {
    /*
     * LeetCode 1061
     *
     * We will use Union-Find. We ensure that each time find is called, the
     * smallest letter is returned.
     *
     * O(UnionFind * N), 3 ms, 41.19%
     */
    DSU dsu;
    for (int i = 0; i < s1.size(); i++)
      dsu.union_(s1[i] - 'a', s2[i] - 'a');
    std::string res;
    for (char c : baseStr)
      res.push_back(char(dsu.find_(c - 'a') + 'a'));
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
