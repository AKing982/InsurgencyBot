import praw
import reddit
import re
import datetime
from urllib.parse import quote_plus

# Create a list of keywords to search
key_word_list = ['Steyr', 'AUG', 'What do', 'The game is', 'I like', 'CPU issues ', 'weapons ', 'game issues']

# Create a list of keywords for CPU issues
cpu_issues_keywords = ['cpu issues', 'cpu performance', 'cpu problems', 'cpu bottleneck']

gpu_issues_keywords = ['gpu issues', 'gpu performance', 'gpu problems', 'gpu bottleneck']

opinion_keywords = ["What's your thoughts", "How do you think of", "How good is the game",
                  "how amazing is the game", "opinions", "Is sandstorm worth buying", "worth buying", "issues with game"]

steyr_aug_keywords = ['Steyr', 'AUG', 'steyr', 'aug']

# Create a dictionary to store different categories of comments
comment_categories = {'FPS Issues: ': [],
                      'GPU Issues: ': [],
                      'CPU Issues: ': [],
                      'Opinions: ': [],
                      'Steyr Aug: ': []}

def getHotComments():
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")


    for submission in subreddit.hot(limit=300):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)

           # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''

def getTopComments():
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.top(limit=300):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)

           # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''

def getRisingComments():
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.rising(limit=300):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            print(submission.title)
            comment = comment_queue.pop(0)

           # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''

def getNewComments():
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.new(limit=300):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)

           # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''

def main():

    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                     client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                     user_agent='<happy:q:1.0>')

    subreddit = reddit_api.subreddit("insurgency")

main()


