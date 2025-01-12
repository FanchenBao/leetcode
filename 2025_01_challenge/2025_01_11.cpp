#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool canConstruct(string s, int k) {
    /*
     * LeetCode 1400
     *
     * The number of odd frequency letter determines how many palindromes must
     * be formed to use up every letter in s. Thus if this lower bound number
     * is bigger than k, we are not able to form just k palindromes.
     *
     * O(N), 1 ms, 80.42%
     */
    if (s.size() < k)
      return false;
    std::vector<int> freq(26);
    for (char c : s)
      freq[c - 'a']++;
    for (int i = 0; i < 26; i++)
      k -= freq[i] % 2;
    return k >= 0;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
