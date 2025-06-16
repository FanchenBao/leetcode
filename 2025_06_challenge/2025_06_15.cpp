#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int maxDiff(int num) {
    /*
     * LeetCode 1432
     *
     * The largest is easy to find. Just replace the first non-nine digit to
     * nine, and we are done.
     *
     * The smallest is a bit more tricky to find, since we do not allow leading
     * zeros. If the first digit is 1, we are free to use zero to replace the
     * next non-zero and non-one digit. Otherwise, we have to replace the first
     * digit with 1.
     *
     * 0 ms
     */
    std::string a = std::to_string(num);
    std::string b = a;
    int idx = a.find_first_not_of('9');
    if (idx != std::string::npos)
      std::replace(a.begin(), a.end(), (char)a[idx], '9');
    if (b[0] == '1') {
      // since we cannot turn the first digit to zero, we need to find, among
      // the remainig digits, what is the first non-zero and non-one digit.
      idx = 1;
      while (idx < b.size() && b[idx] <= '1')
        idx++;
      if (idx < b.size())
        std::replace(b.begin(), b.end(), (char)b[idx], '0');
    } else {
      // first digit is not 1, then we have no choice but to replace all its
      // occurrence with 1.
      std::replace(b.begin(), b.end(), (char)b[0], '1');
    }
    return std::stoi(a) - std::stoi(b);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
