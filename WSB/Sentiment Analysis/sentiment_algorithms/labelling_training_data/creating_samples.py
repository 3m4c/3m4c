import config
import psycopg2
import psycopg2.extras
import random

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER,
                              password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

# we take a third of samples from march 2020 crash (to train enough bearish posts), 
# the we change the interval to fetch posts from january 2021
# and then again from june 2021

cursor.execute("""
    SELECT stock_symbol, post_id, dt, title, body, flair, upvote_ratio 
    FROM mention
    WHERE dt::date BETWEEN '2020-02-13' AND '2020-03-27'
""")
rows = cursor.fetchall()

random_sample = random.sample(rows, 500) 

for row in random_sample:
    print(f'{row["title"]} \n {row["flair"]} \n {row["body"]}')
    sentiment = 'neutral'
    sentiment_input = input(f'questo post ti sembra bullish (a), bearish (s), neutral (d) o controversial (f)?: ')
    if sentiment_input == 'a':
        sentiment = 'bullish'
    if sentiment_input == 's':
        sentiment = 'bearish'
    if sentiment_input == 'f':
        sentiment = 'controversial'

    post_id = row['post_id']
    stock_symbol = row['stock_symbol']

    try:
        cursor.execute('''
        UPDATE mention
        SET sentiment = %s
        WHERE post_id = %s AND stock_symbol = %s
        ''', (sentiment, post_id, stock_symbol))
        connection.commit()

    except Exception as e:
        print(e)
        connection.rollback()
