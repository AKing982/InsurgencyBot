import praw
import reddit
import re
from urllib.parse import quote_plus

# Create a list of keywords to search
key_word_list = ['Steyr', 'AUG', 'What do', 'The game is', 'I like', 'CPU issues ', 'weapons ', 'game issues']

# Create a list of keywords for CPU issues
cpu_issues_keywords = ['cpu issues', 'cpu performance', 'cpu problems', 'cpu bottleneck']

gpu_issues_keywords = ['gpu issues', 'gpu performance', 'gpu problems', 'gpu bottleneck']

opinion_keywords = ["What's your thoughts", "How do you think of", "How good is the game", "how amazing is the game",
                    "opinions", "Is sandstorm worth buying",
                    "worth buying", "issues with game"]

steyr_aug_keywords = ['Steyr', 'AUG', 'steyr', 'aug']

# Create a dictionary to store different categories of comments
comment_categories = {'FPS Issues: ': [],
                      'GPU Issues: ': [],
                      'CPU Issues: ': [],
                      'Opinions: ': [],
                      'Steyr Aug: ': []}


def get_hot_comments(user_sub_limit, user_question):
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.hot(limit=user_sub_limit):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)
            if len(comment.body) > 5:
                comment_body = comment.body.lower()
                # If the user_question is about cpu issues get comments relating to cpu issues
                if user_question in cpu_issues_keywords:
                    print("Submission: ", submission.title)
                    print("Comments ", comment.body)
                    print("---------")
                    print()

                # Else if the user_question is about fps issues get comments relating to fps issues
                if user_question in opinion_keywords:
                    # If any of the comments are related to opinions return that comment
                    if any(opinion in comment_body for opinion in opinion_keywords):
                        print("Submission: ", submission.title)
                        print("Comments")
                        print("---------")
                        print(comment.body)
                        print()

                # Else if the user_question is about gpu issues get comments relating to gpu issues

                # Else if the user_question is about opinions of the game get comments relating to opinions

            # print(comment.body)

            comment_queue.extend(comment.replies)

    return ''


def get_top_comments(user_sub_limit, user_question):
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.top(limit=user_sub_limit):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)
            for words in steyr_aug_keywords:
                if words.lower() in comment.body:
                    print(comment.body)

            # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''


def get_rising_comments(user_sub_limit, user_question):
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.rising(limit=user_sub_limit):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            print(submission.title)
            comment = comment_queue.pop(0)
            for words in opinion_keywords:
                if words.lower() in comment.body:
                    print(comment.body)

            # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''


def get_new_comments(user_sub_limit, user_question):
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')
    subreddit = reddit_api.subreddit("insurgency")

    for submission in subreddit.new(limit=user_sub_limit):
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)
            for words in opinion_keywords:
                if words.lower() in comment.body:
                    print(comment.body)

            # print(comment.body)
            comment_queue.extend(comment.replies)

    return ''


def get_user_info():
    # Ask the user for the topic, i.e. hot, top, new
    user_topic = input("Enter the topic to be searched: ")
    # Ask the user for the number of submissions to be searched
    user_sub_limit = int(input("Enter the desired number of submissions to be searched: "))
    # Ask the user what issue they want to search
    user_question = input('Enter the desired issue to be searched: ')
    if user_topic == 'hot'.lower():
        print(get_hot_comments(user_sub_limit, user_question))
    elif user_topic == 'top'.lower():
        print(get_top_comments(user_sub_limit, user_question))
    elif user_topic == 'rising'.lower():
        print(get_rising_comments(user_sub_limit, user_question))
    elif user_topic == 'new'.lower():
        print(get_new_comments(user_sub_limit, user_question))


def main():
    reddit_api = praw.Reddit(client_id='sWoQ6hSvdJueiw',
                             client_secret='4JYNsj4ZgzxL1gFSfbjeB2yFMLA',
                             user_agent='<happy:q:1.0>')

    subreddit = reddit_api.subreddit("insurgency")

    get_user_info()


if "__name__" == "__main__":
    main()
