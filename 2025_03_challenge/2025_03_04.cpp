#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool checkPowersOfThree(int n) {
    /*
     * LeetCode 1780
     *
     * This is equivalent of finding the binary representation of an integer,
     * except that now we want to find the trinary representation. For an
     * integer to be representable by trinary, its MOD 3 must be either 0 or 1.
     * Whenever it is 2, it is not possible to find a trinary representation.
     *
     * 0 ms.
     */
    while (n > 0) {
      if (n % 3 == 2)
        return false;
      n /= 3;
    }
    return true;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
