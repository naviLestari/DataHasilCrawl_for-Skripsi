#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import csv


# In[ ]:


consumer_key = 'J3dN7EpnWwexP1OB67TWURMpw'
consumer_secret = 'yE1Sr7OBpUmeALHXmIaArHRdIlYfV8Hs7kVnEjEPmXXNxi84WM'
access_token = '566327625-WNktUnm0KdI1eTtUVuVvqlVxqD5ARt1WJOzFYOVw'
access_token_secret = 'oycg0wk6QaV2FfmE4NKjp80rPzSTZJMUWAVybaxsfRYGf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('Indihome_TesCrawl_1.csv', 'a', encoding= 'utf-8')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="@indihome",count=50,
                           lang="id",
                           since="2019-01-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text])


# In[ ]:




