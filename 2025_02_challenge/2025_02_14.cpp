#include <iostream>
#include <set>
#include <vector>

using namespace std;

class ProductOfNumbers {
  /*
   * LeetCode 1352
   *
   * Use prefix product. However, pay attention to the complication of zeros.
   * If the suffix covers a zero, then the product will always be zero. Thus,
   * we need to keep track of the largest index that is zero.
   *
   * Also, whenever we hit a zero, we assign the value 1 to the prefix product
   * array.
   *
   * 30 ms, 39.84%
   */
public:
  std::vector<int> pprod;
  int max_zero_idx;
  int idx;

  ProductOfNumbers() {
    pprod.push_back(1);
    max_zero_idx = 0;
    idx = 1;
  }

  void add(int num) {
    if (num == 0) {
      max_zero_idx = idx;
      pprod.push_back(1);
    } else {
      pprod.push_back(pprod.back() * num);
    }
    idx++;
  }

  int getProduct(int k) {
    int N = pprod.size();
    if (N - k <= max_zero_idx)
      return 0;
    return pprod.back() / pprod[N - k - 1];
  }
};

class ProductOfNumbers2 {
  /*
   * This is from the official solution which resets the prefix prod array each
   * time zero is encountered.
   *
   * 12 ms, 91.95%
   */
public:
  std::vector<int> pprod;

  ProductOfNumbers2() { pprod.push_back(1); }

  void add(int num) {
    if (num == 0) {
      pprod.clear();
      pprod.push_back(1);
    } else {
      pprod.push_back(pprod.back() * num);
    }
  }

  int getProduct(int k) {
    int N = pprod.size();
    if (N - k <= 0)
      return 0;
    return pprod.back() / pprod[N - k - 1];
  }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
