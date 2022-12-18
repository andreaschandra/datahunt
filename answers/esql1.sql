-- Exercise 1
-- SELECT .. FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...
-- ESQL1
-- get first 10 rows of  customer_id, first_name, last_name, address, and postal_code
-- in first_name alphabetical order
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       a.address,
       a.postal_code
FROM customer c
JOIN address a ON c.address_id = a.address_id
ORDER BY first_name
LIMIT 10;