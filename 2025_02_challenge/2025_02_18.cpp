#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool backtrack(int idx, std::string &pat, std::vector<int> &arr,
                 std::vector<bool> &seen) {
    if (idx == arr.size())
      return true;
    if (arr[idx] > 0)
      return backtrack(idx + 1, pat, arr, seen);
    for (int c = 1; c < seen.size(); c++) {
      if (!seen[c] &&
          (idx == 0 || ((pat[idx - 1] == 'I' && c > arr[idx - 1]) ||
                        (pat[idx - 1] == 'D' && c < arr[idx - 1])))) {
        seen[c] = true;
        arr[idx] = c;
        if (backtrack(idx + 1, pat, arr, seen))
          return true;
        // backtrack
        seen[c] = false;
        arr[idx] = 0;
      }
    }
    return false;
  }

  string smallestNumber(string pattern) {
    /*
     * LeetCode 2375
     *
     * Backtracking. O(N!)
     */
    std::vector<int> arr(pattern.size() + 1);
    std::vector<bool> seen(pattern.size() + 2);
    backtrack(0, pattern, arr, seen);
    std::string res;
    for (int a : arr)
      res += std::to_string(a);
    return res;
  }
};

class Solution2 {
public:
  string smallestNumber(string pattern) {
    /*
     * This solution is inspired by the editorial.
     *
     * Notice that when we have consecutive I's, we simply increment the digit.
     * When we have consecutive D's, we cannot immediately decide what digit
     * to assign the first D, because it is dependent on the second D, and so
     * on. In this case, we keep moving forward until we hit the next I. This
     * "I" we have a deterministic value, which is the smallest so far. And
     * after filling this I, we can fill the previous D's.
     *
     * We can use stack to do this, but we don't need to physically have a
     * stack. Two pointers shall suffice.
     *
     * O(N)
     */
    std::string new_pat = pattern + "I";
    std::vector<int> arr(new_pat.size());
    int dig = 1;
    for (int i = 0; i < new_pat.size(); i++) {
      if (new_pat[i] == 'I') {
        arr[i] = dig++;
        for (int j = i - 1; j >= 0 && new_pat[j] == 'D'; j--)
          arr[j] = dig++;
      }
    }
    std::string res;
    for (int a : arr)
      res += std::to_string(a);
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
