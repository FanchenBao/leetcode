#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numberOfAlternatingGroups(vector<int> &colors, int k) {
    for (int i = 0; i < k - 1; i++)
      colors.push_back(colors[i]);
    // find consecutive islands
    int res = 0;
    int prehi = 0, lo = -1;
    for (int i = 1; i < colors.size(); i++) {
      if (colors[i] == colors[i - 1]) {
        if (lo < 0)
          lo = i - 1;
      } else if (lo >= 0) {
        res += std::max(lo - prehi - k + 2, 0);
        lo = -1;
        prehi = i - 1;
      }
    }
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
