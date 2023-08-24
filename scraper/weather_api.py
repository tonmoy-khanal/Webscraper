import requests
import json
import pandas as pd


class Weather_API:

    def __init__(self, keyword):
        self.keyword = keyword

    def json_print(self, obj):
        with open('api_data.txt', 'w') as json_file:
            json.dump(obj, json_file)
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def create_dataframe(self, obj):
        FIELDS = ["source.id", "source.name", "author", "title", "description", "url", "urlToImage", "publishedAt",
                  "content"]
        df = pd.json_normalize(obj['articles'])
        final_df = df[FIELDS]
        display(final_df.head())

    def news_api(self):
        url = ('https://newsapi.org/v2/everything?'
               'q={keyword}&'
               'apiKey=4e70cabb80884db08524a28ac33cdc1d'.format(keyword=self.keyword))

        response = requests.get(url)
        if response.status_code == 200:
            print('API call successful!')
            json_response = response.json()
            if len(json_response['articles']) == 0:
                print('No News Articles Found')
            else:
                self.json_print(json_response)
                self.create_dataframe(json_response)
        else:
            print('Status code:', response.status_code)