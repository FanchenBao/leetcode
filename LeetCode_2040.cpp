#include <algorithm>
#include <iostream>
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
    int zero1, zero2;
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

    long long lo = -100000, hi = 100001;
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
        }
      } else if (mid < 0) {
        for (int)
      }
    }
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
