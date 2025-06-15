#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int get_swapped_number(std::string num_str, int swap_from, int swap_to) {
    int res = 0;
    for (char c : num_str) {
      int d = (c - '0' == swap_from) ? swap_to : c - '0';
      res = res * 10 + d;
    }
    return res;
  }
  int minMaxDifference(int num) {
    /*
     * LeetCode 2566
     */
    std::string num_str = std::to_string(num);
    int max_swap = -1;
    for (char d : num_str) {
      if (d != '9') {
        max_swap = d - '0';
        break;
      }
    }
    int min_swap = num_str[0] - '0';
    return get_swapped_number(num_str, max_swap, 9) -
           get_swapped_number(num_str, min_swap, 0);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
