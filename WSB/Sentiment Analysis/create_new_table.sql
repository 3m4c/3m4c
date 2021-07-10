CREATE TABLE sentiment_evolution (
  stock_id INTEGER NOT NULL,
  dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  stock_symbol TEXT NOT NULL,
  mention_post_id TEXT NOT NULL,
  bullish_sentiment NUMERIC NOT NULL DEFAULT 0,
  bearish_sentiment NUMERIC NOT NULL DEFAULT 0
);

CREATE INDEX ON sentiment_evolution (stock_id, dt DESC);
SELECT create_hypertable('sentiment_evolution', 'dt');
