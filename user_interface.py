import crud as cr
import generator as gen


print('\nстарт программы "телефонная книга"')


def ls_menu():
    while True:
        print('\nМЕНЮ, выбереите пункт работы, увОжаемый кожанный ублюдок')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Найти номер по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись.')
        print('6. Изменить существующую запись.')
        print('7. Удалить запись.')
        print('8. Cгенерировать левые днанные (тест работы)')
        print('9. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            print(cr.retrive())

        elif n == 2:
            search = input('Введите фамилию: ')
            print(cr.retrive(surname=search))

        elif n == 3:
            search = input('Введите имя: ')
            print(cr.retrive(name=search))

        elif n == 4:
            search = input('Введите номер  телефона: ')
            print(cr.retrive(number=search))

        elif n == 5:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            email = input('Введите электронную почту: ')
            cr.create(name, surname, number, email)

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                search = input('Введите фамилию: ')
                cr.retrive(surname=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            elif change == 2:
                search = input('Введите имя: ')
                cr.retrive(name=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            elif change == 3:
                search = input('Введите номер телефона: ')
                cr.retrive(number=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            else:
                print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню, или позовите взрослого.')

        elif n == 7:
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                search = input('Введите фамилию: ')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                cr.delete(id=user_id)

            elif deleting == 2:
                search = input('Введите имя: ')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                cr.delete(id=user_id)

            elif deleting == 3:
                search = input('Введите номер телефона: ')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nНеверное значение.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
           gen.start
           print(cr.retrive())

        elif n == 9:
            print('Программа закрыта')
            break

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число. Позовите к компьютеру взрослого!')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
