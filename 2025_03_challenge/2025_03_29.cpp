#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  /* Iterative Function to calculate (x^y)%p in O(log y) */
  // Stolen from
  // https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
  int power(long long x, long long y, int p) {
    int res = 1; // Initialize result
    x = x % p;   // Update x if it is more than or
                 // equal to p
    if (x == 0)
      return 0; // In case x is divisible by p;
    while (y > 0) {
      // If y is odd, multiply x with result
      if (y & 1)
        res = (res * x) % p;
      // y must be even now
      y = y >> 1; // y = y/2
      x = (x * x) % p;
    }
    return res;
  }

  int get_prime_score(int x, std::vector<int> &hash) {
    if (hash[x] >= 0)
      return hash[x];
    int xx = x;
    hash[x] = xx % 2 == 0;
    // remove all 2
    while (xx > 0 && xx % 2 == 0)
      xx /= 2;
    // removal starting from 3
    int p = 3;
    while (p * p < xx) {
      bool is_prime_factor = false;
      while (xx > 0 && xx % p == 0) {
        xx /= p;
        is_prime_factor = true;
      }
      hash[x] += is_prime_factor;
      p += 2;
    }
    hash[x] += xx > 1;
    return hash[x];
  }

  std::vector<int> get_low_bound(std::vector<int> &nums,
                                 std::vector<int> &pscore) {
    int N = nums.size();
    std::vector<int> res(N);
    std::vector<int> mono;
    for (int i = 0; i < N; i++) {
      while (!mono.empty() && pscore[mono[mono.size() - 1]] < pscore[i])
        mono.pop_back();
      res[i] = mono.empty() ? 0 : mono[mono.size() - 1] + 1;
      mono.push_back(i);
    }
    return res;
  }

  std::vector<int> get_high_bound(std::vector<int> &nums,
                                  std::vector<int> &pscore) {
    int N = nums.size();
    std::vector<int> res(N);
    std::vector<int> mono;
    for (int i = N - 1; i >= 0; i--) {
      while (!mono.empty() && pscore[mono[mono.size() - 1]] <= pscore[i])
        mono.pop_back();
      res[i] = mono.empty() ? N - 1 : mono[mono.size() - 1] - 1;
      mono.push_back(i);
    }
    return res;
  }

  int maximumScore(vector<int> &nums, int k) {
    /*
     * LeetCode 2818 (Fail)
     *
     * First of all, obtain the prime scores of each element in nums.
     * Then sort nums along with their indices. Start from the largest number,
     * for each number, we first take by itself, then we try to expand to
     * the right as much as possible. Each expansion is contingent on the
     * expanded number's primer score not bigger than the largest number.
     * Each expansion also cost an operation, but it yields the largest
     * number to the final score.
     *
     * Similarly, we can also expand to the left, but the requirement is all
     * the expansion has prime score strictly smaller than the one of the
     * largest number. It's important to note that when expanding to the left,
     * each successful expansion carries all the expansions to the right.
     *
     * Once all subarrays starting from the
     * largest score is exhausted, we move on to the next largest number.
     *
     * The original idea doesn't work because we kept TLE. I checked the last
     * time when I successfully did this in one shot!! I used monotonic array
     * to find the boundary to the left and right of each number. This can
     * significantly reduce the amount of looping.
     *
     * 283 ms, 73.78%
     */
    int N = nums.size();
    int MOD = 1000000007;
    std::vector<int> hash(100001, -1);
    std::vector<int> pscore;
    std::vector<std::pair<int, int>> sorted_nums;
    for (int i = 0; i < N; i++) {
      pscore.push_back(get_prime_score(nums[i], hash));
      sorted_nums.push_back({nums[i], i});
    }
    std::sort(sorted_nums.begin(), sorted_nums.end(), std::greater<>());
    // Get the boundaries
    std::vector<int> lo_bound = get_low_bound(nums, pscore);
    std::vector<int> hi_bound = get_high_bound(nums, pscore);
    long long res = 1;
    for (int j = 0; j < sorted_nums.size() && k > 0; j++) {
      auto p = sorted_nums[j];
      int v = p.first, i = p.second;
      int cnt_lo = i - lo_bound[i] + 1;
      int cnt_hi = hi_bound[i] - i + 1;
      long long total = (long long)cnt_lo * (long long)cnt_hi;
      long long c = std::min((long long)k, total);
      res = (res * (long long)power(v, c, MOD)) % MOD;
      k -= (int)c;
    }
    return (int)res;
  }
};

int main() {
  std::vector<int> nums{8, 3, 9, 3, 8};
  int k = 2;
  Solution sol;
  std::cout << sol.maximumScore(nums, k) << std::endl;
}
