#include <algorithm>
#include <iostream>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  int minDominoRotations(vector<int> &tops, vector<int> &bottoms) {
    /*
     * LeetCode 1007
     *
     * Find the indices of each element in tops and bottoms. Check the ones
     * that exist in both, and see if the union of their indices can cover
     * the entire vector. If so, choose the one with fewer replacement.
     *
     * O(N), 20 ms, 7.33%
     */
    int N = tops.size();
    std::unordered_map<int, std::vector<int>> top_indices;
    std::unordered_map<int, std::vector<int>> bot_indices;
    for (int i = 0; i < N; i++) {
      top_indices[tops[i]].push_back(i);
      bot_indices[bottoms[i]].push_back(i);
    }
    int res = N + 1;
    for (const auto &[val, top_is] : top_indices) {
      if (bot_indices.contains(val)) {
        auto bot_is = bot_indices[val];
        std::vector<int> v(top_is.size() + bot_is.size());
        auto it = std::set_union(top_is.begin(), top_is.end(), bot_is.begin(),
                                 bot_is.end(), v.begin());
        if (it - v.begin() == N)
          res = std::min(
              res, std::min(int(N - top_is.size()), int(N - bot_is.size())));
      }
    }
    return res > N ? -1 : res;
  }
};

class Solution2 {
private:
  int get_num_swaps(vector<int> &base, vector<int> &swap, int tgt) {
    int N = base.size();
    int cnt = 0, i = 0;
    // check using tops[0]
    // tops is base, bottoms is swap
    while (i < N) {
      if (base[i] != tgt) {
        if (swap[i] != tgt)
          break;
        cnt++;
      }
      i++;
    }
    return i == N ? cnt : N + 1;
  }

public:
  int minDominoRotations(vector<int> &tops, vector<int> &bottoms) {
    /*
     * This solution is inspired by my previous attempt at this problem more
     * than two years ago.
     *
     * The key insight is that after one of the vector has the same numbers,
     * it must take either its own first value, or the other vector's first
     * value. Therefore, we just need to check the number of swaps when all
     * the values are either tops[0] or bottoms[0].
     *
     * O(N), 4ms, 56.25%
     */
    int N = tops.size();
    int res = N + 1;
    res = std::min(res, get_num_swaps(tops, bottoms, tops[0]));
    res = std::min(res, get_num_swaps(tops, bottoms, bottoms[0]));
    res = std::min(res, get_num_swaps(bottoms, tops, tops[0]));
    res = std::min(res, get_num_swaps(bottoms, tops, bottoms[0]));
    return res > N ? -1 : res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
