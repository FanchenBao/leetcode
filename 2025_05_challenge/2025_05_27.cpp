#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int differenceOfSums(int n, int m) {
    /*
     * LeetCode 2894
     *
     * Let k = n / m, then num2 = (1 + k)k / 2 * m
     *
     * Total sum = (1 + n)n / 2
     *
     * Since num1 = sum - num2, we have num1 - num2 = sum - 2(num2)
     * = (1 + n)n / 2 - mk(1 + k)
     *
     * O(1)
     */
    int k = n / m;
    return (1 + n) * n / 2 - m * k * (1 + k);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
