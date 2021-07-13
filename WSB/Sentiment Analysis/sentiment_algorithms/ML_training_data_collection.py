import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

cursor.execute("""
    SELECT stock_id, stock_symbol, dt, post_id, message, sentiment FROM mention
""")
rows = cursor.fetchall()

for row in rows:
    print(row['message'])
    bullish_sentiment = 0
    bearish_sentiment = 0
    sentiment_input = input(f'questo post ti sembra bullish (a), bearish (s) o neutral (d)?: ')
    if sentiment_input == 'a':
        bullish_sentiment = 1
    if sentiment_input == 's':
        bearish_sentiment = -1
    
    
    try:
        cursor.execute('''
            INSERT INTO sentiment_evolution (stock_id, dt, stock_symbol, mention_post_id, bullish_sentiment, bearish_sentiment)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (row['stock_id'], row['dt'], row['stock_symbol'], row['post_id'], bullish_sentiment, bearish_sentiment))
        connection.commit()

    except Exception as e:
        print(e)
