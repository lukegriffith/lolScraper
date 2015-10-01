import requests as r
import json
headers = {'User-Agent': 'python:lolscraper:0.01 (by /u/Lokkion)'}


def LoadSubreddit(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit +\
        "/top/.json?sort=top&t=month&limit=100"
    content = r.get(url=url, headers=headers)
    lol = json.loads(content.text)
    return lol


def loadAfter(subreddit, after):
    url = 'http://www.reddit.com/r/' + subreddit +\
        "/top/.json?sort=top&t=month&limit=100&after=" + after
    content = r.get(url=url, headers=headers)
    lol = json.loads(content.text)
    return lol


def loadComments(permaLink):
    url = permaLink + '.json?sort=hot&limit=100'
    content = r.get(url=url, headers=headers)
    lol = json.loads(content.text)
    return lol
