from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq 

import pandas as pd 

bojangles_df = pd.read_csv('bojangles.csv')

def get_url_list(df):
    url_list = []
    for url in df['url']:
        url_list.append(url)
    return url_list

url_list = get_url_list(bojangles_df)
reviews_df = pd.DataFrame()


my_url = 'https://www.yelp.com/biz/bojangles-famous-chicken-n-biscuits-charlotte-23?adjust_creative=7QcreiNcfG2XG4IiEgZjvw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=7QcreiNcfG2XG4IiEgZjvw' 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')
reviews = page_soup.findAll('div', {'class': 'lemon--div__373c0__1mboc i-stars__373c0__Y2F3O i-stars--regular-3__373c0__1DXMK border-color--default__373c0__YEvMS overflow--hidden__373c0__3Usf-'})
print(reviews[0])

for url in url_list:
    #transfer code for scrapping
    pass


