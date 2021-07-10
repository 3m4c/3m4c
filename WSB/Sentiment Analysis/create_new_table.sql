CREATE TABLE sentiment_evolution (
  stock_id INTEGER NOT NULL,
  dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  stock_symbol TEXT NOT NULL,
  stock_sentiment NUMERIC NOT NULL,
  mention_id TEXT NOT NULL
);

CREATE INDEX ON sentiment_evolution (stock_id, dt DESC);
SELECT create_hypertable('sentiment_evolution', 'dt');
