-- Add python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
SELECT id AS Movie_ID, name AS Movie_Title, imdb_rating AS Rating
FROM movies
WHERE genre = 'Horror' AND year <= 1985
ORDER BY imdb_rating DESC
LIMIT 3;
python run_sql.py
git add sql/horror_movies.sql data/movies.csv
git commit -m "Add SQL query and results"
git push origin main
pytest tests.py
