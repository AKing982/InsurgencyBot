import praw
import reddit
import re
import datetime
from urllib.parse import quote_plus

# Create a list of keywords to search
key_word_list = ['Steyr', 'AUG', 'What do', 'The game is', 'I like', 'CPU issues ', 'weapons ', 'game issues']


opinion_keywords = ["opinion", "thoughts", "best about insurgency", "is it fun?", "is it fun", "worth buying?", "worth buying"]

sys_requirements = ["system requirements", "system specs", "pc specs", "PC Specs", "hardware", "memory", "gpu", "cpu",
                    "motherboard", "RAM", "ram", "i7", "rtx", "RTX", "GPU", "specs", "mobo"]

opinion_submissions = ["What are your opinions", ""]


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

            # If the comment has 5 or more words
            if len(comment.body) > 5:
                comment_body = comment.body.lower()

                # If each comment get those that have phrases in sys_requirements
                for questions in sys_requirements:
                    if questions in comment_body:
                        print("Sys Requirements")
                        print("Submission: ", submission.title)
                        print("Comments")
                        print(comment.body)
                        print()
                        break

                # If any comment has phrases in opinion_keywords
                for questions in opinion_keywords:
                    if questions in comment_body:
                        print("Opinions")
                        print("Submission: ", submission.title)
                        print("Comments")
                        print(comment.body)
                        print()

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

    print(getHotComments())


main()


