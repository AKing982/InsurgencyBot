import praw
import reddit
from urllib.parse import quote_plus


def main():

    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                     client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                     user_agent='<happy:q:1.0>'
)

if "__name__" == "__main__":
    main()
    
