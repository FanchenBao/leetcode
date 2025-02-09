#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class NumberContainers {
private:
  std::unordered_map<int, int> idx_to_num;
  std::unordered_map<int, std::priority_queue<int>> num_to_idx;

public:
  /*
   * LeetCode 2349
   *
   * Use a map<int, heap> to keep track of each number's indices. Top of the
   * heap is the smallest index. However, to make sure that the index does
   * point to the number of interest, we use another array to keep track of
   * what number is at which index.
   *
   * 73 ms, 97.19%
   */
  NumberContainers() {}

  void change(int index, int number) {
    idx_to_num[index] = number;
    num_to_idx[number].push(-index);
  }

  int find(int number) {
    while (!num_to_idx[number].empty()) {
      int i = -num_to_idx[number].top();
      if (idx_to_num[i] != number)
        num_to_idx[number].pop();
      else
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
