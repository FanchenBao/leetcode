#include <iostream>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  long long putMarbles(vector<int> &weights, int k) {
    /*
     * LeetCode 2551 (Fallo)
     *
     * Although this counts as another fail, we are very close to solve it.
     * I realized that to make k subarrays, we need k - 1 breaks. Each break
     * consists of two adjacent numbers in weights. But that's where I got
     * stuck. The trick is to sort all adjacent pairs based on their sum. Then
     * the min way of partitioning the subarrays are the sum of the smallest
     * k - 1 pairs. Similarly, the max way of partitioning is the sum of the
     * largest k - 1 pairs.
     *
     * O(NlogN), 37 ms, 48.52%
     */
    std::vector<int> pairs;
    int N = weights.size();
    for (int i = 0; i < N - 1; i++) {
      pairs.push_back(weights[i] + weights[i + 1]);
    }
    std::sort(pairs.begin(), pairs.end());
    long long min_score = 0, max_score = 0;
    for (int i = 0; i < pairs.size() && i < k - 1; i++) {
      min_score += (long long)pairs[i];
      max_score += (long long)pairs[pairs.size() - i - 1];
    }
    return max_score - min_score;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
