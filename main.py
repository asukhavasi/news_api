import requests
import smtplib

from email_send import send_email

topic = 'ford'
news_api = '50dfa446388b4f3c8cb3db298f1122b2'
news_url = ('https://newsapi.org/v2/everything?'\
            f'q={topic}&from=2024-12-09&sortBy'\
            '=publishedAt&apiKey=50dfa446388b4f3c8cb3db298f1122b2&language=en')
request = requests.get(news_url)

content = request.json()

body = ''
for article in content["articles"][:5]:
    title = article["title"]
    description = article['description']


    raw_message1 = str(title) + '\n' + str(description) +'\n' + article['url']+2*'\n'
    body += raw_message1

    message = f"""\
Subject: News update.
{body}
"""
message = message.encode("utf-8")
send_email(message)
