# Write your MySQL query statement below
select 
a.symbol as metal,
b.symbol as nonmetal
from 
Elements as a,
Elements as b
where a.type= "Metal" and b.type="Nonmetal"
[object Object]
