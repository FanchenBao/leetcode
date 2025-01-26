#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> lexicographicallySmallestArray(vector<int> &nums, int limit) {
    /*
     * LeetCode 2948
     *
     * Take advantage of the ordered map in C++. Use number as key and the
     * value is a stack of positions.
     *
     * For each number in nums, we find the smallest number that is swappable
     * with it. The lower limit is set as nums[i] - limit. If such swappable
     * number is available, we swap it. Otherwise we use the original one.
     *
     * Note that once a number is set in stone, we must pop its index in the
     * map's value. And if a number has all its indices popped, the number must
     * be removed from the map.
     *
     * O(NlogM), where N = len(nums) and M = len(unique nums)
     *
     * TLE, this idea does not work!
     */
    std::map<int, std::set<int>> pos;
    int N = nums.size();
    for (int i = N - 1; i >= 0; i--)
      pos[nums[i]].insert(i);
    std::vector<int> res{nums};
    for (int i = 0; i < N; i++) {
      int tgt = res[i];
      auto it = pos.lower_bound(tgt - limit);
      // keep searching for the smallest value to be put at position i
      while (it->first < tgt) {
        tgt = it->first;
        it = pos.lower_bound(tgt - limit);
      }
      int j = *(pos[tgt].begin());
      if (i != j) {
        // update the index of the current number
        pos[res[i]].erase(i);
        pos[res[i]].insert(j);
        // update the index of the target number
        pos[tgt].erase(j);
        pos[tgt].insert(i);
        std::swap(res[i], res[j]);
      }
      // we have settled on index i, remove it from the pos
      pos[res[i]].erase(i);
      if (pos[res[i]].empty())
        pos.erase(res[i]);
    }
    return res;
  }
};

class Solution2 {
public:
  vector<int> lexicographicallySmallestArray(vector<int> &nums, int limit) {
    /*
     * This is my second solution without going through either the hint or
     * official solutions.
     *
     * The idea is to first sort nums desc and then group them. Each group
     * consists of consecutive sorted numbers with adjacent difference not
     * more than limit. We assign an index to each group and record a mapping
     * from each number to this group.
     *
     * Then as we go through nums, the current number can map to a group. Since
     * any number in the group can swap all the way to the smallest member of
     * the group, the current number can be replaced with that smallest member.
     * We then pop that smallest member and move on to the next number.
     *
     * There is still room for optimization. For example, we don't need to
     * use a vector of stack to represent the groups. We can use a vector of
     * indices of the sorted array. But let's submit this solution first.
     *
     * O(NlogN), 934 ms, 5.40%
     */
    std::vector<int> res{nums};
    std::sort(res.begin(), res.end(), std::greater<int>());
    std::vector<std::stack<int>> groups;
    std::map<int, int> num_group_map;
    for (int i = 0; i < res.size(); i++) {
      if (i == 0 || res[i - 1] - res[i] > limit) {
        // create new stack in groups
        groups.push_back(std::stack<int>());
      }
      groups[groups.size() - 1].push(res[i]);
      num_group_map[res[i]] = groups.size() - 1;
    }
    for (int i = 0; i < nums.size(); i++) {
      int group_idx = num_group_map[nums[i]];
      res[i] = groups[group_idx].top();
      groups[group_idx].pop();
    }
    return res;
  }
};

class Solution3 {
public:
  vector<int> lexicographicallySmallestArray(vector<int> &nums, int limit) {
    /*
     * Let's optimize solution2. Instead of materializing the groups, we only
     * keep the last index of each group. After the smallest number of a group
     * is used, we decrement the last index.
     *
     * O(NlogN), 339 ms, 29.05%
     */
    std::vector<int> res{nums};
    std::sort(nums.begin(), nums.end(), std::greater<int>());
    std::vector<int> group_last_indices;
    std::map<int, int> num_group_map;
    for (int i = 0; i < nums.size(); i++) {
      if (i == 0 || nums[i - 1] - nums[i] > limit) {
        // create new group
        group_last_indices.push_back(i);
      }
      group_last_indices[group_last_indices.size() - 1] = i;
      num_group_map[nums[i]] = group_last_indices.size() - 1;
    }
    for (int i = 0; i < res.size(); i++) {
      int group_idx = num_group_map[res[i]];
      res[i] = nums[group_last_indices[group_idx]];
      group_last_indices[group_idx]--;
    }
    return res;
  }
};

int main() {
  std::vector<int> nums{1, 7, 6, 18, 2, 1};
  int limit = 3;
  Solution3 sol;
  sol.lexicographicallySmallestArray(nums, limit);
}
