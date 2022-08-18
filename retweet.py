def top_retweet(database):
    top10 = database.sort(key=lambda x: x["retweetCount"])[0:10]
    return top10