#include <iostream>
#include <set>
#include <sstream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  std::vector<int> ALL_DIGITS{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  std::vector<std::vector<int>> END_DIGITS{
      {},           {1, 2, 3, 4, 5, 6, 7, 8, 9},
      {2, 4, 6, 8}, {1, 2, 3, 4, 5, 6, 7, 8, 9},
      {2, 4, 6, 8}, {5},
      {2, 4, 6, 8}, {1, 2, 3, 4, 5, 6, 7, 8, 9},
      {2, 4, 6, 8}, {1, 2, 3, 4, 5, 6, 7, 8, 9}};
  std::unordered_set<long long> SEEN;

  long long get_num(std::vector<int> &digits) {
    long long num = 0;
    for (int d : digits)
      num = num * 10 + d;
    return num;
  }

  std::vector<int> get_counter(std::vector<int> &digits) {
    std::vector<int> counter(10);
    for (int d : digits)
      counter[d]++;
    return counter;
  }

  bool has_seen(std::vector<int> &palindrome) {
    std::vector<int> cp = palindrome;
    std::sort(cp.begin(), cp.end());
    long long num = get_num(cp);
    if (SEEN.contains(num))
      return true;
    SEEN.insert(num);
    return false;
  }

  long long comb(int n, int k) {
    long long num = 1, den = 1;
    for (int i = n - k + 1; i <= n; i++)
      num *= i;
    for (int i = 1; i <= k; i++)
      den *= i;
    return num / den;
  }

  long long num_perm(std::vector<int> &counter, int n) {
    long long total = 1;
    for (int d = 0; d < 10; d++) {
      int k = counter[d];
      if (k > 0) {
        total *= comb(n, k);
        n -= k;
      }
    }
    return total;
  }

  long long dfs(std::vector<int> &palindrome, int idx, int k) {
    int n = palindrome.size();
    long long total = 0;
    if (idx >= (n + 1) / 2) {
      // the palindrome has been formed
      long long num = get_num(palindrome);
      if (num % k == 0 && !has_seen(palindrome)) {

        std::vector<int> counter = get_counter(palindrome);
        total = num_perm(counter, n);
        if (counter[0] > 0) {
          // remove all the permutations that start with 0
          counter[0]--;
          total -= num_perm(counter, n - 1);
        }
        return total;
      }
      return 0;
    }
    std::vector<int> digits;
    if (idx == 0)
      digits = END_DIGITS[k];
    else
      digits = ALL_DIGITS;
    for (int d : digits) {
      palindrome[idx] = d;
      palindrome[n - idx - 1] = d;
      total += dfs(palindrome, idx + 1, k);
    }
    return total;
  }

  long long countGoodIntegers(int n, int k) {
    /*
     * LeetCode 3272
     *
     * We will first use DFS to find all the palindromes given the length n
     * and the divisor k. Then for each valid and unique palindrome, we will
     * find the number of unique permutations.
     *
     * 298 ms, 65%
     */
    std::vector<int> palindrome(n);
    return dfs(palindrome, 0, k);
  }
};

int main() {
  int n = 4, k = 4;
  Solution sol;
  std::cout << sol.countGoodIntegers(n, k) << std::endl;
}
