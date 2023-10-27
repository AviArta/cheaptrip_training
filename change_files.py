import pathlib
import json
import argparse

from my_logging import logger


parser = argparse.ArgumentParser(description='The function executes the search of files ' 
    '.json on the specified path inside the all tree, modifies substrings of an element '
    'by key in the found files.It accepts parameters of path, first_data, new_data, key '
    'and overwrites files.To run code from the command line you need to enter the required '
    'parameters')
parser.add_argument('directory', type=str, help='path to the directory for search json files')
parser.add_argument('first_data', type=str, help='the substring to be modified in the string')
parser.add_argument('new_data', type=str, help='the new substring toreplace in the string')
parser.add_argument('key', default='images', type=str, help='the key whose value needs to be modified')
args = parser.parse_args()

def search_change_files(directory: str, first_data: str, new_data: str, key: str):  # key: str = 'images'
    ''' The function executes the search of files ".json" on the specified path 
    inside the all tree, modifies substrings of an element by key in the found files.
    It accepts parameters of path, first_data, new_data, key and overwrites files.
       To run code from the command line you need to enter the required parameters:
    '''
    file_list = list(pathlib.Path(directory).rglob('*.json'))
    counter_change_files = 0

    for entry in file_list:
        try:
            # reading each file:
            with open(entry, encoding='UTF-8') as input_file:
                lines = json.load(input_file)

            # creating the dictionary with modified substrings by key:
            if isinstance(lines[key], list):
                lines[key] = [element if type(element) != str else element.replace(first_data, new_data) for element in lines[key]]
                counter_change_files += 1            
            elif isinstance(lines[key], str):
                lines[key] = lines[key].replace(first_data, new_data)
                counter_change_files += 1
            
            # recording modified data:
            with open(entry, 'w', encoding='UTF-8') as input_file:
                json.dump(lines, input_file, indent=4)
                #logger.warning(f'File {entry.name} changed.')

        except FileNotFoundError:
            logger.error('Files ".json" are not found on the specified path.')
            continue
        except json.JSONDecodeError:
            #logger.warning(f'File {entry.name} is empty.')
            continue
        except KeyError:
            #logger.warning(f'There is no key "{key}" in the file {entry.name}.')
            continue
        except TypeError:
            logger.critical('Check the data type in the arguments of the function.')
        except:
            logger.error(f'Error working the file {entry.name}.')
            continue

    print(f'Количество обработанных файлов: {len(file_list)}')
    print(f'Успешно изменено файлов: {counter_change_files}, без изменений: {len(file_list) - counter_change_files}')
    print(f'Выполнение программы завершено.')