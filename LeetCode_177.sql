-- Syntax for CREATE FUNCTION is here:
-- https://www.educba.com/mysql-create-function/

-- I was trouble computing N - 1 and use it in the LIMIT clause. However, MySQL
-- forbids dynamic values in the LIMIT clause. Thus, I must pre-compute N - 1
-- before passing it to LIMIT. I don't know the syntax for that, but luckily, I
-- stumbled upon this post:
-- https://stackoverflow.com/questions/6740932/mysql-create-function-syntax

-- It demonstrated how to set a declared variable to the desired value.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE tgt INT;
  SET tgt = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL(
        (SELECT DISTINCT
            salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT tgt, 1), NULL)
  );
END


-- Using DENSE_RANK()
-- Solution ref: https://leetcode.com/problems/nth-highest-salary/discuss/872818/Using-Rank
-- DENSE_RANK() ref: https://www.mysqltutorial.org/mysql-window-functions/mysql-dense_rank-function/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM (
        SELECT
          salary,
          DENSE_RANK() OVER (ORDER BY salary DESC) as rk
        FROM Employee
      ) AS t
      WHERE rk = N
  );
END