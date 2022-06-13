from itertools import count
from pytz import timezone
import tweepy

import collections
from collections import abc
collections.MutableMapping = abc.MutableMapping
collections.Iterable = abc.Iterable
collections.Mapping = abc.Mapping
from apscheduler.schedulers.blocking import BlockingScheduler


def autenticate(): 
    auth = tweepy.OAuth1UserHandler(
    consumer_key= 'yourkey',
    consumer_secret= 'yourkey',
    access_token= 'yourkey',
    access_token_secret='yourkey'
    )

    barrier_token = 'yourkey'

    api = tweepy.API(auth, wait_on_rate_limit=True)
    client = tweepy.Client(barrier_token)
    

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    
    return api


def tobyIsback(api):
    
    def __init__(self):
        self.api = api   

    tweets_search = api.search_tweets('toby is back|Toby is back',result_type ='recent', count=3)

    for tweet in tweets_search:
        
        if 'toby is back' in tweet.text or 'Toby is back' in tweet.text:
            id = tweet.id
            try:
                print(f'curtindo o tweet {id} de {tweet.author.name}, texto = {tweet.text}')
                
                api.create_favorite(id)
                
                
                file = open('nogod.mp4', 'rb')
                video = api.media_upload(filename='nogod.mp4', file=file)
                api.update_status(
                    status = f'@{tweet.author.screen_name} No god please, no, noooooooo!',
                    in_reply_to_status_id = id,
                    media_ids = [video.media_id_string]
                )
                print(f'==Tweety de {tweet.author.name} curtido e respondido==')
            except Exception as e:
                print(e)
                print('--pulando para o proximo tweet')
                continue 


            

sched = BlockingScheduler()
sched.configure(timezone='America/Cayenne')

api = autenticate()

#@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('--Nova execução--')
    
    tobyIsback(api) 

sched.add_job(timed_job, 'cron', day_of_week='mon-sun', hour='12-20', minute='0-59/1')

sched.start()







        


