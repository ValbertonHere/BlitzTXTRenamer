import os

print('© Valberton 2018-2024\n')

def main(folderPath, strToRename):

    for file in os.listdir(folderPath):
        if file.endswith('.txt'):
            print(f'Обработка файла: {file}')

            with open(f'{folderPath}/{file}', 'r') as file2r:
                filelines = file2r.readlines()
            
            with open(f'{folderPath}/{file}', 'w') as file2w:
                filelines[1] = strToRename + '\n'
                file2w.writelines(filelines)

while True:
    folderPath = input('Введите имя рабочей папки (по умолчанию - папка выполнения скрипта): ')
    strToRename = input('Введите строку для замены: ')
    
    if len(' '.join(folderPath.split())) == 0:
        folderPath = os.getcwd()

    if len(' '.join(strToRename.split())) == 0:
        print('\nНедопустимая строка для замены, повторение запроса...\n')
        continue
    
    main(folderPath, strToRename)

    isExit = input('Выйти из программы? [Y/N] ')
    if isExit.lower() == 'y' or isExit.lower() == 'д':
        exit()
    else:
        print()