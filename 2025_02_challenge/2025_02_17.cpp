#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  int numTilePossibilities(string tiles) {
    /*
     * LeetCode 1079
     *
     * Create all possible permutations.
     * Two pieces of info that I did not know before.
     * 1. to_string(char) will not produce a string of the char, but
     * rather the string version of the ASCII of the char. To create
     * a string of char, use std::string(char)
     * 2. the insert function of string changes it in-place. Thus we
     * need to create a copy and then do the insertion on the copy.
     *
     * O(N!), 36 ms, 40.21%
     */
    std::unordered_set<std::string> seen;
    for (char t : tiles) {
      std::string t_str{t};
      std::vector<std::string> tmp{"", t_str};
      for (std::string p : seen) {
        for (int i = 0; i <= p.size(); i++) {
          std::string new_str = p;
          tmp.push_back(new_str.insert(i, t_str));
        }
      }
      for (std::string t : tmp)
        seen.insert(t);
    }
    return seen.size() - 1; // do not count empty string
  }
};

class Solution2 {
public:
  int helper(std::vector<int> &counter) {
    /* counter is the state.
     * This function returns the total number of sequences that can be created
     * based on the state described in counter.
     */
    int res = 0;
    for (int i = 0; i < 26; i++) {
      if (counter[i] > 0) {
        res++; // use the current letter by itself
        counter[i]--;
        res += helper(counter); // find the number of sequences without the
                                // current letter, and then prepend the current
                                // letter to each sequence
        // backtrack
        counter[i]++;
      }
    }
    return res;
  }

  int numTilePossibilities(string tiles) {
    /*
     * This method is inspired by method 2 of the editorial. The key
     * observation is that we can use a frequency counter to represent the
     * state of the tile when one tile is selected as the first tile in
     * the sequence. We go through all the tiles to serve as the first
     * tile, and recursion to compute the total number of sequences in the
     * remaining tiles.
     *
     * O(2^N), 0 ms
     */
    std::vector<int> counter(26);
    for (char t : tiles)
      counter[t - 'A']++;
    return helper(counter);
  }
};

int main() {
  string tiles = "AAB";
  Solution sol;
  std::cout << sol.numTilePossibilities(tiles) << std::endl;
}
