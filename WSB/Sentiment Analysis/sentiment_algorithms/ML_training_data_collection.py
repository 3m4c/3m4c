import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

cursor.execute("""
    SELECT stock_symbol, post_id, message FROM mention
""")
rows = cursor.fetchall()

for row in rows:
    print(row['message'])
    sentiment = 0
    sentiment_input = input(f'questo post ti sembra bullish (a), bearish (s) o neutral (d)?: ')
    if sentiment_input == 'a':
        sentiment = 1
    if sentiment_input == 's':
        sentiment = -1
    
    post_id = row['post_id']
    stock_symbol = row['stock_symbol']

    try:
        cursor.execute('''
        UPDATE mention
        SET sentiment = %s
        WHERE post_id = %s AND stock_symbol = %s
        ''', (result, post_id, stock_symbol))
        connection.commit()

    except Exception as e:
        print(e)
        connection.rollback()
