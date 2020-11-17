#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    /*
    92% ranking.

    Use three values prepre, pre, and cur. Use a boolean to record whether a
    peak has been encountered. One pass.

    Basically consider all possible situations with three values.
    */
    int longestMountain(vector<int>& A) {
        int pre = 10001;
        int prepre = 10001;
        int count = 0;
        int max_count = 0;
        bool peakSeen = false;
        for (int cur : A) {
            if (pre < cur) {
                if (prepre >= pre) {
                    max_count = max(count, max_count);    
                    count = 2;
                } else {
                    count += 1;
                }
            } else if (pre == cur) {
                if (prepre > pre) {
                    max_count = max(count, max_count);
                    count = 0;
                } else {
                    count = 0;
                }
                peakSeen = false;
            } else {
                if (prepre == pre) {
                    count = 0;
                    peakSeen = false;
                } else if (prepre < pre) {
                    peakSeen = true;
                    count += 1;
                    max_count = max(count, max_count);
                } else if (peakSeen) {
                    count += 1;   
                    max_count = max(count, max_count);
                }
            }
            prepre = pre;
            pre = cur;
        }
        return max_count;
    }
}; 