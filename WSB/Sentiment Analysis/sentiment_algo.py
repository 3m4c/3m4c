import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

cursor.execute(
    '''SELECT stock_id, stock_symbol, message, score, num_comments FROM mention'''
)
rows = cursor.fetchall()

def WSB_sentiment (message, score, num_comments):
    
    bullish = ['moon', 'mars', 'yolo', 'all', 'strong', "can't", 'tits', 'c', 'calls', 'call', 'btfd', 'undervalued', 'gains', 'gain', 'bull', 'bulls', 'bullish', 
               'buy', 'dip', 'fuel', 'fire', 'squeeze', 'squeezing', 'squoze', 'squozing', 'holding', 'bought', 'hold', 'hodl', 'hodling', 'holding',
               '💎', '🤲', '💎🤲', '🤤🤤🤤', '🌝', '💎🤲🚀', '💎🙌🏻', '🙌🏻', '💎💎🙌🙌', '🚀💎👐', '💎✋🚀', 
               '🦍', '🦍🦍', '🦍🦍🦍', '🦍🦍🦍🦍', '🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍🦍🦍',
               '🚀', '🚀🚀', 🚀🚀🚀', '🚀🚀🚀🚀', '🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀🚀', 
               '🚀🚀🚀🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀', '🌙', '🌙🌙', '🌙🌙🌙', '🚀📈', '📈'
              ]
    
    bearish = ['p', 'puts', 'put', 'losses', 'lose', 'loss', 'bear', 'bears', 'bearish', 'gay', 'sold', 'sell', 'selling',
               '🌈🐻', '🌈', '🐻', '😬', '😬😬'
              ]
    
    bullish_count = 0
    bearish_count = 0
    
    words = message.lower().split()
    for word in words:
        if word in bullish:
            bullish_count += 1
        elif word in bearish:
            bearish_count += 1
        return bullish_count
        return bearish count
            
        


