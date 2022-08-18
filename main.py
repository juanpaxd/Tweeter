import json
from retweet import top_retweet
from tweeters import top_tweeters
from days import top_days
from hashtags import top_hashtags

f = open("dataset.json")
database = json.load(f)