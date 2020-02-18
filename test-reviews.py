import requests
import csv
import collections

# import dash 
# import dash_core_components as dcc 
# import dash_html_components as html
# from dash.dependencies import Input, Output

# import plotly.graph_objects as go
# import plotly.express as px

import pandas as pd 


# map_box_token = 'pk.eyJ1IjoidGl6ZWJpIiwiYSI6ImNrNm84cGhpMDA3cHAzZW1paWR2dzR4MnMifQ.yZD21gter2HtNcrcIGqh8A'
# bojangles_df = pd.read_csv('bojangles_yelp.csv')
# bojangles_df = bojangles_df.drop_duplicates(subset=['biz_id'])
# bojangles_df = bojangles_df[bojangles_df['name'].str.contains('Bojangles', case=False)]

bojangles_reviews = pd.read_csv('bojangles_yelp_reviews.csv')
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", 
"he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
"what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", 
"had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", 
"by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", 
"down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", 
"all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

############################Dictionary of Reviews######################################
count_words = {}
for reviews in bojangles_reviews['review']:
    list_of_words = reviews.split(' ')
    for word in list_of_words:
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")

        if word.lower() not in stop_words:
            if word.lower() in count_words:
                count_words[word.lower()] += 1
            else:
                count_words[word.lower()] = 1

word_counter = collections.Counter(count_words)
lst = word_counter.most_common(100)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])