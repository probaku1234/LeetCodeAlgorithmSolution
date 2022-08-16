https://leetcode.com/problems/fix-names-in-a-table/

select user_id, concat(ucase(left(name,1)),lcase(right(name,CHAR_LENGTH(name) - 1))) as name
from users
order by user_id