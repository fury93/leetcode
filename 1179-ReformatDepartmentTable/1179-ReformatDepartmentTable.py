  LEFT JOIN Department AS October ON (
    Ids.id = October.id
    AND October.month = "Oct"
  )
  LEFT JOIN Department AS November ON (
    Ids.id = November.id
    AND November.month = "Nov"
  )
  LEFT JOIN Department AS December ON (
    Ids.id = December.id
    AND December.month = "Dec"
  );
[object Object]
