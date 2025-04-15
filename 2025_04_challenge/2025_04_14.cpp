#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countGoodTriplets(vector<int> &arr, int a, int b, int c) {
    /*
     * LeetCode 1534
     *
     * Brute force. Can't think of a better way at the moment.
     *
     * O(N^3), 6 ms, 78.59%
     */
    int res = 0;
    for (int i = 0; i < arr.size(); i++) {
      for (int j = i + 1; j < arr.size(); j++) {
        if (std::abs(arr[i] - arr[j]) <= a) {
          for (int k = j + 1; k < arr.size(); k++) {
            if (std::abs(arr[j] - arr[k]) <= b &&
                std::abs(arr[i] - arr[k]) <= c)
              res++;
          }
        }
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
