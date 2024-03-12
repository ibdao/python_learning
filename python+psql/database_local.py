import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='iandao', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''SELECT 'CREATE DATABASE test2db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'test2db')''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()