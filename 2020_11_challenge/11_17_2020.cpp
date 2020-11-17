#include <iostream>

using namespace std;


class Solution {
public:
    void swap(int &a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }

    /*
    0 ms run time. As this problem is not so much a coding challenge as a good
    brain teaser.
    */
    int mirrorReflection(int p, int q) {
        if (q == 0) {return 0;}  // edge case
        int tan_n = q;
        int tan_d = p;
        int wall = 0;
        int remain_wall = p;  // remaining length of wall in the dir of laser
        int height_needed = 0;  // height computed from remain_wall
        int dir = 1;  // 1 = counter clockwise, 3 = clockwise
        while (remain_wall != 0) {
            height_needed = remain_wall * tan_n / tan_d;
            if (height_needed <= p) {  // end point is on adjacent wall
                wall = (wall + dir) % 4;
                remain_wall = p - height_needed;
                swap(tan_n, tan_d);
            } else {  // end point on opposite wall
                remain_wall -= p * tan_d / tan_n;
                wall = (wall + 2) % 4;
                dir = (dir + 2) % 4;
            }
        }
        return dir == 1 ? wall : wall - 1;
    }
};