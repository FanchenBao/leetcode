#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumDeletions(string word, int k) {
    /*
     * LeetCode 3085
     *
     * Find the frequencies of all letters, sort it, and then go through the
     * frequencies from small to large. For each frequency, we assume that it
     * is the smallest after the removal, then we count how many removals are
     * needed to satisfy the constraint. We find the smallest of the removals.
     *
     * O(N), 8 ms, 56%
     */
    std::vector<int> freq(26);
    for (char c : word)
      freq[c - 'a']++;
    std::sort(freq.begin(), freq.end());
    int presum = 0, res = word.size() + 1;
    for (int i = 0; i < 26; i++) {
      if (freq[i] == 0)
        continue;
      int removals = presum;
      for (int j = i + 1; j < 26; j++)
        removals += std::max(0, freq[j] - (freq[i] + k));
      res = std::min(res, removals);
      presum += freq[i];
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
