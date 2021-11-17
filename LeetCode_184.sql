-- Two levels of INNER JOIN. Very slow.

-- 703 ms, 26% ranking

SELECT
    tt.name AS Department,
    ee.name AS Employee,
    tt.salary
FROM Employee ee
INNER JOIN (
    SELECT
        *
    FROM Department d
    INNER JOIN (
        SELECT
            e.departmentId,
            MAX(e.salary) AS Salary
        FROM
            Employee e
        GROUP BY e.departmentId
    ) t ON d.id = t.departmentId
) tt ON ee.departmentId = tt.id AND ee.salary = tt.salary


-- Official solution
-- The usage of IN is interesting.

SELECT
    d.name AS `Department`,
    e.name AS `Employee`,
    e.salary AS `Salary`
FROM Employee e
INNER JOIN Department d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT
        departmentId,
        MAX(salary)
    FROM Employee ee
    GROUP BY departmentId
)