import os

print('© Valberton 2018-2024\n')

def main(folderPath):

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
            filelines[1] = webpFiles[idx] + '\n'
            file2w.writelines(filelines)

while True:
    folderPath = input('Введите имя рабочей папки (по умолчанию - папка выполнения скрипта): ')
    
    if len(' '.join(folderPath.split())) == 0:
        folderPath = os.getcwd()

    main(folderPath)

    isExit = input('Выйти из программы? [Y/N] ')
    if isExit.lower() == 'y' or isExit.lower() == 'д':
        exit()
    else:
        print()