from bs4 import BeautifulSoup
import requests


def indian():
  url_in = 'https://indianexpress.com/'
  html_data = requests.get(url_in)
  soup = BeautifulSoup(html_data.text, 'html.parser')
  top_news = soup.find_all("div",   {"class": "other-article"})
  news_array = []
  for news in top_news:
    links = news.find('a')
    news_link = links.get('href')
    news_title = links.img.get('alt')
    image_link = links.img.get('src')
    new = {'title':news_title,
         'link':news_link,
       'image':'https:'+image_link
        }
    news_array.append(new)
  print(news_array)

def american():
  url_us = 'https://www.usatoday.com/'
  html_data = requests.get(url_us)
  soup = BeautifulSoup(html_data.text, 'html.parser')
  top_news = soup.find_all('a',{'class':'gnt_m_sl_a'})
  news_array = []
  for news in top_news:
    news_title = news.text
    image_link = news.img.get('data-gl-src')
    news_link = 'https://www.usatoday.com/'+news.get('href')
    new = {
      'title':news_title,
      'image':image_link,
      'link':news_link
    }
    news_array.append(new)
  print(news_array)
  


print('Choose the country, whose news you want.Press "in"-India, "us"-USA')

country = input('Enter country code :')
if country=='in':
  indian()
elif country=='us':
  american()
