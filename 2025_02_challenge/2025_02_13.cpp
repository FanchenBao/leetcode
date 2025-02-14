#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    /*
     * LeetCode 3066
     *
     * Use a min heap.
     * 86 ms, 91.25%
     */
    std::priority_queue<long long, std::vector<long long>,
                        std::greater<long long>>
        pq(nums.begin(), nums.end());
    int op = 0;
    while (pq.size() >= 2 && pq.top() < k) {
      long long x = pq.top();
      pq.pop();
      long long y = pq.top();
      pq.pop();
      pq.push(std::min(x, y) * 2 + std::max(x, y));
      op++;
    }
    return op;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
