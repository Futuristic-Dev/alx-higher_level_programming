-- list the score and the number of occurences with each score with number

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
