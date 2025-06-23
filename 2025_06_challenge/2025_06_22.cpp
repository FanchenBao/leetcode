#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution1 {
public:
  vector<string> divideString(string s, int k, char fill) {
    /*
     * LeetCode 2138
     *
     * 1 ms, 22%
     */
    std::vector<std::string> res;
    for (int i = 0; i < s.size(); i += k)
      res.push_back(s.substr(i, k));
    if (res[res.size() - 1].size() < k)
      res[res.size() - 1] =
          res[res.size() - 1].append(k - res[res.size() - 1].size(), fill);
    return res;
  }
};

class Solution2 {
public:
  vector<string> divideString(string s, int k, char fill) {
    /*
     * 0 ms
     */
    std::vector<std::string> res;
    int r = s.size() % k;
    int num_to_add = r > 0 ? k - r : 0;
    s.append(num_to_add, fill);
    for (int i = 0; i < s.size(); i += k)
      res.push_back(s.substr(i, k));
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
