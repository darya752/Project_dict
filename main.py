# Программа представляет собой управляемую телефонную книгу. Пользователю предлагается выбрать одну из
# 5 опций: найти номер в книге, добавить номер, изменить номер, удалить номер, выйти из программы.
# После того, как пользователь введет телефонные номера и выйдет из программы, все данные (имя и номер телефона),
# будут занесены в отдельный файл-телефонную книгу input.txt.

Look_up = 1
Add = 2
Change = 3
Delete = 4
Exit = 5

with open('input.txt', 'w') as f_in:
    def main():
        numbers = {}
        choice = 0
        while choice != Exit:
            choice = menu_choice()
            if choice == Look_up:
                look_up(numbers)
            elif choice == Add:
                add(numbers)
            elif choice == Change:
                change(numbers)
            elif choice == Delete:
                delete(numbers)
        if choice == Exit:
            for key in numbers:
                print(key, numbers[key], file=f_in)

    def menu_choice():
        try:
            print('-------------------------')
            print('PHONE BOOK')
            print('-------------------------')
            print('1. find a phone number')
            print('2. add a new number')
            print('3. change a number')
            print('4. delete a number')
            print('5. exit the program')
            print('-------------------------')
            choice = int(input('Enter the selected item: '))
            while choice < Look_up or choice > Exit:
                choice = int(input('Enter the selected item (from the five possible options): '))
            return choice
        except ValueError:
            print('Enter an integer')

    def look_up(numbers):
        name = input('Enter a name: ')
        print(numbers.get(name, 'Name not found'))

    def add(numbers):
        name = input('Enter a name: ')
        num = input('Enter a phone number: ')
        if num not in numbers:
            numbers[name] = num
        else:
            print('This number is already in the phone book')

    def change(numbers):
        name = input('Enter a name: ')
        if name in numbers:
            num = input('Enter a new phone number: ')
            numbers[name] = num
        else:
            print('This name was not found')

    def delete(numbers):
        name = input('Enter a name: ')
        if name in numbers:
            del numbers[name]
        else:
            print('This name was not found')

    main()




