task = 'Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
first = int(input('Введите число в переменную "first": '))
second = int(input('Введите число в переменную "second": '))
third = int(input('Введите число в переменную "third": '))
if first != second and first != third and second != third:
    print('Число совпадений = 0')
elif first != second or second != third or third !=first:
    print('Число совпадений = 2')
    if first == second:
        print(f'first: {first} = second: {second}')
    elif second == third:
        print(f'second: {second} = third: {third}')
    elif first == third:
        print(f'first: {first} = third: {third}')
else:
    print('Число совпадений = 3')
    print(f'first: {first} = second: {second} = third:{third}')
print()
print(thanks)

