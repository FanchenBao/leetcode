"""
07/02/2019

I couldn't solve this problem, so I looked it up in the discussion.

I knew it had to be DP, but I was confused how DP should be carried
out. My initial thought was that given the min height of i books, I
just need to figure out how to compute the min height for i+1 books.
Then this was a typical DP. But once I realized that it was almost
impossible to use simple analysis to get min height for i+1 books
from i books, I was stuck. I tried some convoluted algorithms to
analyze different situations, but I knew that was bound to fail. But
I just seemed to be unable to figure out the right approach for DP.

After checking the discussion, I realized my biggest mistake in the
initial DP attempt. For DP to work, the i+1 solution must depend on
MORE THAN just the i solution. If i+1 only depends on i, then it is
not DP but linear solution. DP works if i+1 depends on solution of
i, i-1, i-2, etc. And this concept was exactly the essence of the
solution. To find min height after adding the i+1th book, we need
to group as many books as possible from i+1 all the way down into
one shelf, as a single shelf always had the min height for the given
books currently in the shelf. Then, we need to find out the min
height of the remaining books, which was where DP came into play.
We added these two values together, and we would have one possible
small heights for i+1 books. But that was only one possibilities,
not the smallest. We had to do this procedure for each book we grabbed
to fit in one shelf with the i+1th book, and the overall min of all
possible smalle heights for i+1 was the answer.
"""


class Solution:
    def minHeightShelves(self, books, shelf_width):
        numBooks = len(books)
        h = [10 ** 6] * (
            numBooks + 1
        )  # h[i] is the min height for i books. We want to find h[numBooks]
        h[0] = 0
        for i in range(1, numBooks + 1):
            j = i - 1  # the ith book's index is j
            currWidth = 0
            currHeight = 0
            # put books j to i-1 in a single shelf, then the h[j] is the min height of the remaining
            # j books. The sum of h[j] and the height of the last shelf is one possibility to achieve
            # h[i]. If we go through all possible j to i-1 that can place in a single shelf, we have
            # all possible h[i]. We then pick the smallest such h[i].
            while j >= 0:
                currWidth += books[j][0]
                if currWidth > shelf_width:
                    break
                currHeight = max(currHeight, books[j][1])
                h[i] = min(h[i], h[j] + currHeight)
                j -= 1
        return h[numBooks]


sol = Solution()
print(
    sol.minHeightShelves(
        [[1, 1], [2, 3], [2, 3], [2, 3], [1, 1], [1, 1], [1, 2]], 4
    )
)
