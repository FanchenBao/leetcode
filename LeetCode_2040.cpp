#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long kthSmallestProduct(vector<int> &nums1, vector<int> &nums2,
                               long long k) {
    /*
     * This solution is inspired by the hints and the initial part of the
     * editorial. Note that it is not inspired by the official solution itself.
     *
     * We divide nums1 and nums2 into three parts each: negatives, zeros, and
     * positives. We store all the negatives as their absolute values. All of
     * the numbers will be sorted within their own division.
     *
     * Then we do binary search for the target product. Suppose the target
     * product is mid, we need to find the number of products that are smaller
     * or equal to mid. If the count is smaller than k, we need to make mid
     * bigger. Otherwise, we make mid smaller.
     *
     * When counting, if mid is positive, we can easily find the total count of
     * negative products and zeros; they are all smaller. Similarly, if mid is
     * negative, we only need to find the count among the products between a
     * positive and negative values.
     *
     * O(N(logN)^2), the outer logN is the overall binary search, whereas the
     * inner logN is the binary search to find the count.
     */
    std::vector<int> pos1, pos2, neg1, neg2;
    int zero1 = 0, zero2 = 0;
    for (int n : nums1) {
      if (n == 0)
        zero1++;
      else if (n < 0)
        neg1.push_back(std::abs(n));
      else
        pos1.push_back(n);
    }
    for (int n : nums2) {
      if (n == 0)
        zero2++;
      else if (n < 0)
        neg2.push_back(std::abs(n));
      else
        pos2.push_back(n);
    }
    std::sort(pos1.begin(), pos1.end());
    std::sort(neg1.begin(), neg1.end());
    std::sort(pos2.begin(), pos2.end());
    std::sort(neg2.begin(), neg2.end());

    long long lo = -10000000000, hi = 10000000001;
    long long neg_prod_cnt =
        pos1.size() * neg2.size() + pos2.size() * neg1.size();
    long long pos_prod_cnt =
        pos1.size() * pos2.size() + neg1.size() * neg2.size();
    long long zero_prod_cnt = zero1 * nums2.size() + zero2 * nums1.size();
    while (lo < hi) {
      long long mid = lo + (hi - lo) / 2;
      long long cnt = 0;
      if (mid > 0) {
        cnt += neg_prod_cnt + zero_prod_cnt;
        for (int p1 : pos1) {
          auto it = std::upper_bound(pos2.begin(), pos2.end(), mid / p1);
          if (it == pos2.begin())
            break;
          cnt += (long long)std::distance(pos2.begin(), it);
        }
        for (int n1 : neg1) {
          auto it = std::upper_bound(neg2.begin(), neg2.end(), mid / n1);
          if (it == neg2.begin())
            break;
          cnt += (long long)std::distance(neg2.begin(), it);
        }
      } else if (mid < 0) {
        for (int i = pos1.size() - 1; i >= 0; i--) {
          auto it = std::lower_bound(neg2.begin(), neg2.end(),
                                     std::ceil(-mid / (float)pos1[i]));
          if (it == neg2.end())
            break;
          cnt += (long long)std::distance(it, neg2.end());
        }
        for (int i = pos2.size() - 1; i >= 0; i--) {
          auto it = std::lower_bound(neg1.begin(), neg1.end(),
                                     std::ceil(-mid / (float)pos2[i]));
          if (it == neg1.end())
            break;
          cnt += (long long)std::distance(it, neg1.end());
        }
      } else {
        // mid == 0
        cnt += neg_prod_cnt + zero_prod_cnt;
      }
      if (cnt >= k) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }
};

int main() {
  std::vector<int> nums1{-2, -1, 0, 1, 2};
  std::vector<int> nums2{-3, -1, 2, 4, 5};
  int k = 3;
  Solution sol;
  std::cout << sol.kthSmallestProduct(nums1, nums2, k) << std::endl;
}
