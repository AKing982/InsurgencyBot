import praw
import reddit
import re
from urllib.parse import quote_plus

# Create a list of keywords to search
key_word_list = ['Steyr', 'AUG', 'What do you think ', 'The game is ', 'I like the game ', 'CPU issues ', 'weapons ', 'game issues']
# Create a list of keywords for CPU issues
keywords_cpu = ['CPU']


# Create a dictionary to store different categories of comments
comment_categories = {'FPS Issues: ': [],
                      'GPU Issues: ': [],
                      'CPU Issues: ': [],
                      'Opinions: ': [],
                      'Steyr Aug: ': []}


def getHotComments(user_sub_limit):
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.hot(limit=user_sub_limit):
        for comment in submission.comments:
          



    return ''




def main():

    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                     client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                     user_agent='<happy:q:1.0>')

    subreddit = reddit_api.subreddit("insurgency")

    # Ask the user for the topic, i.e. hot, top, new
    user_topic = input("Enter the topic to be searched: ")

    # Ask the user for the number of submissions to be searched
    user_sub_limit = int(input("Enter the desired number of submissions to be searched: "))

    if user_topic == 'hot':
        print(getHotComments(user_sub_limit))

main()


