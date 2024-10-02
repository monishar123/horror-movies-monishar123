import sqlite3
import pandas as pd

def main():
    # Connect to your SQLite database
    conn = sqlite3.connect('your_database.db')  # Ensure this matches the created database file

    # Create a table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        name TEXT,
        genre TEXT,
        year INTEGER,
        imdb_rating REAL
    );
    """
    conn.execute(create_table_query)

    # Check if the table is empty and insert sample data if it is
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies;")
    count = cursor.fetchone()[0]

    if count == 0:  # If the table is empty, insert data
        insert_query = """
        INSERT INTO movies (id, name, genre, year, imdb_rating) VALUES
        (1, 'Psycho', 'Horror', 1960, 8.5),
        (2, 'The Shining', 'Horror', 1980, 8.4),
        (3, 'Halloween', 'Horror', 1978, 7.8);
        """
        conn.execute(insert_query)
        conn.commit()

    # Query to fetch horror movies from the database
    sql = "SELECT id AS Movie_ID, name AS Movie_Title, imdb_rating AS Rating FROM movies WHERE genre = 'Horror' AND year <= 1985 ORDER BY imdb_rating DESC LIMIT 3;"

    # Execute the query and read into a DataFrame
    movies = pd.read_sql(sql, conn)

    # Print the results
    if movies.empty:
        print("No horror movies found.")
    else:
        print("Top horror movies:")
        print(movies)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()