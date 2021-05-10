import datetime
import pandas as pd
from psaw import PushshiftAPI

api = PushshiftAPI()

# Creating a list, which is then transformed into empty dataframe (I don't know if it's necessary)
list1 = [{"Timestamp": 0}]
df = pd.DataFrame(list1)

# i are days following start date
for i in range(0, 365):

    #Start date + i days
    posted_after = int(datetime.datetime(2017, 12, 1).timestamp()) + 86400*i

    #Date after start date (needed as upper bound of time interval) + i days
    posted_before = int(datetime.datetime(2017, 12, 2).timestamp()) + 86400*i

    # limit is number of comments in current day
    # We can also try to replace it with search_submissions
    query = list(api.search_comments(subreddit='Bitcoin', after=posted_after, before=posted_before, limit=200))

    # Creating temporary dataframe with comments from current day and integer datetime code of that date
    dfTemp = pd.DataFrame([comment.body for comment in query])
    dfTemp['Timestamp'] = posted_after

    #Appending current date comments to main dataframe
    df = df.append(dfTemp)

    #Once in 10 iterations display iteration number
    if i % 10 == 0:
        print(i)

#Save final dataframe to
df.to_csv("C:/Users/Marek/Documents/reddit.csv")

