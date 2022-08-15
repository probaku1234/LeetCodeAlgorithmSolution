https://leetcode.com/problems/calculate-special-bonus/


SELECT employee_id,
IF(employee_id%2 != 0 AND name NOT LIKE 'M%',salary,0) AS bonus
FROM Employees ORDER BY employee_id;

SELECT employee_id,
CASE
    WHEN employee_id%2 != 0 AND name NOT LIKE 'M%' THEN salary else 0
END AS bonus
FROM Employees ORDER BY employee_id;