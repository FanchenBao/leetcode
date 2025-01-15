#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findThePrefixCommonArray(vector<int> &A, vector<int> &B) {
    /*
     * LeetCode 2657
     *
     * Use bitmask to keep track of what number has appeared in A and B. The
     * AND of the two bitmasks show the common numbers.
     *
     * NOTE: have to use __builtin_popcountll() to handle long long
     *
     * O(N), 0 ms, 100%
     */
    long long mask_a = 0, mask_b = 0;
    long long bit = (long long)1;
    std::vector<int> res;
    for (int i = 0; i < A.size(); i++) {
      mask_a |= (bit << A[i]);
      mask_b |= (bit << B[i]);
      res.push_back(__builtin_popcountll(mask_a & mask_b));
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
