import requests
import os
from dotenv import load_dotenv


VK_API_URL = 'https://api.vk.ru/method/'


def short_link(token, url):
    try:
        parm = {
            'url': url,
            "access_token": token,
            "v": '5.199 HTTP/1.1'
        }
        response = requests.get(f'{VK_API_URL}utils.getShortLink', params=parm)
        urloutput = response.json()['response']
        return urloutput['short_url']
    except:
        return KeyError


def count_clicks(token, url):
    try:
        parm = {
            "access_token": token,
            'key': url.replace('https://vk.cc/', ''),
            "interval": 'forever',
            "v": '5.199 HTTP/1.1'
        }
        response = requests.get(f'{VK_API_URL}utils.getLinkStats', params=parm)
        urloutput = response.json()["response"]
        stats = urloutput['stats']
        if stats == []:
            return 0
        else:    
            views = stats[-1]
            return views['views']
    except requests.exceptions.HTTPError:
        print('Не действительная ссылка!!!')
        pass


def is_shorten_link(token, url):
    if short_link(token, url) == KeyError:
        return True
    else:
        return False


def main():
    load_dotenv()
    url = input('Введите ссылку:')
    token = os.environ['VK_TOKEN']
    if is_shorten_link(token, url) == True:
        return print(count_clicks(token, url))
    else:
        return print(short_link(token, url))
            

if __name__ == "__main__":
    main()