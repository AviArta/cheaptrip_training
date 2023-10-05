import pathlib
import json

def search_change_files(directory, first_data, new_data):

    file_list = sorted(pathlib.Path(directory).glob('*.json'))
    for entry in file_list:
        print(f'Имя файла: {entry.name}')

        try:
            # читаем каждый файл:
            with open(entry, encoding='UTF-8') as input_file:
                lines = json.load(input_file)
            
            # формируем словарь с измененёнными нужными подстроками для перезаписи файла:
            result_dict = {key:str(value).replace(first_data, new_data)  for (key, value) in lines.items()}
            #print('result_dict:', result_dict)
            
            # записываем изменённые данные:
            with open(entry, 'w', encoding='UTF-8') as input_file:
                json.dump(result_dict, input_file, indent=4)
            print(f'Изменения в файле {entry.name} сделаны.')

        except FileNotFoundError:
            print('По указанному пути файл не найден.')
        except json.JSONDecodeError:
            print(f'Файл {entry.name} пустой.')
        except:
            print(f'Ошибка при работе с файлом {entry.name}.')


if __name__ == '__main__':
    search_change_files('C:/Users/kuvsh/Desktop/Стажировка/Dir_1', 'second', 'NEW')