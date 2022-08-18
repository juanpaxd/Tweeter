from collections import defaultdict
def top_tweeters(database):
    users = defaultdict(0)
    for tweet in database:
        users[tweet["user"]] += 1
    top10 = sorted(users.items(), key=lambda x:x[1], reverse=True)[0:10] #Array
    return top10