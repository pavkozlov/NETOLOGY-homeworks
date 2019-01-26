documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    "1": ["2207 876234", "11-2"],
    "2": ["10006"],
    "3": []
}


def get_people(documents, doc_number):
    counter = 0
    for document in documents:
        if document["number"] == doc_number:
            print(document["name"])
        else:
            counter += 1
        if counter == len(documents):
            print("Нет такого документа.")


def documents_list(documents):
    for document in documents:
        print(document["type"], document["number"], document["name"])


def shelf_nubmer(directories, doc_number):
    counter = 0
    for directory_num in directories:
        if doc_number in directories[directory_num]:
            print("Документ находится на {} полке".format(directory_num))
        else:
            counter += 1
        if counter == len(directories):
            print("Документ не найден")


def add_document(documents, directories, doc_number, type, name, directory_num):
    documents.append({"type": type, "number": doc_number, "name": name})
    if directory_num in directories:
        directories[directory_num].append(doc_number)
    else:
        directories[directory_num] = [doc_number]


def delete(documents, directories, doc_number):
    counter = 0
    for document in documents:
        if document["number"] == doc_number:
            documents.pop(documents.index(document))
        else:
            counter += 1
    if counter == len(documents):
        print("Такого документа в списке нет!")
    else:
        for directory_num in directories:
            if doc_number in directories[directory_num]:
                directories[directory_num].pop(directories[directory_num].index(doc_number))


def move(directories, doc_number, directory):
    counter = 0
    for directory_num in directories:
        if doc_number in directories[directory_num]:
            directories[directory_num].pop(directories[directory_num].index(doc_number))
        else:
            counter += 1
    if counter == len(directories):
        print("Такого элемента нет!")
    else:
        if directories.get(directory):
            directories[directory].append(doc_number)
        else:
            directories[directory] = [doc_number]


def add_shelf(directories, directory):
    if directory not in directories:
        directories[directory] = []


print("Для выхода из программы введите q\n")

while True:
    user_command = input("Введите команду: ")
    if user_command == "p":
        print()
        doc_number = input("Введите номер документа: ")
        get_people(documents, doc_number)
        print()
    elif user_command == "l":
        print()
        documents_list(documents)
        print()
    elif user_command == "s":
        print()
        doc_number = input("Введите номер документа: ")
        shelf_nubmer(directories, doc_number)
        print()
    elif user_command == "a":
        print()
        doc_number = input("Введите номер документа: ")
        type = input("Введите тип документа: ")
        name = input("Введите имя владельца: ")
        directory_num = input("Введите номер полки: ")
        add_document(documents, directories, doc_number, type, name, directory_num)
        print()
    elif user_command == "d":
        print()
        doc_number = input("Введите номер документа: ")
        delete(documents, directories, doc_number)
        print()
    elif user_command == "m":
        print()
        doc_number = input("Введите номер документа: ")
        directory = input("Введите номер полки: ")
        move(directories, doc_number, directory)
        print()
    elif user_command == "as":
        print()
        directory = input("Введите номер полки: ")
        add_shelf(directories, directory)
        print()
    elif user_command == "q":
        print("Завершение работы.")
        break
    else:
        print("Такой команды не найдено, попробуйте ещё раз")


def get_all_names(documents):
    try:
        for document in documents:
            print(document["name"])
    except KeyError:
        print("В документе не указано имя")

