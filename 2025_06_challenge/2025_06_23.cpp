#include <algorithm>
#include <cmath>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool IsPalindrome(long long num) {
    std::string num_str = std::to_string(num);
    std::string reversed = num_str;
    std::reverse(reversed.begin(), reversed.end());
    return num_str == reversed;
  }

  long long kMirror(int k, int n) {
    /*
     * LeetCode 2081
     *
     * It should be faster to go through all the k-base mirror numbers,
     * because they are basically palindromes.
     *
     * We will create memory of previously produced k-base mirror numbers with
     * lower number of digits, and use them to produce k-base mirror numbers
     * with higher digits. For example, if we have two-digit k-base mirror
     * number 11, then we can produce a four-digit k-base mirror number based
     * off 11 as 0110 (not counted towards the result, but we need it to
     * build the base), 1111, 2112, 3113, etc.
     *
     * As we go through the k-base mirror numbers in order, we check whether
     * their 10-base number also has palindrome digits.
     *
     * 322 ms, 58.77%
     */
    long long res = 0;
    std::vector<std::vector<std::vector<long long>>> memo(k);
    for (int i = 0; i < k; i++)
      memo[i].push_back({}); // this is the dummy for zero number of digits
    int num_d = 1;
    while (n > 0) {
      for (int d = 0; d < k; d++) {
        memo[d].push_back({});
        if (num_d == 1) {
          long long val = (long long)d;
          memo[d][num_d].push_back(val);
          if (d > 0) {
            res += val;
            n--;
            if (n == 0)
              break;
          }
        } else if (num_d == 2) {
          long long val = (long long)(d + d * k);
          memo[d][num_d].push_back(val);
          if (d > 0 && IsPalindrome(val)) {
            res += val;
            n--;
            if (n == 0)
              break;
          }
        } else { // more than two digits
          for (int pre_d = 0; pre_d < k && n > 0; pre_d++) {
            for (long long pre : memo[pre_d][num_d - 2]) {
              // put the current digit on both sides of the previously
              // configured number in memo
              long long val =
                  (long long)(d + d * (long long)pow(k, num_d - 1) + pre * k);
              memo[d][num_d].push_back(val);
              if (d > 0 && IsPalindrome(val)) {
                res += val;
                n--;
                if (n == 0)
                  break;
              }
            }
          }
        }
      }
      num_d++;
    }
    return res;
  }
};

int main() {
  int k = 2;
  int n = 5;
  Solution sol;
  std::cout << sol.kMirror(k, n) << std::endl;
}
