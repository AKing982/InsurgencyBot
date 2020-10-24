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
                     user_agent='<happy:q:1.0>'


)



def getHotComments():

def getNewComments():

def getRisingComments():

def getTopComments():


if "__name__" == "__main__":
    main()
    
