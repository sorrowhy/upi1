#17.Вывести в виде таблицы 
#все предметы и 
#количество студентов, получивших оценки 
#по этим предметам
import os.path
import pandas as pd

def Print():
    result = dict()
    check_file = os.path.exists('./input_file.txt')
    if (check_file == False):
        print('Не найден файл input_file.txt')
    else:
        with open('./input_file.txt', 'r', encoding="utf-8") as f:
            content = f.read()
            for row in content.split('\n'):
                zachetka = row.split(',')[3]
                for predmet in zachetka.split(';'):
                    predmet_name = predmet.split('|')[0]
                    predmet_name = predmet_name[:predmet_name.index(':')]
                    if (predmet_name not in result.keys()):
                        result[predmet_name] = 1
                    else:
                        result[predmet_name] += 1
    result = pd.DataFrame(result.items(), columns=['Subject', 'nStudents'])
    print(result)