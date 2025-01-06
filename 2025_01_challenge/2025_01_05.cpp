#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string shiftingLetters(string s, vector<vector<int>> &shifts) {
    /*
     * LeetCode 2381
     *
     * Break the shifts into start and end + 1. If shift back, start has -1 and
     * end + 1 has +1; if shift forward, start has +1 and end + 1 has -1.
     *
     * Sort the individual shifts and use two pointers, one for the individual
     * shifts and the other for s. For each index in s, we first compute all
     * the shifts that needed on it from the individual shifts. We progress
     * the individual shifts once the index in s is equal to the front the
     * the individual shifts.
     *
     * O(NlogN + M + N), where N = len(shifts) and M = len(s). 210 ms, 7.80%
     */
    std::vector<std::vector<int>> ind_shifts;
    for (auto shift : shifts) {
      ind_shifts.push_back(std::vector<int>{shift[0], shift[2] == 0 ? -1 : 1});
      ind_shifts.push_back(
          std::vector<int>{shift[1] + 1, shift[2] == 0 ? 1 : -1});
    }
    std::sort(ind_shifts.begin(), ind_shifts.end());
    int i = 0, cur_shifts = 0;
    for (int j = 0; j < s.size(); j++) {
      while (i < ind_shifts.size() && j == ind_shifts[i][0]) {
        cur_shifts += ind_shifts[i][1];
        i++;
      }
      s[j] = (char)(((s[j] - 'a' + cur_shifts) % 26 + 26) % 26 + 'a');
    }
    return s;
  }
};

class Solution2 {
public:
  string shiftingLetters(string s, vector<vector<int>> &shifts) {
    /*
     * This is from the official solution. It uses the same idea as solution1,
     * but with a much faster implementation. Instead of creating an array of
     * array and sort it, this solution creates an array that considers all
     * the indices of s. We accumulate the shift changes on the additional
     * array and use prefix sum to aggregate the total shifts for each position.
     *
     * O(M + N), 38 ms, 43.67%
     */
    std::vector<int> shift_diffs(s.size() + 1);
    for (auto shift : shifts) {
      shift_diffs[shift[0]] += shift[2] == 0 ? -1 : 1;
      shift_diffs[shift[1] + 1] += shift[2] == 0 ? 1 : -1;
    }
    int cur_shifts = 0;
    for (int i = 0; i < s.size(); i++) {
      cur_shifts += shift_diffs[i];
      s[i] = ((s[i] - 'a' + cur_shifts) % 26 + 26) % 26 + 'a';
    }
    return s;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
