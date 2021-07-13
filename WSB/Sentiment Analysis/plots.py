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
    '''SELECT stock_symbol, dt, bullish_sentiment, bearish sentiment FROM sentiment_evolution'''
)
rows = cursor.fetchall()

# df = pd.DataFrame(data = rows)

sns.relplot(
    data=rows, kind="line",
    x="dt", y="bullish_sentiment", col="align",
    hue="stock_symbol", size="coherence", style="choice"
    #facet_kws=dict(sharex=False),
)
