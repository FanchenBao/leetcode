#include <algorithm>
#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  int binary_search(vector<vector<int>> &events, int end) {
    int lo = 0, hi = events.size();
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (events[mid][0] <= end)
        lo = mid + 1;
      else
        hi = mid;
    }
    return lo;
  }

  int maxTwoEvents(vector<vector<int>> &events) {
    /*
     * LeetCode 2054
     *
     * Sort events by starting point and produce a suffix max array to record
     * the max value from events[i:].
     *
     * Then for each event, binary search the sorted events to find the first
     * index whose start is larger than the current event's end. We then use
     * the suffix max array to find the max value achievable from that index
     * to the end.
     *
     * O(NlogN), 2297 ms, faster than 5.40%
     */
    std::sort(events.begin(), events.end(),
              [](vector<int> a, vector<int> b) { return a[0] < b[0]; });
    int N = events.size();
    std::vector<int> suff_max(N);
    suff_max[N - 1] = events[N - 1][2];
    for (int i = N - 2; i >= 0; i--)
      suff_max[i] = std::max(events[i][2], suff_max[i + 1]);
    int res = 0;
    for (auto event : events) {
      res = std::max(res, event[2]);
      int idx = binary_search(events, event[1]);
      if (idx < N)
        res = std::max(res, event[2] + suff_max[idx]);
    }
    return res;
  }
};

class Solution2 {
public:
  int maxTwoEvents(vector<vector<int>> &events) {
    /*
     * This is a two pointer solution without binary search.
     *
     * O(NlogN), 95 ms, faster than 54.50%
     */
    int N = events.size();
    std::vector<std::pair<int, int>> ends;
    std::vector<std::pair<int, int>> starts;
    for (auto event : events) {
      ends.push_back(std::make_pair(event[1], event[2]));
      starts.push_back(std::make_pair(event[0], event[2]));
    }
    std::sort(ends.begin(), ends.end(),
              [](std::pair<int, int> a, std::pair<int, int> b) {
                return a.first < b.first;
              });
    std::sort(starts.begin(), starts.end(),
              [](std::pair<int, int> a, std::pair<int, int> b) {
                return a.first < b.first;
              });
    for (int i = N - 2; i >= 0; i--) // suffix max
      starts[i].second = std::max(starts[i].second, starts[i + 1].second);
    int res = 0;
    int j = 0;
    for (int i = 0; i < N; i++) {
      res = std::max(res, ends[i].second);
      while (j < N && starts[j].first <= ends[i].first)
        j++;
      if (j < N)
        res = std::max(res, ends[i].second + starts[j].second);
    }
    return res;
  }
};

class Solution3 {
public:
  int maxTwoEvents(vector<vector<int>> &events) {
    /*
     * This solution originates from the official solution with the priority
     * queue. We sort events by starting point. Then for each event, we look
     * to the left to find the max value so far with ending smaller than the
     * current event's start. Essentially, we are creating a prefix max using
     * priority queue.
     *
     * Also, there is no need to check max just against the event itself,
     * because for an events that cannot be paired with a previous event,
     * the pref_max would always be zero. pref_max + event[2] would be
     * equivalent to checking against event[2] itself.
     *
     * O(NlogN), 50 ms, faster than 91.89%
     */
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        std::greater<std::pair<int, int>>>
        pq;
    std::sort(events.begin(), events.end());
    int pref_max = 0;
    int res = 0;
    for (auto &event : events) {
      // res = std::max(res, event[2]);  // not necessary to check against
      // itself
      while (!pq.empty() && pq.top().first < event[0]) {
        pref_max = std::max(pref_max, pq.top().second);
        pq.pop();
      }
      res = std::max(res, event[2] + pref_max);
      pq.push({event[1], event[2]});
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
