#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long continuousSubarrays(vector<int> &nums) {
    /*
     * LeetCode 2762
     *
     * Two priority queues, one max heap and the other min heap. For each
     * new number encountered, we put its index in both heaps. And then pop
     * the heaps if the min or max values exceed the requirement with regards
     * to the current number.
     *
     * Each pop help us find the start of the continous subarray that
     * ends at the current number.
     *
     * O(NlogN), 137 ms, faster than 48.20%
     */
    auto min_cmp = [&](int left, int right) {
      return nums[left] > nums[right];
    };
    auto max_cmp = [&](int left, int right) {
      return nums[left] < nums[right];
    };
    std::priority_queue<int, std::vector<int>, decltype(min_cmp)> min_heap(
        min_cmp);
    std::priority_queue<int, std::vector<int>, decltype(max_cmp)> max_heap(
        max_cmp);
    int N = nums.size();
    long long res = 0;
    int i = 0;
    for (int j = 0; j < N; j++) {
      min_heap.push(j);
      max_heap.push(j);
      while (!min_heap.empty() && nums[j] - nums[min_heap.top()] > 2) {
        i = std::max(min_heap.top() + 1, i);
        min_heap.pop();
      }
      while (!max_heap.empty() && nums[max_heap.top()] - nums[j] > 2) {
        i = std::max(max_heap.top() + 1, i);
        max_heap.pop();
      }
      res += (long)j - i + 1;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{5, 4, 2, 4};
  Solution sol;
  std::cout << sol.continuousSubarrays(arr) << std::endl;
}
