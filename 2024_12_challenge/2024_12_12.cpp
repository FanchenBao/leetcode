#include <cmath>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long pickGifts(vector<int> &gifts, int k) {
    /*
     * LeetCode 2558
     *
     * Priority Queue
     * O(KlogN), 4 ms, faster than 31.50%
     */
    std::priority_queue<int> pq;
    long long res = 0;
    for (int n : gifts) {
      pq.push(n);
      res += (long long)n;
    }
    while (k > 0 && !pq.empty()) {
      int p = pq.top();
      pq.pop();
      int np = std::floor(std::sqrt(p));
      res -= (long long)p - np;
      if (np > 0)
        pq.push(np);
      k--;
    }
    return res;
  }
};

class Solution2 {
public:
  long long pickGifts(vector<int> &gifts, int k) {
    /*
     * Same solution but hopefully faster
     *
     * 1 ms, faster than 68.38%
     */
    std::priority_queue<int> pq(gifts.begin(), gifts.end());
    long long res = 0;
    for (int n : gifts)
      res += (long long)n;
    for (int i = 0; i < k; i++) {
      int p = pq.top();
      pq.pop();
      int np = (int)std::sqrt(p);
      res -= (long long)p - np;
      pq.push(np);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
