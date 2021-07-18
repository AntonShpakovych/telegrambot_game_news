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
    URL = 'https://stopgame.ru/news/all/p' + itter
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    soup_titles_news = soup.find_all('div', class_='caption caption-bold')
    list_titles_news = [i.text.strip() for i in soup_titles_news]
    return list_titles_news


def Show_urls(itter):
    URL = 'https://stopgame.ru/news/all/p' + itter
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    soup_titles_news = soup.find_all('div', class_='caption caption-bold')
    list_titles_url = [i.find('a').get('href') for i in soup_titles_news]
    return list_titles_url
