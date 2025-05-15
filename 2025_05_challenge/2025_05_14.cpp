#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int lengthAfterTransformations(string s, int t, vector<int> &nums) {
    /*
     * LeetCode 3337
     *
     * I am going to try the same method as suggested by the editorial the
     * day before. The only difference is that instead of transforming each
     * letter by one position, we need to do another loop to obtain the number
     * of positions of transformation.
     *
     * The total runtime can be O(26 * 26 * N). I hope it will still be within
     * the limit.
     *
     * Unfortunately, this solution TLE.
     *
     */
    long long MOD = 1000000007;
    std::vector<long long> counter(26);
    for (char c : s)
      counter[c - 'a']++;
    for (int i = 0; i < t; i++) {
      std::vector<long long> tmp(26);
      for (int j = 0; j < 26; j++) {
        if (counter[j] == 0)
          continue;
        for (int k = 1; k <= nums[j]; k++) {
          int idx = (j + k) % 26;
          tmp[idx] = (tmp[idx] + counter[j]) % MOD;
        }
      }
      counter = std::move(tmp);
    }
    long long res = 0;
    for (long long c : counter)
      res = (res + c) % MOD;
    return res;
  }
};

static constexpr int N = 26;
static constexpr int MOD = 1000000007;

class Mat {
public:
  Mat(int default_ = 0) {
    std::vector<std::vector<int>> tmp(N, std::vector<int>(N, default_));
    mat_ = std::move(tmp);
  };

  Mat &operator=(const Mat &other) {
    // assignment constructor
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++)
        mat_[i][j] = other.mat_[i][j];
    }
    return *this;
  };
  std::vector<std::vector<int>> mat_;
};

Mat operator*(const Mat &a, const Mat &b) {
  Mat res;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        res.mat_[i][j] =
            (res.mat_[i][j] + (long long)a.mat_[i][k] * b.mat_[k][j]) % MOD;
      }
    }
  }
  return res;
}

Mat I() {
  // identity matrix
  Mat I;
  for (int i = 0; i < N; i++) {
    I.mat_[i][i] = 1;
  }
  return I;
}

Mat exp(const Mat &a, int q) {
  Mat res = I(), cur = a;
  while (q > 0) {
    if (q % 2 == 1) {
      res = res * cur;
    }
    cur = cur * cur;
    q /= 2;
  }
  return res;
}

class Solution2 {
public:
  int lengthAfterTransformations(string s, int t, vector<int> &nums) {
    /*
     * Follow the editorial. Given a counter where counter[i] is the number of
     * instances for letter 'a' + i, we create a matrix such that mat[i][j] is
     * 1 if there exists a transformation from 'a' + j tp 'a' + i.
     *
     * Then for row mat[i], when we do mat[i] X counter, we obtain the total
     * number of 'a' + i after all the eligible letters  transform to 'a' + i.
     *
     * We keep doing this for t times, which essentially means we take the t
     * power of mat. The final counter is the result of the exponentiation of
     * mat, multiplied by counter.
     *
     * 320 ms, 60%
     */
    Mat T;
    for (int i = 0; i < N; i++) {
      for (int j = 1; j <= nums[i]; j++) {
        T.mat_[(i + j) % N][i] = 1;
      }
    }
    T = exp(T, t);
    std::vector<int> counter(N);
    for (char c : s)
      counter[c - 'a']++;
    int res = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        res = (res + (long long)T.mat_[i][j] * counter[j]) % MOD;
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
