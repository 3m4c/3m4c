CREATE TABLE sentiment_evolution (
  stock_id INTEGER NOT NULL,
  dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  stock_symbol TEXT NOT NULL,
  bullish_sentiment NUMERIC NOT NULL DEFAULT 0,
  bearish_sentiment NUMERIC NOT NULL DEFAULT 0,
  mention_post_id TEXT NOT NULL,
  PRIMARY KEY (stock_id, dt),
  CONSTRAINT fk_mention_stock FOREIGN KEY (stock_id) REFERENCES stock (id)
);

--I should probably also reference the mention table

CREATE INDEX ON sentiment_evolution (stock_id, dt DESC);
SELECT create_hypertable('sentiment_evolution', 'dt');
