import re
from collections import defaultdict
def top_hashtags(database):
    hashtags_dict = defaultdict(int)
    for tweet in database:
        pattern = r'\B(\#[a-zA-Z]+\b)(?!;)'
        hashtags = re.findall(pattern, tweet["description"])
        for hashtag in hashtags:
            hashtags_dict[hashtag] += 1
            
    top10 = sorted(hashtags_dict.items(), key=lambda x:x[1], reverse=True)[0:10]
    return top10