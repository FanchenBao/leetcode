#include <functional>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> getFinalState(vector<int> &nums, int k, int multiplier) {
    /*
     * LeetCode 3264
     *
     * Priority queue, again.
     *
     * O(NlogN + KlogN), 0 ms, faster than 100.00%
     */
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        std::greater<std::pair<int, int>>>
        pq;
    int N = nums.size();
    for (int i = 0; i < N; i++)
      pq.push({nums[i], i});
    while (k > 0) {
      auto ele = pq.top();
      pq.pop();
      pq.push({ele.first * multiplier, ele.second});
      k--;
    }
    std::vector<int> res(N);
    while (!pq.empty()) {
      auto ele = pq.top();
      pq.pop();
      res[ele.second] = ele.first;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
