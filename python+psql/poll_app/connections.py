import psycopg2

def create_connection():
    return psycopg2.connect(database="poll_app", user='iandao', password='password', host='127.0.0.1', port= '5432')

# poll = SimpleConnectionPool(minconn=1, maxconn=10, dsn=)