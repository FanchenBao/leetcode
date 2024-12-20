#include <functional>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution1 {
public:
  int maxChunksToSorted(vector<int> &arr) {
    /*
     * LeetCode 769
     *
     * Use a min heap to keep track of the min value encountered so far. We
     * also use a tgt to keep track of the min value we must include in the
     * current chunk. If the min heap and tgt matches, we search for the next
     * min. Once the min heap is exhausted and all the tgts can be satisfied,
     * we have found the smallest chunk so far. Then we move on for the next
     * smallest chunk.
     *
     * O(N^2logN), 0 ms, faster than 100.00%
     */
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    int res = 0;
    int tgt = 0;
    for (int a : arr) {
      pq.push(a);
      while (!pq.empty() && pq.top() == tgt) {
        pq.pop();
        tgt++;
      }
      if (pq.empty()) {
        res++;
      }
    }
    return res;
  }
};

class Solution2 {
public:
  int maxChunksToSorted(vector<int> &arr) {
    /*
     * This is from the official solution where we compare prefix max and
     * suffix min. If suffix min > prefix max, then we can create a chunk.
     */
    std::vector<int> suf_min(arr.begin(), arr.end());
    for (int i = arr.size() - 2; i >= 0; i--)
      suf_min[i] = std::min(suf_min[i + 1], arr[i]);
    int res = 0;
    int pref_max = 0;
    for (int i = 0; i < arr.size() - 1; i++) {
      pref_max = std::max(pref_max, arr[i]);
      if (pref_max < suf_min[i + 1])
        res++;
    }
    return res + 1; // always include the chunk that ends with the last number
  }
};

class Solution3 {
public:
  int maxChunksToSorted(vector<int> &arr) {
    /*
     * This is the prefix sum solution from the official.
     */
    int tgt_sum = 0, pref_sum = 0, res = 0;
    for (int i = 0; i < arr.size(); i++) {
      tgt_sum += i;
      pref_sum += arr[i];
      if (tgt_sum == pref_sum)
        res++;
    }
    return res;
  }
};

class Solution4 {
public:
  int maxChunksToSorted(vector<int> &arr) {
    /*
     * This is the min-max solution NOT read from the official solution, but
     * inspired by thinking about montonotic increasing stack. We basically
     * keep a prefix min and prefix max. If the prefix min = 0 and prefix max
     * = the current index, we can guarantee that a chunk has been formed.
     */
    int pref_min = arr.size(), pref_max = 0;
    int res = 0;
    for (int i = 0; i < arr.size(); i++) {
      pref_min = std::min(pref_min, arr[i]);
      pref_max = std::max(pref_max, arr[i]);
      if (pref_min == 0 && pref_max == i)
        res++;
    }
    return res;
  }
};

class Solution5 {
public:
  int maxChunksToSorted(vector<int> &arr) {
    /*
     * This is essentially the same as Solution4, except that we don't have to
     * keep track of prefix min.
     */
    int pref_max = 0, res = 0;
    for (int i = 0; i < arr.size(); i++) {
      pref_max = std::max(pref_max, arr[i]);
      if (pref_max == i)
        res++;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
