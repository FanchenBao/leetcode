#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool threeConsecutiveOdds(vector<int> &arr) {
    /*
     * LeetCode 1550
     */
    int cnt = 0;
    for (int a : arr) {
      if (a % 2 == 1) {
        cnt++;
        if (cnt == 3)
          return true;
      } else {
        cnt = 0;
      }
    }
    return false;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
