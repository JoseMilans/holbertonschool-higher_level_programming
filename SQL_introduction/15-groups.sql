-- Lists the number of records for each score in second_table, sorted by the count in descending order
SELECT score, COUNT(score) AS `number` FROM second_table GROUP BY score ORDER BY `number` DESC;
