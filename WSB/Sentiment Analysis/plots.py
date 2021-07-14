import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER,
                              password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute(
    '''SELECT stock_symbol, dt, bullish_sentiment, bearish_sentiment FROM sentiment_evolution'''
)
rows = cursor.fetchall()

df = pd.DataFrame(data = rows, columns=('stock_symbol', 'dt', 'bullish_sentiment', 'bearish_sentiment'))

sorted_values = df.sort_values('stock_symbol')

stock_to_plot = sorted_values[sorted_values['stock_symbol'] == 'AMC']
del stock_to_plot['stock_symbol']

#create new column to hold exponentially weighted moving average
stock_to_plot['1dayEWM'] = stock_to_plot['bullish_sentiment'].ewm(span = 50, adjust=False).mean()
print(stock_to_plot.head(20))
stock_to_plot = stock_to_plot.melt('dt', var_name='cols',  value_name='vals')


sns.relplot(
    data=stock_to_plot, kind="line",
    x = 'dt', y='vals', hue = 'cols'
)

plt.show()
