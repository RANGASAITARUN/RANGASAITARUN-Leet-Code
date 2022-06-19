# Write your MySQL query statement below
with t1 as (
SELECT *, 
       ROW_NUMBER() OVER(PARTITION BY customer_number) RowNumber
FROM orders)
select customer_number from t1
where RowNumber= (select max(RowNumber) from t1)