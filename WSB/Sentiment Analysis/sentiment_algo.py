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
    
    bullish = ['moon', 'mars', 'yolo', 'all', 'strong', "can't", 'tits', 'c', 'calls', 'call', 'btfd', 'undervalued', 'gains', 'bull', 'bulls', 'bullish', 
               'buy', 'dip', 'fuel', 'fire', 'squeeze', 'squeezing', 'squoze', 'squozing', 'holding',
               '💎', '🤲', '💎🤲', '🤤🤤🤤', '🌝', '💎🤲🚀', '💎🙌🏻', '🙌🏻', '💎💎🙌🙌', '🚀💎👐', '💎✋🚀', 
               '🦍', '🦍🦍', '🦍🦍🦍', '🦍🦍🦍🦍', '🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍🦍', '🦍🦍🦍🦍🦍🦍🦍🦍',
               '🚀', '🚀🚀', 🚀🚀🚀', '🚀🚀🚀🚀', '🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀🚀', 
               '🚀🚀🚀🚀🚀🚀🚀🚀🚀', '🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀', '🌙', '🌙🌙', '🌙🌙🌙', '🚀📈', '📈'
              ]
    bearish = ['p', 'puts', 'put', 'losses', 'lose', 'bear', 'bears', 'bearish', 'gay',  '🌈🐻', '🌈', '🐻',
               '😬', '😬😬',]
    
    bullish_count =
    bearish_count = 
    
    words = message.lower().split()
    for word in words:
        if word in bullish:
            
        elif word in bearish:
            
        


