import os
import json


def search_change_files(directory, first_data, new_data):
    """Функция принимает на вход путь к папке, просматривает все .json файлы в этой папке
    и делает в них замену одной подстроки на другую, перезаписывая файл.
    Искомая и заменяющая подстроки передаются в параметрах данной функции.
    Применяется модуль json."""

    try: # лучше поместить вовнутрь цикла for
        for entry in os.scandir(directory): # pathlib так и не захотел устанавливаться?
            if entry.is_file() and entry.name.endswith('.json'): # лучше идти от обратного, т.е. проверять НЕвыполнение условия и, в случае True, переходить к следующему entry припомощи continue
                                                                 # это уменьшит количество отступов и улучшит читаемость кода
                print(f'Путь: {entry.path}. Имя файла: {entry.name}')  # нашли каждый файл .json

                # читаем каждый файл:
                lines = json.load(open(entry.path)) # здесь и далее используй контексный менеджер with open() для открытия файла
                
                #print('lines:', lines)            
                copy_lines, index_list = {}, []    # не потребуется (см. ниже)
                counter = -1                       # не потребуется
                
                # поиск строк с нужными подстроками:
                for line in lines: # т.к. lines - это словарь, то ВЕСЬ этот цикл for несложно заменить ОДНОЙ строчкой - используй "dictionary comprehension"
                    counter += 1
                    if first_data in str(lines[line]):
                        print(f'Подстрока "{first_data}" найдена в строке {line}.')
                        index_list.append(counter)   # список индексов строк, где есть нужная подстрока
                        copy_lines[line] = lines[line]
                        
                        # изменение строк:
                        new_str = copy_lines[line].replace(first_data, new_data)  # изменённая строка без лишних символов
                        copy_lines[line] = new_str

                    else:
                        copy_lines[line] = lines[line]

                print(f'Изменения в файле {entry.name} сделаны в {len(index_list)} стр.')
                #print('copy:', copy_lines)
                
                # записываем изменённые данные:
                json.dump(copy_lines, open(entry.path, 'w'), indent=4) 

    except FileNotFoundError:
        print('По указанному пути файл не найден.')
    except json.JSONDecodeError:
        print(f'Файл {entry.name} пустой.')
    except:
        print(f'Ошибка при работе с файлом {entry.name}.')


if __name__ == '__main__':
    search_change_files('C:/Users/kuvsh/Desktop/Стажировка/Dir_1', 'second', 'NEW')
