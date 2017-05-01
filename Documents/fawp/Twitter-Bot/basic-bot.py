# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:11:17 2017

@author: joel
"""

import tweepy, sys, time

argfile = str(sys.argv[1])

CONSUMER_KEY = 'SeYjLYZr5XjpCNw28j8KxbuwY'
CONSUMER_SECRET = '4xTSu9ulPLbtthsC9IaTkxgoIDpRd7wlbsbIST29skPwtQvrYi'
ACCESS_KEY = '797920179678285824-a52Zj2mbthEr7A36il3UaW2laJ2web1' 
ACCESS_SECRET = '7ThiAslAOhlr7UZjC2ywkur5veRxPBM7J7M0MxJZ5Th54'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes