from psycopg2.extras import execute_values
from typing import List, Tuple

Poll = Tuple[int, str, int]
Option = Tuple[int, str, int]
Vote = Tuple[str, int]
# PollWithOptions = Tuple[int, str, str, int, str, int]
# PollResults = Tuple[int, str, int, float]

CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""
CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES polls (id));"""
CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER, vote_timestamp INTEGER  FOREIGN KEY(option_id) REFERENCES options (id));"""


SELECT_ALL_POLLS = "SELECT * FROM polls;"
SELECT_POLL = "SELECT * FROM polls WHERE id = %s;"
SELECT_POLL_OPTIONS = """SELECT * FROM options WHERE polls.id = %s;"""
SELECT_LATEST_POLL = """SELECT * FROM polls 
WHERE polls_id = (SELECT id FROM polls ORDER BY id DESC LIMIT 1);"""
# SELECT_POLL_VOTE_DETAILS = """SELECT options_id, options.option_text,
# COUNT (votes.options_id) AS vote_count, 
# COUNT (votes.option_id) / SUM(COUNT(votes.option_id)) OVER() * 100.0 AS vote_percentage
# FROM options 
# LEFT JOIN votes ON options_id = votes.option_id
# WHERE options.poll_id = %s
# GROUP BY options.id"""
# SELECT_RANDOM_POLL = """SELECT * FROM votes WHER option_id = %s ORDER BY RANDOM() LIMIT 1;"""

SELECT_OPTION = "SELECT * FROM options WHERE id = %s;"
SELECT_VOTES_FOR_OPTION = "SELECT * FROM votes WHERE option_id = %s"
INSERT_POLL_RETURN_ID = "INSERT INTO polls (title, owner_username )VALUES (%s, %s) RETURNING id;"
INSERT_OPTION_RETURN_ID = "INSERT INTO options (option_text, poll_id) VALUES (%s, %s) RETURNING id;"
INSERT_VOTE = "INSERT INTO votes (username, option_id, vote_timestamp) VALUES (%s, %s, %s);"


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)

def create_poll(connection, title: str, owner: str, options: List[str]):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_POLL_RETURN_ID, (title, owner))

            poll_id = cursor.fetchone()[0]
            return poll_id
            # option_values = [(option_text, poll_id) for option_text in options]

            # execute_values(cursor, INSERT_OPTION, option_values)

# ---- Polls

def get_poll (connection, poll_id: int) -> Poll:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL, (poll_id))
            return cursor.fetchone()

def get_polls(connection) -> List[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()


def get_latest_poll(connection) -> List[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchone()


def get_poll_options(connection, poll_id: int) -> List[Option]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_OPTIONS, (poll_id,))
            return cursor.fetchall()

# -- Options
    
def get_option(connection, option_id: int) -> Option:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_OPTION, (option_id,))
            return cursor.fetchone()

def add_option(connection, option_text, poll_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_OPTION_RETURN_ID, (option_text, poll_id))
            option_id = cursor.fetchone()[0]
            return option_id

# -- Votes

def get_votes_for_option(connection, option_id: int) -> List[Vote]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_VOTES_FOR_OPTION, (option_id,))
            return cursor.fetchall()

def add_poll_vote(connection, username: str, vote_timestamp: float, option_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id, vote_timestamp,))

# def get_poll_and_vote_results(connection, poll_id: int) -> List[PollResults]:
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(SELECT_POLL_VOTE_DETAILS, (poll_id))
#             return cursor.fetchall()


# def get_random_poll_vote(connection, option_id: int) -> List[Vote]:
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(SELECT_RANDOM_POLL, (option_id))
#             return cursor.fetchone()