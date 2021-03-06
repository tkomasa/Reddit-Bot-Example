#!/usr/bin/python

# Imports
import praw
from random import randint

# Quote list
quote = ["ENTER QUOTES ARRAY HERE"]

# Reddit api login
reddit = praw.Reddit(client_id='client id here',
                     client_secret='client secret here',
                     username='reddit bot account username here',
                     password='reddit bot account password here',
                     user_agent='you should put your main/personal reddit account username here')

# Subreddit restrictions
subreddit = reddit.subreddit('REDDIT TO WATCH')

# Activation phrase
keyphrase = 'KEYPHRASE TO RESPOND TO'
second_keyphrase = 'SECONDARY KEYPHRASE'

# Look for keyphrase and respond
for comment in subreddit.stream.comments(skip_existing=True):
     if keyphrase in comment.body:
        try:
            reply = quote[randint(0, len(quote) - 1)]
            comment.reply(reply)
            print('posted for main call')
        except:
            print('error')
     if second_keyphrase in comment.body:
        try:
            reply = "SPECIFIC QUOTE"
            comment.reply(reply)
            print('posted for secondary call')
        except:
            print('error')
