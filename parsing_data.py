import requests
from bs4 import BeautifulSoup


# list_news = []

def show_new(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    n_new = soup.find('section', class_='article').text
    try:
        n_twitter_url = soup.find(
            'div', class_='twitter-embed').find('a').get('href')
        if 'Посмотреть твит' in n_new:
            nn_new = n_new.replace(
                'Посмотреть твит', f"Посмотреть твит -> {n_twitter_url}")
        return nn_new
    except AttributeError:
        return n_new


def Show_titles(itter):
    URL = 'https://stopgame.ru/news/all/p' + str(itter)
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    soup_titles_news = soup.find_all('div', class_='caption caption-bold')
    list_urls_news = [i.find('a').get('href') for i in soup_titles_news]
    list_titles_news = [i.text.strip() for i in soup_titles_news]
    return [list_titles_news, list_urls_news]


# a = Show_titles(1)
# b = a[1]
# print(b)
