import praw
import reddit
from urllib.parse import quote_plus

# Create a list of keywords to search
key_word_list = ['Steyr', 'AUG', 'What do you think ', 'The game is ', 'I like the game ', 'CPU issues ']

# Create a dictionary to store different categories of comments
comment_categories = {'FPS Issues: ': [],
                      'GPU Issues: ': [],
                      'CPU Issues: ': [],
                      'Opinions: ': [],
                      'Steyr Aug: ': []}

def main():

    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                     client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                     user_agent='<happy:q:1.0>')

    subreddit = reddit_api.subreddit("insurgency")

    # Ask the user for the topic, i.e. hot, top, new
    user_topic = input("Enter the topic to be searched: ")

    # Ask the user for the number of submissions to be searched
    user_sub_limit = input("Enter the desired number of submissions to be searched: ")

    if user_topic == 'hot' or user_topic == 'Hot':
        print(getHotComments(user_topic, user_sub_limit))
    elif user_topic == 'top' or user_topic == 'Top':
        print(getTopComments(user_topic, user_sub_limit))
    elif user_topic == 'Rising' or user_topic == 'rising':
        print(getRisingComments(user_topic, user_sub_limit))
    elif user_topic == 'new' or user_topic == 'New':
        print(getNewComments(user_topic, user_sub_limit))
        







def getHotComments(user_topic, user_sub_limit):

def getNewComments(user_topic, user_sub_limit):

def getRisingComments(user_topic, user_sub_limit):

def getTopComments(user_topic, user_sub_limit):


if "__name__" == "__main__":
    main()
    
