#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numOfSubarrays(vector<int> &arr) {
    /*
     * LeetCode 1524
     *
     * Prefix sum, then count the number of even or odd psum along the way.
     * The answer is the product of the two counts.
     *
     * O(N), 3 ms, 73%
     */
    long long even = 1,
              odd = 0; // even gets an initial count for 0 in prefix sum
    int psum = 0;
    for (int a : arr) {
      psum += a;
      if (psum % 2 == 0)
        even++;
      else
        odd++;
    }
    return int((even * odd) % 1000000007);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
