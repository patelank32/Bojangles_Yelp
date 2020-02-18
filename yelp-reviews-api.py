import requests
import csv

import pandas as pd 

# Store Yelp API Key
client_id = '7QcreiNcfG2XG4IiEgZjvw'
api_key = 'jC8sHyC_kBuPe9Og5AQTAKAqsW84aYmambIJRJ0DvUPYZ1ujkY_frrts1Qb8ZT8wjBN1P9W1xtldTm9_1E7zS1oQ7KnrMIdZIh1FHze4BNkqaEtA1O1GYa7AC75IXnYx'

reviews_df = pd.read_csv('chickfila_yelp.csv')
reviews_df = reviews_df.drop_duplicates(subset=['biz_id'])
reviews_df = reviews_df[reviews_df['name'].str.contains('Chick-fil-A', case=False)]
print(reviews_df.shape)
print(reviews_df.head)

#Set endpoint for business search and authenticate

HEADERS = {'Authorization': 'bearer %s' % api_key}

column_headers = ['biz_id', 'review_id', 'review_rating', 'reviewer_name', 'review', 'time_created', 'url']
f = open('chickfila_yelp_reviews.csv', 'w')
writer = csv.writer(f)
writer.writerow(column_headers)

for biz_id in reviews_df['biz_id']:
    ENDPOINT ='https://api.yelp.com/v3/businesses/' + biz_id + '/reviews'
    response = requests.get(url=ENDPOINT, headers=HEADERS)
    bojangles_reviews = response.json()
    print(bojangles_reviews)

    for jangle in bojangles_reviews['reviews'][:5]:
        #include biz_id
        review_id = jangle['id']
        review_rating = jangle['rating']
        reviewer_name = jangle['user']['name']
        review = jangle['text']
        time_created = jangle['time_created']
        url = jangle['url']

        writer.writerow([biz_id, review_id, review_rating, reviewer_name, review, time_created, url])

f.close()