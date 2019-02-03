import xml.etree.ElementTree as ET
from pprint import pprint


def get_descriptions(filename):
    words_list = list()
    three = ET.parse(filename)
    root = three.getroot()
    descriptions = root.findall("channel/item/description")
    for descriptions in descriptions:
        for words in descriptions.text.strip().split():
            if len(words) > 6:
                words_list.append(words)
    return words_list


def get_top(words_list, top):
    count_dict = dict()
    for words in words_list:
        count_dict[words] = words_list.count(words)
    count_dict = sorted(count_dict, key=count_dict.get, reverse=True)
    return count_dict[:top]


pprint(get_top(get_descriptions('newsafr.xml'), 10))
