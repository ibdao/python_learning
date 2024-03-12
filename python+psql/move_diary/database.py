import sqlite3
import datetime
#title, release_date, watched

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL, 

);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    username TEXT PRIMARY KEY,
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (user_username), REFERENCES users(username)
    FOREIGN KEY (movie_id), REFERENCES movies(id)
);"""

CREATE_RELEASE_INDEX = """CREATE INDEX IF NOT EXISTS idx_movies_release 
    ON movies(release_timestamp);
"""

INSERT_MOVIES = """INSERT INTO movies (title, release_timestamp) 
    VALUES (?, ?);"""
INSERT_USER = """INSERT INTO users (username) VALUES (?);"""
DELETE_MOVIE = """DELETE FROM movies WHERE title = ?;"""
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"

SELECT_WATCHED_MOVIES = """
    SELECT movies.* FROM movies
    JOIN watched ON movies_id = watched.movies_id
    JOIN users ON users.username = watched.user_username
    WHERE users.username = ?;
"""
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"
INSERT_WATCHED_MOVIES = """INSERT INTO watched (user_username, movie_id)
    VALUES (?, ?);"""

SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)

def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username))

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            return connection.execute(SELECT_UPCOMING_MOVIES, (today_timestamp))
        else:
            return connection.execute(SELECT_ALL_MOVIES)

def watch_movie(username, movie_id):
    with connection:
        # connection.execute(DELETE_MOVIE, (movie_id))
        connection.execute(INSERT_WATCHED_MOVIES, (username, movie_id))

def get_watched_movies(username):
    with connection:
        return connection.execute(SELECT_WATCHED_MOVIES, (username))

def search_movie(search_term):
    with connection:
        return connection.execute(SEARCH_MOVIE, (f"%{search_term}"))

def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIE, (title))