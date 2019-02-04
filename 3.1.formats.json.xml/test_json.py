import json
from pprint import pprint


def get_descriptions(filename):
    words_list = list()
    with open(filename, encoding='UTF-8') as file:
        result = json.load(file)

    for descriptions in result['rss']['channel']['items']:
        for words in descriptions['description'].strip().split():
            if len(words) > 6:
                words_list.append(words)
    return words_list


def get_top(words_list, top):
    count_dict = dict()
    for words in words_list:
        count_dict[words.lower()] = words_list.count(words)
    count_dict = sorted(count_dict, key=count_dict.get, reverse=True)
    return count_dict[:top]


if __name__ == 'main':
    pprint(get_top(get_descriptions('newsafr.json'), 10))
