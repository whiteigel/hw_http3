from pprint import pprint
import requests
import time
import datetime

# option 1

def get_news(keyword, fromdate, todate):
    news = {}
    keyword = keyword
    fromdate = int(time.mktime(datetime.datetime.strptime(fromdate, "%d/%m/%Y").timetuple()))
    todate = int(time.mktime(datetime.datetime.strptime(todate, "%d/%m/%Y").timetuple()))
    url = "https://api.stackexchange.com/2.3/questions?"
    params = {"fromdate": fromdate,
              "todate": todate,
              "order": "asc",
              "sort": "activity",
              "tagged": keyword,
              "site": "stackoverflow",
              "filter": "!nKzQUR30W7"}
    response = requests.get(url=url, params=params)
    res = response.json()['items']
    if response.status_code != 200:
        print("ERROR")
    for ind, elm in enumerate(res):
        title = elm['title']
        q_link = elm['link']
        body = elm['body_markdown']
        news = [title, q_link, body]
        print(news)
        # news[title] = [q_link, body]
        # return news

# option 2

# def get_news(keyword, fromdate, todate):
#     news = {}
#     keyword = keyword
#     fromdate = int(time.mktime(datetime.datetime.strptime(fromdate, "%d/%m/%Y").timetuple()))
#     todate = int(time.mktime(datetime.datetime.strptime(todate, "%d/%m/%Y").timetuple()))
#     url = f"https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&todate={todate}&order=asc&sort=activity&tagged={keyword}&site=stackoverflow"
#     response = requests.get(url=url)
#     res = response.json()['items']
#     if response.status_code != 200:
#         print("ERROR")
#     for ind, elm in enumerate(res):
#         title = elm['title']
#         q_link = elm['link']
#         news[title] = q_link
#     return news

if __name__ == '__main__':
    pprint(get_news('Python', '06/07/2021', '08/07/2021'))


