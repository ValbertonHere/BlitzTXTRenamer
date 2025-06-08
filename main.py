import os

print('© Valberton 2018-2024\n')

def main(folderPath, strToRename=None):

    txtFiles = []
    webpFiles = []

    for file in os.listdir(folderPath):
        if file.endswith('.txt'):
            txtFiles.append(file)
        
        if file.endswith('.webp'):
            webpFiles.append(file)

    for idx, file in enumerate(txtFiles):
        print(f'Обработка файла: {file}')

        with open(f'{folderPath}/{file}', 'r') as file2r:
            filelines = file2r.readlines()
        
        with open(f'{folderPath}/{file}', 'w') as file2w:
            if strToRename is not None:
                filelines[1] = strToRename + '\n'
            else:
                filelines[1] = webpFiles[idx] + '\n'
            file2w.writelines(filelines)

while True:
    folderPath = input('Введите имя рабочей папки (по умолчанию - папка выполнения скрипта): ')
    strToRename = input('Введите строку для замены (для присваивания множеству txt одного webp-файла): ')
    
    if len(' '.join(folderPath.split())) == 0:
        folderPath = os.getcwd()

    if len(' '.join(strToRename.split())) == 0:
        strToRename = None

    main(folderPath, strToRename)

    isExit = input('Выйти из программы? [Y/N] ')
    if isExit.lower() == 'y' or isExit.lower() == 'д':
        exit()
    else:
        print()