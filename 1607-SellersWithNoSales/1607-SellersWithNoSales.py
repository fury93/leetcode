    FROM 
        Seller s
    LEFT JOIN 
        Orders o
    ON 
        s.seller_id = o.seller_id
    GROUP BY 
        s.seller_id
)t0
WHERE 
    flag=0
ORDER BY 1 ASC
[object Object]
