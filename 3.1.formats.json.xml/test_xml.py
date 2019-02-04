import xml.etree.ElementTree as ET
from pprint import pprint
from test_json import get_top


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


if __name__ == 'main':
    pprint(get_top(get_descriptions('newsafr.xml'), 10))
