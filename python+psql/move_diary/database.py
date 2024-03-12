import os
import psycopg2
import datetime

from dotenv import load_dotenv

load_dotenv()

#title, release_date, watched

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (user_username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);"""

CREATE_RELEASE_INDEX = """CREATE INDEX IF NOT EXISTS idx_movies_release 
    ON movies(release_timestamp);
"""

INSERT_MOVIES = """INSERT INTO movies (title, release_timestamp) 
    VALUES (%s, %s);"""
INSERT_USER = """INSERT INTO users (username) VALUES (%s);"""
DELETE_MOVIE = """DELETE FROM movies WHERE title = %s;"""
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > %s;"

SELECT_WATCHED_MOVIES = """
    SELECT movies.* FROM movies
    JOIN watched ON movies_id = watched.movies_id
    JOIN users ON users.username = watched.user_username
    WHERE users.username = %s;
"""
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = %s;"
INSERT_WATCHED_MOVIES = """INSERT INTO watched (user_username, movie_id)
    VALUES (%s, %s);"""

SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE %s;"""

connection = psycopg2.connect(os.environ["DATABASE_URL"])

def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHLIST_TABLE)
            cursor.execute(CREATE_RELEASE_INDEX)

def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username))

def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()

def watch_movie(username, movie_id):
    with connection:
        # cursor.execute(DELETE_MOVIE, (movie_id))
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIES, (username, movie_id))

def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            return cursor.execute(SELECT_WATCHED_MOVIES, (username))

def search_movie(search_term):
    with connection:
        with connection.cursor() as cursor:
            return cursor.execute(SEARCH_MOVIE, (f"%{search_term}"))

def delete_movie(title):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_MOVIE, (title))