# from pudb import set_trace; set_trace()
from random import randint
import math
import sys

"""
Is the coordinates in integer?

I want to run some examples. An equal-lateral triangle, we have 3 boomerangs, correct?

If we have a square, we have four.

but if we have a rectangle with unequal sides, then we have zero

here is in my mind right now.

Each boomerang is uniquely defined by the corner. by corner, I mean it is the
start that the other two stars' distances to it are equal.

So, given each star, we can try to find all possible booerangs that uses this
star as the corner, or anchor. So, let's say we compute pairwise distance for
all stars, then for each star, we search through the remaining stars and find
all the stars that have equal distance to it. Then we can compute the number
of boomerangs that can be formed by these equal-distance stars. We can use
combinatorial number to determine the number of boomerangs formed by all the
equal-distance stars.

So let me think. We first get all the distance. then for each star, we need to 
know all the other stars that are the same distance to it. What data structure
can i use to represent this by only computing the pairwise distace once.

so when we do pair wise distance, we get a distance, which can be attached
to both stars. if I can use the distance as the key, we can create a list of
starts that have the same distance to a target star. so something like this:

distances = {
    star1: {
        dist1: count
        dist2: count
        ...
    }
    star2: {
        dist1: count
        dist2: count
    }
}

We don't need to record the list of stars, we just need to have the count for
each distance.

Now here is one problem, I am going to use distance as a key to a mapping.
Distance is a floating number, can I do that? I acutally do not know.

You know what, I know. We can. Python has a library for fraction number. SO I
can use fraction number as the key. Even better, when we compute the distance,
we don't have to actually compute the distance, we can avoid doing the square root.
just the squraed plus squared. that will be a real number, which can be
represnted by fraction, which can then be used to serve as key

I am ready to give this a shot
"""
from collections import defaultdict
import fractions
from math import factorial


def boomerange(coords: List[Tuple[float, float]]) -> int:
    # let's use coords to represent the coords of all stars
    # first perform pairwise distance computation

    # We take O(N^2) to build distances.
    # We then take O(N) to accumulate the result, supposing that the factorial operation takes O(1)
    # So in total we have O(N^2)

    # Probably also O(N^2). improve on what? space or time compleixty

    # probably. because we seem to be repeating some of the values.
    # let me think. So when we compute one distance, it is associated with
    # two stars. Can we only record that once instead of twice? That will reduce
    # the space complexity.

    # I see where you are going with this. When we do the O(N^2), I will loop
    # the second one not from i + 1, but from 0 as well. This way, for each
    # star, we will obtain the full range of distances without the help from 
    # any previous computation. this won't hurt the time complexity too much,
    # but can reduce the space complexity to O(N)

    # Yes. For each corner of the cross, we have only two points that have
    # the same distance to it. so the corner of the cross form four boomerangs.
    # Then for the center point, all four corners are of the same distance,
    # then we can form 6 boomerangs out of it. BUT!! we are considering the 
    # case where three dots on the same line is considered as a boomerang. So
    # then we have 6 boomerangs with the center point as anchor, that is 4 choose 2.
    # so in total we have 4 + 6 = 10 boomerangs out of this configuration.

    # see what he is doing
    # Our algo will get 10.
    # I think so.
    # Yes, I think it is correct.
    # the other four are from the edges of the cross

    # wondering if google has any training, mentoring program for new employees
    # two parts of that one is what is mentoring like, onboarding. Resources for
    # self ton of class. taught by other googles. C++ wow~~~ iaccouple of course to 
    # get the c++ course. 


    # do the internal classes cost money????

    # fwfnwjfeva

    distances = defaultdict(lambda: defaultdict(int))
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i != j:
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dist = fractions.Decimal((x1 - x2)**2 + (y1 - y2)**2)  # use Decimal to serve as key
            # increment the number of stars that are dist distance away from for star i 
            distances[i][dist] += 1
            distances[j][dist] += 1
    # Now we have obtained the distances mapping. We will loop through it to
    # find the total number of boomerangs
    res = 0
    for val in distances.values():
        # each val is of shape
        # {dist1: count, dist2: count, ...}
        for c in val.values():
            # this obtains the number of stars for a particular distance
            if c >= 2:
                # I need to refresh my memory on how to do N choose 2. the math formula
                # for n choose 2. I might be wrong here.
                # because any two stars among the stars that have the same distance
                # to the anchor can form a unique boomerang. So the number of total
                # boomerangs is from these stars choose any two, which is N choose 2
                res += factorial(c) / (factorial(c - 2) * 2)
    return res

"""
(1, 1), (1, -1), (-1, 1), (-1, -1)

This is a square, which shall return 4 boomerangs.

So going through the construction of distances.
for the first point (1, 1), we have
So we have two stars that are 2 distance away (strictly speaking sqrt(2)), and
one star that is 8 distance away.

same thing for all the otehr stars

it's not really a matrix, because i am using distance as the key to a mapping.
but each star has an entry, and for each star, we have bunch of distances
associated with it. for each distance, we have a count of number of stars that
are that distance away from it.

Yes, that is correct.
{
    0: {
        2: 2
        8: 1
    },
    1: {
        2: 2
        8: 1
    },
    2: {
        2: 2
        8: 1
    },
    3: {
        2: 2
        8: 1
    }
}

Then we loop over each star in the distances mapping, and then check each distance
For star 0, dist 2 gives us 2 counts, 2 choose 2 gives us 1. We record 1 in the
result. Dist 8 gives us 1 count, we cannot use this, skip.

The same goes for the other three stars, so in total we have four boomerangs.

"""



# tests = [([randint(-1000000000, 1000000000) for _ in range(1000)], 0) for _ in range(5)]
tests = [
    ([(1, 1), (1, -1), (-1, 1), (-1, -1)], 4)
]

for i, (coords, ans) in enumerate(tests):
    res = boomerange(coords)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {A}')



