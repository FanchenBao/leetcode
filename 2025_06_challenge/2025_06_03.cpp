#include <deque>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxCandies(vector<int> &status, vector<int> &candies,
                 vector<vector<int>> &keys, vector<vector<int>> &containedBoxes,
                 vector<int> &initialBoxes) {
    /*
     * LeetCode 1298
     *
     * Follow the instruction and use BFS.
     *
     * O(N^2), 0 ms
     */
    std::deque<int> opened; // only contains available and opened boxes
    std::deque<int> closed; // only contains available but unopened boxes.
    int res = 0;
    for (int b : initialBoxes) {
      if (status[b] == 1)
        opened.push_back(b);
      else
        closed.push_back(b);
    }
    while (!opened.empty()) {
      int b = opened.front();
      opened.pop_front();
      // accumulate candies
      res += candies[b];
      // update the status of opened boxes
      for (int k : keys[b])
        status[k] = 1;
      // if a box becomes open, move it from closed to open
      int closed_size = closed.size();
      for (int i = 0; i < closed_size; i++) {
        int c = closed.front();
        closed.pop_front();
        if (status[c] == 1)
          opened.push_back(c);
        else
          closed.push_back(c);
      }
      // add new boxes to open or closed based on their status
      for (int cb : containedBoxes[b]) {
        if (status[cb] == 1)
          opened.push_back(cb);
        else
          closed.push_back(cb);
      }
    }
    return res;
  }
};

class Solution2 {
public:
  int maxCandies(vector<int> &status, vector<int> &candies,
                 vector<vector<int>> &keys, vector<vector<int>> &containedBoxes,
                 vector<int> &initialBoxes) {
    /*
     * This solution is inspired by the editorial. We don't have to keep a
     * separate queue to keep track of available but unopened boxes. We just
     * need to keep track of what boxes are available to us. Then when a new
     * key is obtained, we check the available list to see if the box can be
j    * obtained. Similarly, when we get new boxes, we check the kesy to see if
     * it can be obtained.
     *
     * O(N) 10 ms.
     */
    std::deque<int> opened; // only contains available and opened boxes
    std::vector<bool> owned(status.size(), false);
    int res = 0;
    for (int b : initialBoxes) {
      if (status[b] == 1)
        opened.push_back(b);
      owned[b] = true;
    }
    while (!opened.empty()) {
      int b = opened.front();
      opened.pop_front();
      // accumulate candies
      res += candies[b];
      // If a box can be opened, check if we own it already. If so, add it to
      // the opened queue.
      for (int k : keys[b]) {
        if (owned[k] && status[k] == 0)
          opened.push_back(k);
        status[k] = 1;
      }
      // If a box is owned, check if it can be opened already. If so, add it
      // to the opened queue.
      for (int cb : containedBoxes[b]) {
        if (!owned[cb] && status[cb] == 1)
          opened.push_back(cb);
        owned[cb] = true;
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
