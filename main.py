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

def help():
    return """
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    ld– list-directories – команда, которая выведет список всех полок;
    a – add – команда, которая добавит новый документ в каталог и в перечень полок;

    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
    """
def people(inp):
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if inp in num_list:
        name = next(x for x in documents if x["number"] == inp)
        return name["name"]
    else:
        return "Такого номера документа нет"


def shelf(inp):
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if inp in num_list:
        direct_list = directories.items()
        for x in direct_list:
            if inp in x[1]:
                return f'Документ находится на {x[0]} полке'
    else:
        return "Такого номера документа нет"


def list():
    return [[string['type'], string['number'], string['name']] for string in documents]


def list_directories():
    return [(key, value) for key, value in directories.items()]

def add(type_inp, number_inp, name_inp, dict_inp):
    new_dict = {}
    if dict_inp in directories.keys():
        new_dict['type'] = type_inp
        new_dict['number'] = number_inp
        new_dict['name'] = name_inp
        documents.append(new_dict)
        directories[dict_inp].append(number_inp)
        return 'Добавлен в словарь и на полку'
    else:
        return 'Такой полки нет!'


def delete(inp):
    num_list = []
    for num in documents:
        num_list.append(num["number"])
    if inp in num_list:
        for i in range(len(documents)):
            if documents[i]['number'] == inp:
                del documents[i]
                return f'Документ {inp} удален из списка!'
    else:
        return "Такого номера документа нет"

def del_in_shelf(inp):
    for element in directories.values():
        if inp in element:
            element.remove(inp)
            return f'Документ {inp} удален c полки!'


def move(inp, move_inp):
    if not check_document(inp):
        return "Такого номера документа нет"
    if not check_shelf(move_inp):
        return 'Такой полки нет!'
    if check_document(inp) == True and check_shelf(move_inp) == True:
        del_in_shelf(inp)
        if move_inp in directories.keys():
            directories[move_inp].append(inp)
            return f'Перемещена на {move_inp} полку'


def add_shelf(new_key):
    if new_key in directories.keys():
        return 'Такая полка уже есть!'
    else:
        directories[new_key] = []
        return f'Полка номер {new_key} создана!'

def check_document(number):
    lst = [el["number"] for el in documents]
    if number in lst:
        return True
    else:
        return False

def check_shelf(number):
    if number in directories.keys():
        return True
    else:
        return False

def main():
    print('Для помощи введите help')
    while True:
        user_input = input("Введите команду: ")
        if user_input == 'p':
            inp = input('Введите номер ')
            print(people(inp))
        elif user_input == 's':
            inp = input('Введите номер ')
            print(shelf(inp))
        elif user_input == 'l':
            print(list())
        elif user_input == 'ld':
            print(list_directories())
        elif user_input == 'a':
            type_inp = input('Введите тип документа: ')
            number_inp = input('Введите номер документа: ')
            name_inp = input('Введите фамилию и имя: ')
            dict_inp = input('В какую полку положить документ ? ')
            print(add(type_inp, number_inp, name_inp, dict_inp))
        elif user_input == 'd':
            inp = input('Введите номер документа который вы хотите удалить: ')
            print(delete(inp))
            print(del_in_shelf(inp))
        elif user_input == 'm':
            inp = input('Введите номер документа, который хотите переместить: ')
            move_inp = input('Введите номер полки, в которую хотите переместить документ: ')
            print(move(inp, move_inp))
        elif user_input == 'as':
            new_key = input('Введите номер новой полки: ')
            print(add_shelf(new_key))
        elif user_input == 'help':
            print(help())
        elif user_input == 'q':
            break


main()