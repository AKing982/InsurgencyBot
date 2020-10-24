import praw
import reddit
import re
from urllib.parse import quote_plus

# Create a list of keywords to search
key_word_list = ['Steyr', 'AUG', 'What do you think ', 'The game is ', 'I like the game ', 'CPU issues ', 'weapons ', 'game issues']
# Create a list of keywords for CPU issues
keywords_cpu = ['CPU']
opinion_keywords = ["What's your opinion of the game? ", "What's your thought's on the game?", "How good is this game?",
                    ]


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
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)
            for opinion in opinion_keywords:
                if opinion in comment.body:
                    print(comment.body)
                else:
                    break

           # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''

def getTopComments(user_sub_limit):
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.top(limit=user_sub_limit):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)
            print("Comment: ")
            print(comment.body)
            comment_queue.extend(comment.replies)
            print("--------------------")

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

    if user_topic == 'hot'.lower():
        print(getHotComments(user_sub_limit))
    elif user_topic == 'top'.lower():
        print(getTopComments(user_sub_limit))


main()


