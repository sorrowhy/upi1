# Лабораторная работа №1
## ББМО-02-22 Исаев Александр Михайлович

Данное приложение состоит из двух основных функций:
1. Запись с определенной позиции в первый массив, всех значения второго (без использования стандартной библиотеки);
2. Вывод в табличном представлении списка предметов и количество, сдавших этот предмет студентов.

Приложение запускается через файл main.py.

Функция 1 просит пользователя ввести данные двух массивов через пробел и индекс элемента, с которого начинается запись второго массива к первому.
После ввода необходимой информации функция выводит результат в консоль.

Пример работы функции 1:
```
Введите элементы первого массива через пробел: 1 2 3 4 5
Введите элементы второго массива через пробел: 10 11 12 13 14 15
Введите индекс: 3
Результат: ['1', '2', '3', '10', '11', '12', '13', '14', '15']
```

Функция 2 считывает данные из файла input_file.txt, пример его исполнения приводится ниже.
После обработки информации из файла функция выводит результат в консоль.

Пример работы функции 2:
```
   Subject  nStudents
0     Math          3
1  Physics          3
2  History          3
```

Пример файла input_file.txt:
```
1,Ivanov Ivan Ivanovich,2000-01-01,Math:3|2020-01-01|Pupkin Pup Pupkovich;Physics:4|2020-02-01|Baluev Balu Baluevich;History:5|2020-03-01|Gorin Gor Gorevich
2,Sidorov Sidor Sidorovich,2001-01-01,Math:5|2021-01-01|Pupkin Pup Pupkovich;Physics:4|2021-02-01|Baluev Balu Baluevich;History:3|2021-03-01|Gorin Gor Gorevich
3,Petrov Petr Petrovich,2002-01-01,Math:5|2022-01-01|Pupkin Pup Pupkovich;Physics:5|2022-02-01|Baluev Balu Baluevich;History:3|2022-03-01|Gorin Gor Gorevich
```