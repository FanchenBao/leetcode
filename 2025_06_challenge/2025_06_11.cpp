#include <climits>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxDifference(string s, int k) {
    /*
     * LeetCode 3445 (Fail)
     *
     * This one is very tough. The editorial is good, and we are following
     * its solution.
     *
     * Basically, since the total number of unique characters in s is very
     * small, we will try all combinations of unique pairs.
     *
     * For each combination (a, b), we denote a to have odd count and b even
     * count.
     *
     * We also keep track of the prefix count of a and b. The key point is to
     * have two versions of the prefix count based on two pointers lo and hi.
     * The substring we are interested in is s[lo + 1:hi + 1]. To find out
     * the count of a and b in the substring, we need prefix count (pc) for
     * the hi pointer for a (pc_hi_a), pc_lo_a, pc_hi_b, and pc_lo_b. Then
     * the difference is computed as
     *
     * (pc_hi_a - pc_lo_a) - (pc_hi_b - pc_lo_b)
     * = (pc_hi_a - pc_hi_b) - (pc_lo_a - pc_lo_b)
     *
     * This means we can do two pointers and find the difference between the
     * prefix count in a and b for position hi, and that for position lo.
     * And to make the difference maximum, we need the prefix count diff for
     * position lo to be minimum. This we can do because as lo moves to the
     * right, we can always keep track of the minimum prefix count diff.
     *
     * The next hurdle is to decide which hi can map to which lo. This is
     * determined by the parity. For the prefix sum at each position, there
     * are four possible parity combinations: 00, 01, 10, 11. If the parity
     * state of hi is 00, then the matching parity state of lo has to be 10.
     * Similarly, if the parity state of hi is 01, then the matching parity
     * state of lo has to be 11.
     *
     * In other words, parity_lo = parity_hi ^ 2
     *
     * Therefore, we keep track of the min pc_lo_a - pc_lo_b for each parity
     * state. And for each pc_hi_a - pc_hi_b, we use the min lo with the
     * matching parity.
     *
     * Finally, there is the problem of when lo can proceed. We need to
     * proceed lo to find the minimums for each parity, but lo cannot proceed
     * if the size of the substring (i.e., hi - lo) is smaller than k, or
     * if the count of b (i.e., pc_hi_b - pc_lo_b) is smaller than 2 (this is
     * to guarantee that there are at least even number of b's).
     */
    auto get_par = [](int c1, int c2) { return (c1 & 1) * 2 + (c2 & 1); };

    int res = INT_MIN;
    for (char a = '0'; a <= '4'; a++) {
      for (int b = '0'; b <= '4'; b++) {
        if (a == b)
          continue;
        int lo = -1;
        int pc_lo_a = 0, pc_lo_b = 0, pc_hi_a = 0, pc_hi_b = 0;
        std::vector<int> min_lo(4);
        for (int idx = 0; idx < 4; idx++)
          min_lo[idx] = s.size() + 1;
        for (int hi = 0; hi < s.size(); hi++) {
          pc_hi_a += (int)(s[hi] == a);
          pc_hi_b += (int)(s[hi] == b);
          while (hi - lo >= k && pc_hi_b - pc_lo_b >= 2) {
            if (lo >= 0) {
              pc_lo_a += (int)(s[lo] == a);
              pc_lo_b += (int)(s[lo] == b);
            }
            int p_lo = get_par(pc_lo_a, pc_lo_b);
            min_lo[p_lo] = std::min(min_lo[p_lo], pc_lo_a - pc_lo_b);
            lo++;
          }
          if (pc_hi_a > 0 && pc_hi_b > 0) {
            int p_hi = get_par(pc_hi_a, pc_hi_b);
            res = std::max(res, pc_hi_a - pc_hi_b - min_lo[p_hi ^ 2]);
          }
        }
      }
    }
    return res;
  }
};

int main() {
  std::string s = "12233";
  int k = 4;
  Solution sol;
  std::cout << sol.maxDifference(s, k) << std::endl;
}
