# Write your MySQL query statement below
Select player_id,min(event_date) AS first_login From Activity
Group BY player_id;