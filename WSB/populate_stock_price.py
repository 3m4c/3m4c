import config
import alpaca_trade_api as tradeapi
import psycopg2
import psycopg2.extras


connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url = config.API_URL)


# collecting an array of [id, symbol] arrays from the stock table and storing them into the rows object
cursor.execute("""
    SELECT id, symbol, name FROM stock
""")
rows = cursor.fetchall()


# creating a dictionary where symbols are the keys and ids are the values:
# we need the ids in order to be able to reference the stock table
stock_dict = {}
for row in rows:
    symbol = row['symbol']
    stock_dict[symbol] = row['id']


# creating a list of the symbols we want to know the price data of (these are just examples, it's not definitive)
symbols = ['GME', 'AMC', 'CLOV', 'WISH', 'UWMC', 'CLNE', 'NOK', 'SPCE', 'PLTR', 'TSLA', 'WKHS', 'SPY', 'RKT', 'CRSR', 'BB']


# populating the stock_price table
barsets = api.get_barset(symbols, 'day')
for symbol in barsets:
    #print(f"processing symbol {symbol}")
    for bar in barsets[symbol]:
             stock_id = stock_dict[symbol]
             cursor.execute("""
                 INSERT INTO stock_price (stock_id, dt, open, high, low, close, volume)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)
             """, (stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c, bar.v))

connection.commit()
