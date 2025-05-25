#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findWordsContaining(vector<string> &words, char x) {
    /*
     * LeetCode 2942
     *
     * O(N)
     */
    std::vector<int> res;
    for (int i = 0; i < words.size(); i++) {
      if (words[i].find(x) != std::string::npos)
        res.push_back(i);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
