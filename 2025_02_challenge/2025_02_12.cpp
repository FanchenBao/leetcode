#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int get_digit_sum(int n) {
    int s = 0;
    while (n > 0) {
      s += n % 10;
      n /= 10;
    }
    return s;
  }

  int maximumSum(vector<int> &nums) {
    /*
     * LeetCode 2342
     *
     * Find the max and second-max numbers with the same digit sum. Compute
     * the max sum of the pair.
     *
     * O(N), 31 ms, 46.93%
     */
    std::unordered_map<int, std::vector<int>>
        ds_map; // digit sum map. The value is a vector of size two [max,
                // submax]
    for (int n : nums) {
      int ds = get_digit_sum(n);
      if (ds_map[ds].empty()) {
        ds_map[ds].push_back(n);
      } else if (ds_map[ds].size() == 1) {
        if (ds_map[ds][0] >= n) {
          ds_map[ds].push_back(n);
        } else {
          ds_map[ds].push_back(ds_map[ds][0]);
          ds_map[ds][0] = n;
        }
      } else {
        if (n > ds_map[ds][0]) {
          ds_map[ds][1] = ds_map[ds][0];
          ds_map[ds][0] = n;
        } else if (n > ds_map[ds][1]) {
          ds_map[ds][1] = n;
        }
      }
    }
    int res = -1;
    for (auto const &p : ds_map) {
      if (p.second.size() == 2)
        res = std::max(res, p.second[0] + p.second[1]);
    }
    return res;
  }
};

class Solution2 {
public:
  int get_digit_sum(int n) {
    int s = 0;
    while (n > 0) {
      s += n % 10;
      n /= 10;
    }
    return s;
  }

  int maximumSum(vector<int> &nums) {
    /*
     * LeetCode 2342
     *
     * Find the max and second-max numbers with the same digit sum. Compute
     * the max sum of the pair.
     *
     * O(N), 5 ms, 96.25%
     */
    std::vector<std::vector<int>> ds_map(
        82,
        std::vector<int>(2, -1000000001)); // digit sum map. The value is a
                                           // vector of size two [max, submax]
    for (int n : nums) {
      int ds = get_digit_sum(n);
      if (n > ds_map[ds][0]) {
        ds_map[ds][1] = ds_map[ds][0];
        ds_map[ds][0] = n;
      } else if (n > ds_map[ds][1]) {
        ds_map[ds][1] = n;
      }
    }
    int res = -1;
    for (auto const &max_submax : ds_map) {
      res = std::max(res, max_submax[0] + max_submax[1]);
    }
    return res <= 0 ? -1 : res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
