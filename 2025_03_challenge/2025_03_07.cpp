#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  std::vector<int> get_primes(int upper_bound) {
    std::vector<int> sieves = std::vector<int>(upper_bound + 1, 1);
    sieves[0] = 0, sieves[1] = 0;
    for (int i = 2; i <= upper_bound; i += 2)
      sieves[i] = 0;
    for (int i = 3; i + i <= upper_bound; i += 2) {
      for (int j = i + i; j <= upper_bound; j += i)
        sieves[j] = 0;
    }
    std::vector<int> primes{2};
    for (int i = 3; i <= upper_bound; i += 2) {
      if (sieves[i] == 1)
        primes.push_back(i);
    }
    return primes;
  }

public:
  vector<int> closestPrimes(int left, int right) {
    /*
     * LeetCode 2532
     *
     * Use Eratosthenes Sieve to find all the primes. And then binary search
     * the range to find the pair with the smallest difference.
     *
     * 359 ms, 28.15%
     */
    std::vector<int> primes = get_primes(right);
    auto lit = std::lower_bound(primes.begin(), primes.end(), left);
    auto rit = std::upper_bound(primes.begin(), primes.end(), right);
    int lo = lit - primes.begin(), hi = rit - primes.begin() - 1;
    std::vector<int> res{0, 10000000};
    if (hi - lo + 1 < 2) {
      res[0] = -1, res[1] = -1;
      return res;
    }
    for (int i = lo; i + 1 <= hi; i++) {
      if (primes[i + 1] - primes[i] < res[1] - res[0]) {
        res[0] = primes[i];
        res[1] = primes[i + 1];
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
