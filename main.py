import functions as lol
import time
import json
import os
import datetime

directory = '/Users/lukegriffith/Documents/lolScraper/json/' +\
    datetime.date.today().strftime("%d%m%y") + "/"

if not os.path.exists(directory):
    os.makedirs(directory)

t3 = lol.LoadSubreddit('leagueoflegends')
after = t3.get('data').get('after')


with open(directory + 't3.json', 'w') as outfile:
    json.dump(t3, outfile)


for post in t3.get('data').get('children'):
    url = post.get('data').get('url')
    postID = post.get('data').get('id')
    time.sleep(1.5)
    comments = lol.loadComments(url)
    with open(directory + postID + '.json', 'w') as outfile:
        json.dump(comments, outfile)
    time.sleep(2.5)


for x in 1, 2:
    t3 = lol.loadAfter('leagueoflegends', after)
    after = t3.get('data').get('after')

    with open(directory + 't3_' + x + '.json', 'w') as outfile:
        json.dump(t3, outfile)

    for post in t3.get('data').get('children'):
        url = post.get('data').get('url')
        postID = post.get('data').get('id')
        comments = lol.loadComments(url)
        with open(directory + postID + '.json', 'w') as outfile:
            json.dump(comments, outfile)
        time.sleep(2.5)