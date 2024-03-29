https://leetcode.com/problems/group-sold-products-by-the-date/


select sell_date,
                count(DISTINCT(product)) as num_sold,
                GROUP_CONCAT(DISTINCT product ORDER BY product) as products
from Activities
group by sell_date
order by sell_date