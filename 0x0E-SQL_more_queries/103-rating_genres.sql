-- Lists all genres in database by their rating
SELECT g.name AS genre_name, SUM(s.rating) AS rating_sum
FROM tv_genres g
JOIN tv_shows_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.show_id = s.id
GROUP BY g.name
ORDER BY rating_sum DESC;
