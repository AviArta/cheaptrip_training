import os
import pathlib


def search_change_files(directory, first_data, new_data):
    """Функция принимает на вход путь к папке, просматривает все .json файлы в этой папке
    и делает в них замену одной подстроки на другую, перезаписывая файл.
    Искомая и заменяющая подстроки передаются в параметрах данной функции.
    Применяется модуль json."""
    
    for entry in os.scandir(directory):
        try:
            if not (entry.is_file() and entry.name.endswith('.json')):
                continue
                
            print(f'Путь: {entry.path}. Имя файла: {entry.name}')  # нашли каждый файл .json

            # читаем каждый файл:
            with open(entry.path) as input_file:
                lines = json.load(input_file)
            
            # формируем словарь с измененёнными нужными подстроками для перезаписи файла:
            result_dict = {key:str(value).replace(first_data, new_data)  for (key, value) in lines.items()}
            #print('result_dict:', result_dict)
            
            # записываем изменённые данные:
            with open(entry.path, 'w') as input_file:
                json.dump(result_dict, input_file, indent=4)
            print(f'Изменения в файле {entry.name} сделаны.')

        except FileNotFoundError:
            print('По указанному пути файл не найден.')
        except json.JSONDecodeError:
            print(f'Файл {entry.name} пустой.')
        except:
            print(f'Ошибка при работе с файлом {entry.name}.')


if __name__ == '__main__':
    #search_change_files('C:/Users/kuvsh/Desktop/Стажировка/Dir_1', 'second', 'NEW')
    p = pathlib.Path(__file__)
    print("Path:", p, 'Имя файла', p.name)
    print('Parent 1:', p.parent, 'Суффикс файла:', p.suffix)
    o = pathlib.PurePath('main_json.py')  # проверка, является ли указанный путь абсолютным
    print('Путь абсолютный?', o.is_absolute())
    print('Слепленный путь:', p.joinpath('+file'))  # конкатенация строк

    # содержание каталога:
    p = pathlib.Path('C:/Users/kuvsh/Desktop/Стажировка/Dir_1')
    for child in p.iterdir():
        print(child)
    # возвращает содержимое файла в формате строки:
    p = pathlib.Path('C:/Users/kuvsh/Desktop/Стажировка/Dir_1/test4.json')
    print('Строка:', p.read_text())
    #
    