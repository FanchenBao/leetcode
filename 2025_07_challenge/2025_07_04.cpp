#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int findLucky(vector<int> &arr) {
    /*
     * LeetCode 1394
     */
    std::vector<int> counter(501);
    for (int a : arr)
      counter[a]++;
    for (int i = 500; i > 0; i--) {
      if (counter[i] == i)
        return i;
    }
    return -1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
