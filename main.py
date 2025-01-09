import requests


news_api = '50dfa446388b4f3c8cb3db298f1122b2'
news_url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-12-09&sortBy=publishedAt&apiKey=50dfa446388b4f3c8cb3db298f1122b2'
request = requests.get(news_url)

content = request.json()
# print(type(content))
# print(content["articles"])


for article in content["articles"]:
    print(f"title: {article["title"]}")
    print(f"description: {article['description']}+\n")