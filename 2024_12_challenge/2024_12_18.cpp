#include <iostream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> finalPrices(vector<int> &prices) {
    /*
     * LeetCode 1475
     *
     * Use monotonic increasing stack. Each time a pop happens, we have found
     * the price-discount pair.
     *
     * O(N), 0 ms, faster than 100.00%
     */
    int N = prices.size();
    std::stack<int> mon;
    std::vector<int> res(prices.begin(), prices.end());
    for (int i = 0; i < N; i++) {
      while (!mon.empty() && prices[mon.top()] >= prices[i]) {
        int j = mon.top();
        mon.pop();
        res[j] = prices[j] - prices[i];
      }
      mon.push(i);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
