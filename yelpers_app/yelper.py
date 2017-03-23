from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
   auth = Oauth1Authenticator(
    consumer_key='d63PDSoUjdixe0A6z9Wm0Q',
    consumer_secret='pT9Hy6lBdYdRlD9ci5gq1ljndpc',
    token='G7uVzh6n0LLAIX3wRYkqYBFLVwZKkULp',
    token_secret='J94JOrcmxwD2VkJ4mMWJ5nbtbn0'
)

   client = Client(auth)

   params = {
       'term': term,
       'lang': 'en',
       'limit': 10
   }

   response = client.search(location, **params)

   businesses = []

   for business in response.businesses:
       # print (business.name, business.rating, business.phone)
       businesses.append({"name": business.name,
           "rating": business.rating,
           "phone": business.phone
           })

   return businesses