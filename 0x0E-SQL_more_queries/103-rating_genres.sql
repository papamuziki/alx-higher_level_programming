-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- 	each record displays: tv_genres.name - rating sum
-- 	results sorted in descending order
SELECT tv_genres.name, SUM(tv_shows_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY 2 DESC;
