# Write your MySQL query statement below
select w.id from Weather w
join Weather e on w.recordDate = e.recordDate + INTERVAL 1 DAY
where w.temperature>e.temperature