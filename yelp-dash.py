import requests
import csv
import collections

import dash 
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd 


map_box_token = 'pk.eyJ1IjoidGl6ZWJpIiwiYSI6ImNrNm84cGhpMDA3cHAzZW1paWR2dzR4MnMifQ.yZD21gter2HtNcrcIGqh8A'
bojangles_df = pd.read_csv('bojangles_yelp.csv')
bojangles_df = bojangles_df.drop_duplicates(subset=['biz_id'])
bojangles_df = bojangles_df[bojangles_df['name'].str.contains('Bojangles', case=False)]

bojangles_reviews = pd.read_csv('bojangles_yelp_reviews.csv')

bojangles_joined = pd.merge(bojangles_df, bojangles_reviews, how='inner', on='biz_id')

#######################################################################################

available_ratings = bojangles_joined['rating'].unique()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", 
"he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
"what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", 
"had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", 
"by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", 
"down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", 
"all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

############################Dictionary of Reviews######################################
# Citation for Positive + Negative Words
# ;   Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
# ;       Proceedings of the ACM SIGKDD International Conference on Knowledge 
# ;       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
# ;       Washington, USA, 
# ;   Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
# ;       and Comparing Opinions on the Web." Proceedings of the 14th 
# ;       International World Wide Web conference (WWW-2005), May 10-14, 
# ;       2005, Chiba, Japan.

# positive_words = []
# negative_words = []

# pos_txt = open('positive-words.txt', 'r')
# neg_txt = open('negative-words.txt', 'r')

# positive_words = [line.strip() for line in pos_txt]

# for line in neg_txt:
#     negative_words.append(line)

# pos_txt.close()
# neg_txt.close()

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
lst = word_counter.most_common(150)
word_counts = pd.DataFrame(lst, columns = ['Word', 'Count'])
word_counts['name'] = 'Bojangles'
word_counts.to_csv('review_word_counts.csv')

#######################################################################################

bojangles_map = px.scatter_mapbox(bojangles_df, lat='latitude', lon='longitude', color='rating', size='review_count', size_max=50, 
hover_name='name', hover_data=['state', 'city', 'rating', 'review_count'])

bojangles_map.update_layout(mapbox_style='light', mapbox_accesstoken=map_box_token)
bojangles_map.update_layout(margin={'r':0, 't':0,'l':0,'b':0})

bojangles_reviewer_ratings = px.bar(word_counts, x='Word', y='Count')

######################################################################################

app = dash.Dash()
app.title = 'Yelp'

#bootstrap CSS
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

#dash
app.layout = html.Div([
    dcc.Graph(id='graph', figure=bojangles_map),
    dcc.Graph(id='reviewer-bar', figure=bojangles_reviewer_ratings)
])

#callbacks
# @app.callback(
#     Output(component_id='my-div', component_property='children'),
#     [Input(component_id='my-id', component_property='value')]
# )
# def update_output_div(input_value):
#     return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)
