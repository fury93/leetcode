      NewYork 
    FROM 
  (
    SELECT 
      COUNT(*) as excellent_students 
    WHEN NY.excellent_students < CA.excellent_students THEN 'California University'
    ELSE 'No Winner'
  END AS winner
FROM 
# Write your MySQL query statement below
SELECT 
  CASE 
    WHEN NY.excellent_students > CA.excellent_students THEN 'New York University'
[object Object]
