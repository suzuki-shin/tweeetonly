# -*- coding: utf-8 -*-

from twython import Twython
import sys
import os
from ConfigParser import SafeConfigParser as ConfigParser

# read config
config = ConfigParser()
config.read(os.path.expanduser('~/.tweeetonly'))
CONSUMER_KEY        = config.get('tweeetonly', 'consumer_key')
CONSUMER_SECRET     = config.get('tweeetonly', 'consumer_secret')
ACCESS_TOKEN        = config.get('tweeetonly', 'access_token')
ACCESS_TOKEN_SECRET = config.get('tweeetonly', 'access_token_secret')

argvs = sys.argv
text = argvs[1]

tw = Twython(
    twitter_token = CONSUMER_KEY,
    twitter_secret = CONSUMER_SECRET,
    oauth_token = ACCESS_TOKEN,
    oauth_token_secret = ACCESS_TOKEN_SECRET)
tw.updateStatus(status = text)
