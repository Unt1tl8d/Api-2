import requests
import os
from dotenv import load_dotenv


load_dotenv()
url = 'https://api.vk.ru/method/'
token = os.environ['TOKEN']
short_url = input('Введите ссылку:')


def shorten_link(token, url):
    check_url = requests.get(short_url)
    check_url.raise_for_status()
    parm = {
        'url': short_url,
        "access_token": token,
        "v": '5.199 HTTP/1.1'
    }
    response = requests.get(f'{url}utils.getShortLink', params=parm)
    output = response.json()['response']
    return output['short_url']


def count_clicks(token, url):
    check_url = requests.get(short_url)
    check_url.raise_for_status()
    parm = {
        "access_token": token,
        'key': short_url.replace('https://vk.cc/', ''),
        "interval": 'forever',
        "v": '5.199 HTTP/1.1'
    }
    response = requests.get(f'{url}utils.getLinkStats', params=parm)
    response.json()
    output = response.json()["response"]
    stats = output['stats']
    views = stats[-1]
    return  views['views']


def is_shorten_link(url, short_url):
    if "vk.cc" in short_url:
        try:
            count_click = count_clicks(token, url)
            return count_click
        except requests.exceptions.HTTPError:
            print('Не действительная ссылка!!!')
    else:
        try:
            short_link = shorten_link(token, url)
            return short_link
        except requests.exceptions.HTTPError:
            print('Не действительная ссылка!!!')
            pass


def main():
    end_data = is_shorten_link(url, short_url)
    print(end_data)

if __name__ == "__main__":
    main()