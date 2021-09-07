import config
import psycopg2
import psycopg2.extras
import pandas as pd

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER,
                              password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

sample1 = pd.read_csv('/sample1.csv')
sample2 = pd.read_csv('/sample1.csv')
sample3 = pd.read_csv('/sample1.csv')


def annotator(sample, starting_row = 0)
    for row in sample[starting_row:]:
        print(f'{row["title"]} \n {row["flair"]}, {row["upvote_ratio"]} \n {row["body"]}')
        sentiment = 'neutral'
        sentiment_input = input(f'questo post ti sembra bullish (a), bearish (s), neutral (d) o controversial (f)?: ')
        if sentiment_input == 'a':
            sentiment = 'bullish'
        if sentiment_input == 's':
            sentiment = 'bearish'
        if sentiment_input == 'd':
            sentiment = 'neutral'
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
            
annotator(sample1)
annotator(sample2)
annotator(sample3)
