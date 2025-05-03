#include <iostream>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

class Solution {
public:
  string pushDominoes(string dominoes) {
    /*
     * LeetCode 838
     *
     * Two pointers.
     *
     * O(N), 19 ms, 50%
     */
    std::vector<char> vec(dominoes.begin(), dominoes.end());
    int lo = 0;
    for (int hi = 0; hi < dominoes.size(); hi++) {
      if (dominoes[hi] == 'L') {
        if (dominoes[lo] == 'R') {
          int i = lo + 1, j = hi - 1;
          while (i < j) {
            vec[i++] = 'R';
            vec[j--] = 'L';
          }
          lo = hi + 1;
        } else {
          while (lo < hi) {
            vec[lo++] = 'L';
          }
        }
      } else if (dominoes[hi] == 'R') {
        if (dominoes[lo] == 'R') {
          while (lo < hi) {
            vec[lo++] = 'R';
          }
        } else {
          lo = hi;
        }
      }
    }
    if (dominoes[lo] == 'R') {
      while (lo < dominoes.size())
        vec[lo++] = 'R';
    }
    std::stringstream ss;
    for (char c : vec)
      ss << c;
    return ss.str();
  }
};

class Solution2 {
public:
  string pushDominoes(string dominoes) {
    /*
     * This solution is inspired by the editorial. We add additional L and R
     * to the left and right of the dominoes. Thus, there are only four
     * scenarios of pairs: (L...L), (L...R), (R...L), and (R...R).
     * Each scenario is independent. So we can analyze them by individually.
     *
     * O(N), 17 ms, 54%
     */
    int N = dominoes.size();
    std::vector<char> vec(N + 2);
    vec[0] = 'L', vec[N + 1] = 'R';
    for (int i = 0; i < N; i++)
      vec[i + 1] = dominoes[i];
    int lo = 0;
    for (int hi = 1; hi < N + 2; hi++) {
      if (vec[hi] == 'L') {
        if (vec[lo] == 'L') {
          for (int i = lo + 1; i < hi; i++)
            vec[i] = 'L';
        } else {
          int i = lo + 1, j = hi - 1;
          while (i < j) {
            vec[i++] = 'R';
            vec[j--] = 'L';
          }
        }
        lo = hi;
      } else if (vec[hi] == 'R') {
        if (vec[lo] == 'R') {
          for (int i = lo + 1; i < hi; i++)
            vec[i] = 'R';
        }
        lo = hi;
      }
    }
    std::stringstream ss;
    for (int i = 1; i <= N; i++)
      ss << vec[i];
    return ss.str();
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
