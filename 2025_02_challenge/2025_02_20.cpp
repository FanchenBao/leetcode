#include <bitset>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string findDifferentBinaryString(vector<string> &nums) {
    /*
     * LeetCode 1980
     *
     * Turn nums into a set, and iterate through all possible numbers between
     * 0 and 2^n - 1.
     *
     * Use bitset<16> to convert an integer to its 0-padded binary string.
     *
     * O(N), because nums's size is N. This means we only need to iterate
     * through at most N + 1 values to reach an answer.
     */
    std::set<std::string> seen(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = 0; i <= (1 << n) - 1; i++) {
      std::string bstr = std::bitset<16>(i).to_string().substr(16 - n, n);
      if (!seen.contains(bstr))
        return bstr;
    }
    return ""; // should not hit here
  }
};

class Solution2 {
public:
  string findDifferentBinaryString(vector<string> &nums) {
    /*
     * Using Cantor's diagonal argumnet. We create a binary representation
     * such that the ith bit is different from the ith bit of the ith number.
     */
    std::string res;
    for (int i = 0; i < nums.size(); i++) {
      char c = nums[i][i];
      res += c == '0' ? '1' : '0';
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
