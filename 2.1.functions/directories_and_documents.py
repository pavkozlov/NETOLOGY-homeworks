documents_list = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories_list = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def my_func(documents, directories, command):
    if command == 'p':
        doc_number = input("Введите номер документа: ")
        for document in documents:
            if document['number'] == doc_number:
                print(document['name'])
    if command == 'l':
        for document in documents:
            print(document['type'], document['number'], document['name'])
    if command == 's':
        doc_number = input("Введите номер документа: ")
        for directory_num in directories:
            if doc_number in directories[directory_num]:
                print('Документ находится на {} полке'.format(directory_num))
    if command == 'a':
        number = input('Введите номер документа: ')
        type = input('Введите тип документа: ')
        name = input('Введите имя владельца: ')
        directory_num = input('Введите номер полки: ')
        documents.append({"type": type, "number": number, "name": name})
        if directory_num in directories:
            directories[directory_num].append(number)
        else:
            directories[directory_num] = number
    if command == 'd':
        number = input('Введите номер документа: ')
        for document in documents:
            if document["number"] == number:
                documents.pop(documents.index(document))
        for directory_num in directories:
            if number in directories[directory_num]:
                directories[directory_num].pop(directories[directory_num].index(number))
    if command == 'm':
        number = input('Введите номер документа: ')
        directory = input('Введите номер полки: ')
        for directory_num in directories:
            if number in directories[directory_num]:
                directories[directory_num].pop(directories[directory_num].index(number))
        directories[directory].append(number)
    if command == 'as':
        directory = input('Введите номер полки: ')
        if directory not in directories:
            directories[directory] = []
