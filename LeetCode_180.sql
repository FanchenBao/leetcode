-- This is the very first complex SQL query I have written. The idea is to count
-- the number of rows for a given number with id restriction from that number's
-- id to that number's id plus two. If that count is three, we have a number that
-- is repeating consecutively for three times.

SELECT DISTINCT
  num AS ConsecutiveNums
FROM
  Logs L1
WHERE (
  SELECT COUNT(*) AS c
  FROM (
    SELECT * FROM Logs L2
    WHERE L2.num = L1.num
  ) T
  WHERE T.id >= L1.id AND T.id <= L1.id + 2
  HAVING c = 3
)


-- Using LAG and LEAD
-- Inspired by: https://leetcode.com/problems/consecutive-numbers/solution/720787
-- This solution is better than the official one, because it also handles the
-- case where the three consecutive numbers do not have consecutive id values
-- i.e. their id values have gaps.
SELECT DISTINCT
  t.num AS ConsecutiveNums
FROM (
  SELECT
    num,
    LEAD(num, 1) OVER (ORDER By id) AS `lead`,
    LAG(num, 1) OVER (ORDER By id) AS `lag`
  FROM
    Logs
) t
WHERE t.num = t.lead AND t.num = t.lag