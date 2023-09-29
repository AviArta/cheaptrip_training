import os
# import re


def search_change_files(directory, first_data, new_data):
    """Функция принимает на вход путь к папке, просматривает все .json файлы в этой папке
    и делает в них замену одной подстроки на другую, перезаписывая файл.
    Искомая и заменяющая подстроки передаются в параметрах данной функции."""

    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith('.json'):
            print(f'Путь: {entry.path}. Имя файла: {entry.name}')  # нашли каждый файл .json

            # читаем каждый файл, если найдены нужные подстроки, изменяем их:
            with open(entry.name, 'r', encoding='utf-8') as json_file:
                lines = json_file.readlines()
                copy_lines, index_list = [], []
                counter = -1

                # поиск строк с нужными подстроками:
                for line in lines:
                    line = line.strip()  # строка без \n
                    counter += 1

                    if first_data in line:
                        print(f'Подстрока "{first_data}" найдена в строке {line}.')
                        index_list.append(counter)   # список индексов строк, где есть нужная подстрока
                    copy_lines.append(line)  # список всех строк без \n

                # изменение строк:
                for ind in index_list:
                    new_str = copy_lines[ind].replace(first_data, new_data)  # изменённая строка без лишних символов
                    copy_lines[ind] = new_str
                print(f'Изменения в файле {entry.name} сделаны в {len(index_list)} стр.')
                # print('Результирующий список строк:', copy_lines)

            # построчно перезаписываем файл с изменениями:
            with open(entry.name, 'w', encoding='utf-8') as json_file:
                json_file.writelines('%s\n' % line for line in copy_lines)  # каждый элемент списка с новой строки


if __name__ == '__main__':
    path = 'jsons/'
    search_change_files(path, 'four', 'five')


# ------- намётки с regex
# pattern = fr'second'
# pattern = re.compile(r'%s'%first_data)
# re.sub(pattern, new_data, line)
# if re.findall(pattern, line):
#     print('УРА!:', line, 'Индекс =', counter)
# -------