import requests as r
from requests_oauthlib import OAuth1

auth = OAuth1(client_secret='7zscFaIVyue6M6iRN54KanBFezM', client_key="lolScraper")
subreddit = 'http://www.reddit.com/r/leaugeoflegends.json'
headers = {'User-Agent': 'python:lolscraper:0.01 (by /u/Lokkion)'}

r.get(url=subreddit, auth=auth, headers=headers)

