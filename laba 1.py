import csv
# Используя приложенный файл books.csv, подсчитать количество записей в нём.
# Выдать количество записей, у которых в поле Название строка длиннее 30 символов.
with open('books.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    vsego = 0
    nazv_dl_30 = 0
    for row in file_reader:
        if len(row[1]) > 30:
            nazv_dl_30 += 1
        vsego += 1
    print(f'Всего в файле {vsego-1} строк.')
    print(f'В файле {nazv_dl_30} книг с названием длиннее 30 символов.')

# Реализовать поиск книги по автору, использовать ограничение на выдачу в зависимости от варианта
# Вариант 1
flag = 0
data = input("Search for: ")
with open('books.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    for row in file_reader:
        lower_case = row[3].lower()
        index = row[3].find(data)
        coast = row[7]
        coast = coast.replace(',', '.', 1)
        if index != -1 and float(coast) >= 150:
            print(row)
            flag = 1
    if flag == 0:
        print('Nothing found.')
        
# Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей.
import random
with open('books.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    file = list(row for row in file_reader)[1:]
    random.shuffle(file)
    lines_20 = [f'{row[3]}. {row[1]} - {row[6][0:4]}' for row in file][:20]
f = open('1.txt', 'w')
for line in lines_20:
    f.write(line)
    f.write('\n')
f.close()

# Выдать перечень всех тегов без повторений
with open('books.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    tags = [row[12] for row in file_reader]
    list_of_tags = []
    for line in tags:
        for tag in line.split('#'):
            list_of_tags.append(tag)
    print(set(list_of_tags))

# Самые популярные 20 книг.
with open('books.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    file = [row for row in file_reader][1:]
    max_ = 0
    for line in file:
        max_ = max(int(line[8]), max_)
    k = 0
    for line in file:
        if int(line[8]) == max_ and k < 20:
            print(line)
            k += 1


