# написать функцию, которой на вход может прийти имя студента (ФИО) в формате строки, кортежа, списка, словаря
# функция должна возвращать текст "Error" при неверных или недостоверных данных или возвращать строку
# типа f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'

def parse_name(value: str | tuple | list | dict) -> str:
    match value:
        case surname, name, second_name:
            # return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
            pass
        case {'surname': surname, 'name': name, 'second_name': second_name} if len(value) == 3:
            # return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
            pass
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            # return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
            pass
        case _:
            return 'Error'
    return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'


if __name__ == '__main__':
    assert parse_name(('Иванов', 'Иван', 'Иванович')) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_name(['Иванов', 'Иван', 'Иванович']) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_name({'surname': 'Иванов',
                       'name': 'Иван',
                       'second_name': 'Иванович'}) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_name('Иванов Иван Иванович') == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_name(['Иванов', 'Иван']) == 'Error'
    assert parse_name(('Иванов', 'Иван', 'Иван', 'Иван')) == 'Error'
    assert parse_name({'a': 'Иванов', 'b': 'Иван', 'c': 'Иванович'}) == 'Error'
    assert parse_name('Иванов Иван Иванович 122') == 'Error'
    assert parse_name({'surname': 'Иванов',
                       'name': 'Иван',
                       'second_name': 'Иванович',
                       'salary': 100_000}) == 'Error'
