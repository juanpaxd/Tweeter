from collections import defaultdict
def top_days(database):
    days = defaultdict(0)
    for tweet in database:
        date = tweet["date"].split("T")[0]
        days[date] += 1
    top10 = sorted(days.items(), key=lambda x:x[1]) #Array
    return top10