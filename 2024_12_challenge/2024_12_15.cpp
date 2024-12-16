#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  double maxAverageRatio(vector<vector<int>> &classes, int extraStudents) {
    /*
     * LeetCode 1792 (Pista)
     *
     * I think this problem is pretty hard. After reading the hint, I know how
     * to solve it. The key is that each additional student added to a class
     * produces diminishing increase in the passing ratio. Thus, the goal is
     * to maximize the passing ratio for each added student. We can use a max
     * heap to find the max delta of passing ratio of the current added student.
     * We only add students to the class that produces the max delta of passing
     * ratio for each round.
     *
     * O(NlogN + KlogN), where K = extraStudents, 580 ms, faster than 17.95%
     */
    // pair means (idx, number of students added)
    auto cmp = [&](std::pair<int, int> a, std::pair<int, int> b) {
      double diff_a = (double)(classes[a.first][0] + a.second) /
                          (classes[a.first][1] + a.second) -
                      (double)(classes[a.first][0] + a.second - 1) /
                          (classes[a.first][1] + a.second - 1);
      double diff_b = (double)(classes[b.first][0] + b.second) /
                          (classes[b.first][1] + b.second) -
                      (double)(classes[b.first][0] + b.second - 1) /
                          (classes[b.first][1] + b.second - 1);
      return diff_a < diff_b;
    };
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        decltype(cmp)>
        pq(cmp);
    int N = classes.size();
    std::vector<int> extraPerClass(N);
    for (int i = 0; i < N; i++)
      pq.push({i, 1});
    while (!pq.empty() && extraStudents > 0) {
      auto ele = pq.top();
      pq.pop();
      extraPerClass[ele.first]++;
      pq.push({ele.first, ele.second + 1});
      extraStudents--;
    }
    double res = 0;
    for (int i = 0; i < N; i++)
      res += (double)(classes[i][0] + extraPerClass[i]) /
             (classes[i][1] + extraPerClass[i]);
    return res / N;
  }
};

class Solution2 {
public:
  double get_delta(int passes, int total) {
    return (double)(passes + 1) / (total + 1) - (double)(passes) / total;
  }

  double maxAverageRatio(vector<vector<int>> &classes, int extraStudents) {
    /*
     * This is the official solution, much better implementation of max heap
     * than mine, because it directly put the delta of the ratio in the heap.
     *
     * O(NlogN + KlogN), 359 ms, faster than 54.70%
     *
     */
    std::priority_queue<std::pair<double, std::pair<int, int>>> pq;
    for (auto cls : classes)
      pq.push({get_delta(cls[0], cls[1]), {cls[0], cls[1]}});
    while (extraStudents > 0) {
      auto [_, cls] = pq.top();
      pq.pop();
      pq.push({get_delta(cls.first + 1, cls.second + 1),
               {cls.first + 1, cls.second + 1}});
      extraStudents--;
    }
    double res = 0;
    while (!pq.empty()) {
      auto [_, cls] = pq.top();
      pq.pop();
      res += (double)(cls.first) / cls.second;
    }
    return res / classes.size();
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
