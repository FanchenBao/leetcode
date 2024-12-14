#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  long long findScore(vector<int> &nums) {
    /*
     * LeetCode 2593
     *
     * Priority queue.
     *
     * O(NlogN), 322 ms, faster than 16.25%
     */
    auto cmp = [](const std::pair<int, int> &a, const std::pair<int, int> &b) {
      if (a.first == b.first)
        return a.second > b.second;
      return a.first > b.first; // min heap
    };
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        decltype(cmp)>
        pq(cmp);
    std::set<int> marked;
    for (int i = 0; i < nums.size(); i++)
      pq.push({nums[i], i});
    long long res = 0;
    while (!pq.empty()) {
      auto ele = pq.top();
      pq.pop();
      if (marked.contains(ele.second))
        continue;
      res += (long long)ele.first;
      marked.insert(ele.second + 1);
      marked.insert(ele.second - 1);
    }
    return res;
  }
};

class Solution2 {
public:
  long long findScore(vector<int> &nums) {
    /*
     * LeetCode 2593
     *
     * Priority queue, and with a vector to check whether an index
     * has been marked. This may be faster than using a set.
     *
     * O(NlogN), 121 ms, faster than 66.07%
     */
    auto cmp = [](const std::pair<int, int> &a, const std::pair<int, int> &b) {
      if (a.first == b.first)
        return a.second > b.second;
      return a.first > b.first; // min heap
    };
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        decltype(cmp)>
        pq(cmp);
    int N = nums.size();
    std::vector<bool> marked(N);
    for (int i = 0; i < nums.size(); i++)
      pq.push({nums[i], i});
    long long res = 0;
    while (!pq.empty()) {
      auto ele = pq.top();
      pq.pop();
      if (marked[ele.second])
        continue;
      res += (long long)ele.first;
      marked[std::min(N - 1, ele.second + 1)] = true;
      marked[std::max(0, ele.second - 1)] = true;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{8, 6, 1, 9, 2, 2, 8};
  Solution sol;
  std::cout << sol.findScore(arr) << std::endl;
}
