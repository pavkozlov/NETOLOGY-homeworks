from urllib.parse import urlencode
from time import sleep

import requests

TOKEN = '5a10fbd7f02c92b723338e72a3d4a8252ce4a7e3a511e3e61f3631e19c402dd1b1e9d3af606d1888185d7'


def get_access_token_link():
    APP_ID = 6854739
    AUTH_URL = 'https://oauth.vk.com/authorize'
    AUTH_DATA = {
        'client_id': APP_ID,
        'display': 'page',
        'scope': 'status, friends',
        'response_type': 'token',
        'v': '5.92',
        'redirect_uri': ''
    }
    url = '?'.join((AUTH_URL, urlencode(AUTH_DATA)))
    print(url)


class User:

    def __init__(self, id):
        self.id = id
        params = get_params()
        params['user_ids'] = self.id
        params['name_case'] = 'gen'
        self.name = requests.get('https://api.vk.com/method/users.get', params).json()['response'][0]['first_name']
        sleep(1)

    def __and__(self, other):
        params = get_params()
        params['target_uid'] = other.id
        params['source_uid'] = self.id
        params['name_case'] = 'gen'
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        result_list = response.json()['response']
        user_list = []
        for item in result_list:
            user_list.append(User(item))
        print(f'У {self.name} и {other.name} следующие общие друзья: ')
        return user_list

    def __str__(self):
        return f'http://vk.com/id{self.id}'


def get_params():
    params = {'v': '5.92', 'access_token': TOKEN}
    return params


def get_name(user):
    params = get_params()
    params['user_ids'] = user.id
    name = requests.get('https://api.vk.com/method/users.get', params).json()['response'][0]['first_name']
    secondname = requests.get('https://api.vk.com/method/users.get', params).json()['response'][0]['last_name']
    print(f'http://vk.com/id{user.id} {name} {secondname}')
    sleep(1)


if __name__ == '__main__':

    user1 = User(19541420)
    user2 = User(136707281)

    print(user1)
    print(user2)

    for user in (user1 & user2):
        get_name(user)
