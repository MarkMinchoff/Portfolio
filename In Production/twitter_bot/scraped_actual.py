import requests
import tweepy
import os
import bs4
from bs4 import BeautifulSoup
from os import getenv

def post_tweet(event, context):

     #scraper
     url = "https://www.phillypolice.com/crime-maps-stats/"
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'html.parser')
     homicides = soup.find_all(class_="homicides-count")[0].get_text()
     date  = soup.find_all(class_="text-xl font-bold")[0].get_text()
     change = soup.find_all(class_="homicides-change")[0].get_text()
     death = homicides.strip()
     time = date.strip()
     diff = change.strip()

     #twitter credentials
     auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_SECRET_KEY'))
     auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
     api = tweepy.API(auth)

     #tweet posting data
     tweet = f'As of {time} there have been a total of {death} victims of homicide this year in Philadelphia. This is a change of {diff} since last year. #philadelphia #philly'
     status = api.update_status(status=tweet)

     return 'Tweet Posted'
