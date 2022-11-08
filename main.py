documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people():
    inp = input('Введите номер ')
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if inp in num_list:
        name = next(x for x in documents if x["number"] == inp)
        print(name["name"])
    else:
        print("Такого номера документа нет")


def shelf():
    inp = input('Введите номер ')
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if inp in num_list:
        direct_list = directories.items()
        for x in direct_list:
            if inp in x[1]:
                print(f'Документ находится на {x[0]} полке')
    else:
        print("Такого номера документа нет")


def list():
    for string in documents:
        print(string['type'], string['number'], string['name'])


def add():
    new_dict = {}
    type_inp = input('Введите тип документа: ')
    number_inp = input('Введите номер документа: ')
    name_inp = input('Введите фамилию и имя: ')
    dict_inp = input('В какую полку положить документ ?')
    if dict_inp in directories.keys():
        new_dict['type'] = type_inp
        new_dict['number'] = number_inp
        new_dict['name'] = name_inp
        documents.append(new_dict)
        directories[dict_inp].append(number_inp)
    else:
        print('Такой полки нет!')


def delete():
    inp = input('Введите номер документа который вы хотите удалить: ')
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if inp in num_list:
        for i in range(len(documents)):
            if documents[i]['number'] == inp:
                del documents[i]
                print(f'Документ {inp} удален из списка!')
                for element in directories.values():
                    if inp in element:
                        element.remove(inp)
                    print(element)
                print(f'Документ {inp} удален c полки!')
                print(directories.items())
                break
    else:
        print("Такого номера документа нет")


def move():
    num_imp = input('Введите номер документа, который хотите переместить: ')
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if num_imp in num_list:
        for element in directories.values():
            print(element)
            if num_imp in element:
                element.remove(num_imp)
    else:
        print("Такого номера документа нет")
    move_inp = input('Введите номер полки, в которую хотите переместить документ: ')
    if move_inp in directories.keys():
        directories[move_inp].append(num_imp)
        print(directories.items())
    else:
        print('Такой полки нет!')


def add_shelf():
    new_key = input('Введите номер новой полки: ')
    if new_key in directories.keys():
        print('Такая полка уже есть!')
    else:
        print('Такая полки нет!')
        directories[new_key] = []
        print(f'Полка номер {new_key} создана!')


def main():
    while True:
        user_input = input("Введите команду: ")
        if user_input == 'p':
            people()
        elif user_input == 's':
            shelf()
        elif user_input == 'l':
            list()
        elif user_input == 'a':
            add()
        elif user_input == 'd':
            delete()
        elif user_input == 'm':
            move()
        elif user_input == 'as':
            add_shelf()
        elif user_input == 'q':
            break


main()