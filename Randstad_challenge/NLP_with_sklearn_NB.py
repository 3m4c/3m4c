import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

train_df = pd.read_csv('Dataset_Randstad-Challenge/train_set.csv')
test_df = pd.read_csv('Dataset_Randstad-Challenge/test_set.csv')

X_train, y_train = train_df['Job_offer'], train_df['Label']
X_test, y_test = test_df['Job_offer'], test_df['Label']

labels = {'Java Developer':0, 'Software Engineer':1, 'Programmer':2, 'System Analyst':3, 'Web Developer':4}
y_train = np.array([labels[label] for label in y_train], dtype=np.float32)
y_test = np.array([labels[label] for label in y_test], dtype=np.float32)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)

print(metrics.classification_report(y_test, predicted)
