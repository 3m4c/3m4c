import config
import datetime as dt
from psaw import PushshiftAPI     # Pushshift is a database which contains all Reddit's posts
import praw                       # praw is the Reddit API, and it is useful to know the score and the number of comments of a post
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host = config.DB_HOST, database = config.DB_NAME, user = config.DB_USER, password = config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
reddit = praw.Reddit(client_id =config.R_KEY, client_secret =config.R_SECRET, username =config.R_USERNAME, password =config.R_PASSWORD, user_agent = 'https://github.com/3m4c')
api = PushshiftAPI()


# creating a dictionary whose keys are the tickers with the $ sign (e.g. $GME) 
# and the values are their ids from the stock table
cursor.execute(
    '''SELECT * FROM stock'''
)
rows = cursor.fetchall()
stocks = {}
for row in rows:
    stocks['$' + row['symbol']] = row['id']

# scraping posts from start_time to end_time (we can choose any interval we want)
start_time = int(dt.datetime(2021, 1, 1).timestamp())
endtime = int(dt.datetime(2021, 6, 20).timestamp())
submissions = api.search_submissions(after = start_time,
                                         before = endtime,
                                         subreddit = 'wallstreetbets',
                                         filter = ['url', 'author', 'title', 'subreddit', 'id']
                                          )

# iterating through the submissions (posts)
for submission in submissions:

    # splitting the title into words: any $ticker get (temporarily) stored in the cashtags list
    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    # many sumbmissions do not have a ticker, therefore we can discard them
    if len(cashtags) > 0:

        # iterating through the tickers, if there are more than one in a single post
        for cashtag in cashtags:
            
            # we use Pushshift to extract the submission id, then we use Reddit to extract the score of that submission
            submission_id = submission.id
            sub_praw = reddit.submission(submission_id)
            score = sub_praw.score
            
            # we only need the posts with greater visibility
            if score > 100:
                
                # finally, we can fetch all the data we need
                submitted_time = dt.datetime.fromtimestamp(submission.created_utc).isoformat()
                num_comments = sub_praw.num_comments

                try:
                    cursor.execute('''
                    INSERT INTO mention (dt, stock_id, message, url, post_id, score, num_comments)
                    VAlUES (%s, %s, %s, %s, %s, %s, %s)
                    ''', (submitted_time, stocks[cashtag], submission.title, submission.url, submission_id, score, num_comments))
                    connection.commit()

                except Exception as e:
                    print(e)
                    connection.rollback()
