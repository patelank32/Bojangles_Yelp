import requests
import csv

import pandas as pd 

# Store Yelp API Key
client_id = '7QcreiNcfG2XG4IiEgZjvw'
api_key = 'jC8sHyC_kBuPe9Og5AQTAKAqsW84aYmambIJRJ0DvUPYZ1ujkY_frrts1Qb8ZT8wjBN1P9W1xtldTm9_1E7zS1oQ7KnrMIdZIh1FHze4BNkqaEtA1O1GYa7AC75IXnYx'

# Set endpoint for business search and authenticate
ENDPOINT ='https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % api_key}

# Get list of Bojangles Cities
city_df = pd.read_csv('bojangle_city.csv')

city_list = []
for index, row in city_df.iterrows():
    city_list.append(row['city'] + ', ' + row['abb'])

# # Set parameters of request term: bojangles location: charlotte
# PARAMETERS = {'term' : 'bojangles', 'location' : 'Charlotte'}

# Make request and convert to json


# Create a csv file to store api data in 
column_headers = ['biz_id', 'name', 'rating', 'review_count', 'url', 'image_url', 'latitude', 'longitude', 'city', 'state', 'address', 'zip_code']
f = open('chickfila_yelp.csv', 'w')
writer = csv.writer(f)
writer.writerow(column_headers)

for city in city_list:
    PARAMETERS = {'term': 'Chick-fil-A', 'location': city}
    response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
    bojangles =  response.json()
    print(city)

# iterate through businesses to get the wanted data
    for jangle in bojangles['businesses']:
        biz_id = jangle['id']
        name = jangle['name']
        rating = jangle['rating']
        review_count = jangle['review_count']
        url = jangle['url']
        image_url = jangle['image_url']
        latitude = jangle['coordinates']['latitude']
        longitude = jangle['coordinates']['longitude']
        city = jangle['location']['city']
        state = jangle['location']['state']
        address = jangle['location']['address1']
        zip_code = jangle['location']['zip_code']

        writer.writerow([biz_id, name, rating, review_count, url, image_url, latitude, longitude, city, state, address, zip_code])

# close csv file
f.close()

