#�Write�your�MySQL�query�statement�below
SELECT�ABS((SELECT�MAX(salary)�as�salary�FROM�Salaries�WHERE�department�=�"Engineering")�
-�(SELECT�MAX(salary)�as�salary�FROM�Salaries�WHERE�department�=�"Marketing"))�AS�salary_difference�
[object�Object]
