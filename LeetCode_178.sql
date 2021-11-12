-- Cannot do AS rank because probably rank is a keyword. Thus have to do
-- AS "rank"

SELECT
  score,
  DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores


-- None DENSE_RANK() method
SELECT
  S1.score,
  (
    SELECT
      COUNT(*)
    FROM (
          SELECT DISTINCT
            S2.score
          FROM Scores S2
          WHERE S2.score >= S1.score
        ) AS T
  ) AS `rank`
From Scores S1
ORDER BY `rank`