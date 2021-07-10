import config
import psycopg2
import psycopg2.extras
import functools
import operator
import re
import emoji

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

cursor.execute(
    '''SELECT stock_id, stock_symbol, message, score, num_comments FROM mention'''
)
rows = cursor.fetchall()

def WSB_sentiment (message, score, num_comments):
    
    bullish = ['moon', 'mars', 'yolo', 'all', 'strong', "can't", 'tits', 'c', 'calls', 'call', 'btfd', 'undervalued', 'gains', 'gain', 'bull', 'bulls', 'bullish', 
               'buy', 'dip', 'fuel', 'fire', 'squeeze', 'squeezing', 'squoze', 'squozing', 'holding', 'bought', 'hold', 'hodl', 'hodling', 'holding', 'yoloed',
               "yolo'ed", 'mooning',
               '💎', '🤲', '💎🤲', '🤤🤤🤤', '🌝', '💎🤲🚀', '💎🙌🏻', '🙌🏻', '💎💎🙌🙌', '🚀💎👐', '💎✋🚀', 
               '🦍', '🦍🦍', '🦍🦍🦍', '🦍🦍🦍🦍', '🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍🦍🦍',
               '🚀', '🚀🚀', '🚀🚀🚀', '🚀🚀🚀🚀', '🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀🚀', 
               '🚀🚀🚀🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀', '🌙', '🌙🌙', '🌙🌙🌙', '🚀📈', '📈', '🌚', '🚀🌚'
              ]
    
    bearish = ['p', 'puts', 'put', 'losses', 'lose', 'loss', 'bear', 'bears', 'bearish', 'gay', 'sold', 'sell', 'selling',
               '🌈🐻', '🌈', '🐻', '😬', '😬😬'
              ]
    
    bullish_count = 0
    bearish_count = 0
    magnitude = score + num_comments
    
    message_lowercase = message.lower()
    message_split_emoji = emoji.get_emoji_regexp().split(message_lowercase)
    message_split_whitespace = [substr.split() for substr in message_split_emoji]
    message_split = functools.reduce(operator.concat, message_split_whitespace)
    
    for word in message_split:
        if word in bullish:
            bullish_count += 1
        elif word in bearish:
            bearish_count += 1
    print(bullish_count)
    direction = bullish_count - bearish_count
    sentiment = magnitude * direction
        
        
    if abs(sentiment) > 1:
        return sentiment
    elif bearish_count == 0 or bullish_count == 0:
        return sentiment
    
for row in rows:
    result = WSB_sentiment(row['message'], row['score'], row['num_comments'])
    print(result)

