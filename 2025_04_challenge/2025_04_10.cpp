#include <cmath>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
private:
  long long add(long long x, long long y, int base) {}

public:
  long long numberOfPowerfulInt(long long start, long long finish, int limit,
                                string s) {
    /*
     * LeetCode 2999
     *
     * I did not solve this problem in time when it was first announced during
     * the daily challenge, but I had an idea and now let's see if the idea
     * works.
     *
     * We first find the smallest number, with s as its suffix, that is not
     * smaller than start. And find the largest number, with s as its suffix,
     * that is not bigger than finish. And all the numbers must be within the
     * given limit.
     *
     * Once the smallest and biggest numbers have been found, we can directly
     * find the gap between the two, excluding the suffix. We will have to
     * do the subtraction under a base determined by limit. For example, if
     * limit = 4, then 123 - 4 = 113
     */
    long long suf10s = (long long)(std::pow(10, s.size()));
    // find the smallest number that is no smaller than start, and extract its
    // prefix
    long long sufnum = std::stoi(s);
    long long small_prefix = 0;
    if (start > sufnum) {
      long long start_prefix = start / suf10s;
      if (start_prefix * suf10s + sufnum >= start) {
        small_prefix = start_prefix;
      } else {
        small_prefix = add(start_prefix, 1, limit);
      }
    }
    // find the largest number that is no bigger than finish, and extract its
    // prefix
    long long large_prefix = 0;
    if (finish > sufnum) {
      long long finish_prefix = finish / suf10s;
      if (finish_prefix * suf10s + sufnum <= finish) {
        large_prefix = finish_prefix;
      } else {
        large_prefix = add(finish_prefix, -1, limit);
      }
    }
    return add(large_prefix, -small_prefix, limit) + 1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
