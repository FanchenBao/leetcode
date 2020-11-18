#include <iostream>
#include <math.h> 

using namespace std;


class Solution {
public:
    /*
    This is acquired understanding from the hints in the question. Given T
    number of tests, each pig will have T + 1 states (the first T states, the
    pig live after the first test. And the last state is that the pig dies
    after the first test). Therefore, given x number of pigs and T number of
    tests, we can generate at most (T + 1)^x number of states. The question is
    to find the min x such that (T + 1)^x is larger or equal to the total
    number of buckets. This way, we can always guaranatee that each bucket is
    associated with one of the state.

    The difficulty of this problem is not with coding, but to figure out the
    number of states that can be created with x pigs in T number of tests.
    */
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        return int(ceil(log(buckets) / log(minutesToTest / minutesToDie + 1)));
    }
};
 
 
int main() {
    cout<<"life is lonly\n";
    return 0;
}