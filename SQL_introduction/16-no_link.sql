-- Lists all records with a name from second_table, sorted by descending score
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC;
