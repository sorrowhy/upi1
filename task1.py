#14.Напишите функцию, которая начинает, 
#записывает с определенной позиции, 
#в первый массив, все значения второго 
#(без использования стандартной библиотеки)

def LetsStart():
    array1 = list(input('Введите элементы первого массива через пробел: ').split(' '))
    array2 = list(input('Введите элементы второго массива через пробел: ').split(' '))
    index = int(input('Введите индекс: '))
    array3 = list()
    for i in range(0, index):
        array3.append(array1[i])
    for i in range(0, len(array2)):
        array3.append(array2[i])
    print('Результат:', array3)