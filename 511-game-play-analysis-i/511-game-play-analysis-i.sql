select player_id,event_date as first_login from (SELECT *, 
       ROW_NUMBER() OVER(PARTITION BY player_id  ORDER BY event_date) RowNumber
FROM Activity) as t
where RowNumber=1;