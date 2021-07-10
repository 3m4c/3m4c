import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

cursor.execute("""
    SELECT stock_id, stock_symbol, dt, post_id, sentiment FROM mention
""")
rows = cursor.fetchall()

stonks = {}
for row in rows:
  stonk = row[stock_symbol]
  stonks.add(stonk)
  print(stonks)
