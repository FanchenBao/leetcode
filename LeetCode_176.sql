-- I searched online and found the use of LIMIT to select a specific row after
-- sorting the salary in descending order. However, I didn't know how to return
-- NULL when there is no second highest salary.

-- Also, I failed to realize that when sorting, we have to use SELECT DISTINCT to
-- avoid duplicate in highest salary.

-- The final solution that I like is to use IFNULL to specify when we return NULL

# Write your MySQL query statement below
SELECT
    IFNULL(
        (SELECT DISTINCT 
            salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1,1), NULL
    )
AS SecondHighestSalary
