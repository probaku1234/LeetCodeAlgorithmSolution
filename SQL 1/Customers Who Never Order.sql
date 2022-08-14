/* https://leetcode.com/problems/customers-who-never-order/

SELECT c.Name AS 'Customers' FROM Customers c
LEFT JOIN (SELECT CustomerId from Orders) o ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL

select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);