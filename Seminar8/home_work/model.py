import shutil
import json
import csv

def add_workers():
    with open('workers.csv', 'a', encoding='utf-8') as file:
        family = input('Введите фамилию: ')
        name = input('Введите имя: ')
        tel = input('Введите номер телефона: ')
        solar = input('Введите оклад: ')
        data = family+ ',' + name + ',' + tel + ',' + solar
        file.write('\n' + data)

def search_workers():
    count = 0
    family = input('\nВведите фамилию или имя сотрудника: ')
    with open('workers.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if family in line:
                print("---"*31)
                print('Фамилия  \t\t Имя        \t\t Номер Телефона   \t\t Оклад')
                print("---"*31)
                print('\t\t\t'.join(line.split(',')))
                count = count + 1
    if count == 0:
        print('Сотрудника с данной фамилией нет !')

def del_workers():
    count = 0
    family = input('\nВведите фамилию или имя сотрудника для удаления: ')
    with open('workers.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if family in line:
                count = count + 1
                continue
            else:
                with open('temp.csv', 'a', encoding='utf-8') as file:
                    file.write(line)
    shutil.copyfile('temp.csv','workers.csv')
    with open('temp.csv', 'w', encoding='utf-8') as i:
        if count !=0:
            print('Сотрудник удален!')
    if count == 0:
        print('Сотрудника с данной фамилией нет !')



def csv_to_json():
    csvFilePath = r'workers.csv'
    jsonFilePath = r'workers.json'
    f = open('workers.csv','r+')
    lines = f.readlines() # read old content
    f.seek(0) # go back to the beginning of the file
    f.write('family,name,numbers,solar\n') # write new content at the beginning фамилия,имя,телефон,оклад\n
    for line in lines: # write old content after new
        f.write(line)
    f.close()
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
        print('Файл создан, имя: workers.json')
          
