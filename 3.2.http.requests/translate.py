import requests


def write_to_file(translated_text, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(translated_text)


def get_from_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read().strip()


def translate_it(in_file, from_lang, to_lang, out_file):
    api_key = 'trnsl.1.1.20190206T080012Z.b34ef074ffc40e08.927eb24361bd5d9829979293bd1542c96457470a'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    text = get_from_file(in_file)

    params = {
        'key': api_key,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(url, params=params)
    json_ = response.json()
    result = ''.join(json_['text'])
    write_to_file(result, out_file)
    return result


if __name__ == '__main__':
    translate_it('ES.txt', 'es', 'ru', 'translated.txt')
