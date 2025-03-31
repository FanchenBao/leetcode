#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> partitionLabels(string s) {
    /*
     * LeetCode 763
     *
     * Find the first and last index of occurrence of each letter in s, sort
     * them based on the first, and check if the next range overlaps. If
     * it overlaps, we update the last index to the bigger one. Otherwise,
     * we complete one partition and start a new one.
     *
     * O(N), 0 ms
     */
    std::vector<std::vector<int>> ranges(27, {999, -1});
    for (int i = 0; i < s.size(); i++) {
      int idx = s[i] - 'a';
      ranges[idx][0] = std::min(ranges[idx][0], i);
      ranges[idx][1] = std::max(ranges[idx][1], i);
    }
    std::sort(ranges.begin(), ranges.end());
    std::vector<int> res;
    int pre_lo = 0, pre_hi = 0;
    for (auto const &r : ranges) {
      int lo = r[0], hi = r[1];
      if (lo <= pre_hi) {
        pre_hi = std::max(pre_hi, hi);
      } else {
        res.push_back(pre_hi - pre_lo + 1);
        pre_lo = lo, pre_hi = hi;
      }
      if (pre_lo == 999)
        break;
    }
    return res;
  }
};

int main() {
  std::string s =
      "ntswuqqbidunnixxpoxxuuupotaatwdainsotwvpxpsdvdbwvbtdiptwtxnnbtqbdvnbowqi"
      "tudutpsxsbbsvtipibqpvpnivottsxvoqqaqdxiviidivndvdtbvadnxboiqivpusuxaaqnq"
      "aobutdbpiosuitdnopoboivopaapadvqwwnnwvxndpxbapixaspwxxxvppoptqxitsvaaawx"
      "waxtbxuixsoxoqdtopqqivaitnpvutzchkygjjgjkcfzjzrkmyerhgkglcyffezmehjcllml"
      "rjghhfkfylkgyhyjfmljkzglkklykrjgrmzjyeyzrrkymccefggczrjflykclfhrjjckjlmg"
      "lrmgfzlkkhffkjrkyfhegyykrzgjzcgjhkzzmzyejycfrkkekmhzjgggrmchkeclljlyhjkc"
      "hmhjlehhejjyccyegzrcrerfzczfelzrlfylzleefgefgmzzlggmejjjygehmrczmkrc";
  Solution sol;
  sol.partitionLabels(s);
}
