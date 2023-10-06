import pathlib
import json


def change_files_by_key(directory, key, new_value):  # key = "images"
    ''' Функция реализует поиск файлов с расширением .json в указанной папке 
    любой вложенности, выполняет замену значений для ключа "images". Значение должно быть
    в виде списка с одним элементом-строкой. В пареметрах функции передается путь к папке,
    ключ, новое значение.'''
    # Пример: "images": ["ferry"] должен измениться на "images": ["cherry"] 

    file_list = pathlib.Path(directory).glob('**/*.json')
    for entry in file_list:
        print(f'Имя файла: {entry.name}')
        
        try:
            # читаем каждый файл:
            with open(entry, encoding='UTF-8') as input_file:
                lines = json.load(input_file)

             # формируем словарь с измененёнными нужными подстроками для перезаписи файла:
            for line in lines:
                if line != key:
                    continue
                else:
                    lines[key] = [new_value]
                    print(f'Изменения в файле {entry.name} сделаны.')

            #result_dict = {k: v if k != key else v[0].replace(v[0], new_value) for k, v in lines.items()}
            #print('result_dict:', result_dict)
            # вариант работает только "images": "cherry", не ["cherry"]
            
            # записываем изменённые данные:
            with open(entry, 'w', encoding='UTF-8') as input_file:
                json.dump(lines, input_file, indent=4)  # result_dict

        except FileNotFoundError:
            print('По указанному пути файл не найден.')
            continue
        except json.JSONDecodeError:
            print(f'Файл {entry.name} пустой.')
            continue
        except:
            print(f'Ошибка при работе с файлом {entry.name}.')
            continue


def search_change_files(directory, first_data, new_data):
    """Функция принимает на вход путь к папке, просматривает все .json файлы в этой папке
    и делает в них замену одной подстроки на другую, перезаписывая файл.
    Искомая и заменяющая подстроки передаются в параметрах данной функции.
    Применяется модули pathlib и json."""
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
    #search_change_files('C:/Users/kuvsh/Desktop/Стажировка — копия/Dir_1', 'second', 'NEW')
    change_files_by_key('C:/Users/kuvsh/Desktop/Стажировка', 'images', 'cherry')