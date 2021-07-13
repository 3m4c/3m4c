import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

# extracting data from the 'mention' table: 
# we will use it to partially populate the 'sentiment_evolution' table
cursor.execute("""
    SELECT stock_id, stock_symbol, dt, post_id, sentiment FROM mention
""")
rows = cursor.fetchall()

#iterating through the data we have just extracted
for row in rows:
    
    # we already have a sentiment score from the mention table, 
    # know we split it into two columns
    sentiment = row['sentiment']
    bullish_sentiment = 0
    bearish_sentiment = 0
    if sentiment > 0:
        bullish_sentiment = sentiment

    elif sentiment < 0:
        bearish_sentiment = (-1) * sentiment

    try:
        cursor.execute('''
            INSERT INTO sentiment_evolution (stock_id, dt, stock_symbol, mention_post_id, bullish_sentiment, bearish_sentiment)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (row['stock_id'], row['dt'], row['stock_symbol'], row['post_id'], bullish_sentiment, bearish_sentiment))
        connection.commit()

    except Exception as e:
        print(e)
