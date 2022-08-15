https://leetcode.com/problems/swap-salary/solution/

UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;


update salary set sex = IF (sex = "m", "f", "m");