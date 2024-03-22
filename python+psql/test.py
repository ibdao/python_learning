import psycopg2

url = "postgres://zyhbwcmz:PH22xyi9eeNYeTO90pwklwqyF4f2bG3j@bubble.db.elephantsql.com/zyhbwcmz"
conn = psycopg2.connect(url)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT);")
cursor.execute("INSERT INTO users VALUES ('kungpaodao');")

cursor.execute("SELECT * FROM users;")

print(cursor.fetchall())



conn.close()