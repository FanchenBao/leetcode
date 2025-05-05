#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  int maxTaskAssign(vector<int> &tasks, vector<int> &workers, int pills,
                    int strength) {
    /*
     * LeetCode 2071 (FAIL, didn't work)
     *
     * My idea is greedy. We sort the tasks and go from most demanding to least
     * demanding. For each task, we always use the pill. Then we can find the
     * min strength needed to accomplish the task. Then we look in the workers
     * for the weakest woker whose strength is no smaller than the min strength.
     *
     * O(NlogN)
     */
    std::map<int, int> counter;
    for (int w : workers)
      counter[w]++;
    std::sort(tasks.begin(), tasks.end());
    int res = 0;
    for (int i = tasks.size() - 1; i >= 0; i--) {
      int min_strength = tasks[i] - strength * (pills > 0);
      auto it = counter.lower_bound(min_strength);
      if (it != counter.end()) {
        res++;
        int k = it->first;
        counter[k]--;
        if (counter[k] == 0)
          counter.erase(k);
        if (k < tasks[i])
          pills--;
      }
    }
    return res;
  }
};

class Solution2 {
public:
  int maxTaskAssign(vector<int> &tasks, vector<int> &workers, int pills,
                    int strength) {
    /*
     * Hint (WRONG AGAIN!)
     *
     * This solution is inspired by the hint.
     *
     * We will use binary search. At each iteration, we want to see if we can
     * accomplish k tasks. If we can, we continue searching the upper half,
     * otherwise the lower half.
     *
     * Given k tasks, we want to use the least demanding k tasks and the
     * strongest k workers. Of course, both tasks and workers have been sorted.
     *
     * When checking whether it is possible for the k strongest workers to
     * finish the k least demanding tasks, we use a priority queue to always
     * surface the currently weakest worker. If this worker cannot handle
     * the currently least demanding task, it requires a pill and goes back
     * to the priority queue.
     *
     * O(N(logN)^2)
     */
    int M = workers.size(), N = tasks.size();
    std::sort(tasks.begin(), tasks.end());
    std::sort(workers.begin(), workers.end());
    int lo = 0, hi = N + 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (mid > M) { // not enough workers
        hi = mid;
        continue;
      }
      int pills_rem = pills;
      std::priority_queue<std::pair<int, int>>
          queue; // (strength, has taken pill)
      for (int i = 0; i < mid; i++)
        queue.push({-workers[M - mid + i], 0});
      int i = 0;
      while (i < mid) {
        auto p = queue.top();
        queue.pop();
        if (-p.first < tasks[i]) {
          if (pills_rem == 0 || p.second) // either no more pill or the worker
                                          // has already taken the pill
            break;
          queue.push({-(-p.first + strength), 1});
          pills_rem--;
          continue;
        }
        i++;
      }
      if (i < mid)
        hi = mid;
      else
        lo = mid + 1;
    }
    return lo - 1;
  }
};

class Solution3 {
public:
  int maxTaskAssign(vector<int> &tasks, vector<int> &workers, int pills,
                    int strength) {
    /*
     * This is the solution inspired by the editorial. It is very similar to
     * Solution2 where we use binary search. However, instead of using a
     * priority queue to always consider the currently weakest worker, we
     * ensure that if a task requires someone to take a pill, we use the worker
     * with the lowest strength as possible.
     *
     * O(N(logN)^2), 792 ms, 36.69%
     */
    int M = workers.size(), N = tasks.size();
    std::sort(tasks.begin(), tasks.end());
    std::sort(workers.begin(), workers.end());
    int lo = 0, hi = N + 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (mid > M) { // not enough workers
        hi = mid;
        continue;
      }
      int pills_rem = pills;
      std::multiset<int> ws;
      for (int i = 0; i < mid; i++)
        ws.insert(workers[M - mid + i]);
      for (int i = mid - 1; i >= 0; i--) {
        auto max_it = --ws.end();
        if (*max_it >= tasks[i]) {
          ws.erase(max_it);
        } else if (pills_rem <= 0) {
          break;
        } else {
          auto it = ws.lower_bound(tasks[i] - strength);
          if (it == ws.end())
            break;
          ws.erase(it);
          pills_rem--;
        }
      }
      if (!ws.empty())
        hi = mid;
      else
        lo = mid + 1;
    }
    return lo - 1;
  }
};

int main() {
  std::vector<int> tasks{3, 2, 1};
  std::vector<int> workers{0, 3, 3};
  int pills = 1;
  int strength = 1;
  Solution3 sol;
  std::cout << sol.maxTaskAssign(tasks, workers, pills, strength) << std::endl;
}
