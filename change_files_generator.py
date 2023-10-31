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

def change_list(part_list, first_data, new_data, key):
    for entry in part_list:
        try:
            # reading each file:
            with open(entry, encoding='UTF-8') as input_file:
                lines = json.load(input_file)

            # creating the dictionary with modified substrings by key:
            if isinstance(lines[key], list):
                lines[key] = [element if type(element) != str else element.replace(first_data, new_data) for element in lines[key]]            
            elif isinstance(lines[key], str):
                lines[key] = lines[key].replace(first_data, new_data)

            # recording modified data:
            with open(entry, 'w', encoding='UTF-8') as input_file:
                json.dump(lines, input_file, indent=4)
                logger.warning(f'File {entry.name} changed.')
        

        except FileNotFoundError:
            logger.error('Files ".json" are not found on the specified path.')
            continue
        except (json.JSONDecodeError, KeyError):
            continue
        except:
            logger.error(f'Error working the file {entry.name}.')
            continue

def my_generator(directory, first_data, new_data, key):
    file_list = list(pathlib.Path(directory).rglob('*.json'))
    counter = 0
    cursor = 0

    while cursor <= (len(file_list) - 1 - cursor):
        res_list = []
        for element in file_list[cursor:(cursor + 3)]:
            res_list.append(element)
            counter += 1
        yield change_list(res_list, first_data, new_data, key)
        cursor += 3
    if cursor >= ((len(file_list) - 1) - cursor):
        counter += 1
        yield change_list(file_list[cursor:len(file_list)], first_data, new_data, key)
    
    print(f'Всего файлов json: {len(file_list)}', f'Количество изьенённых файлов: {counter}.', f'Выполнение программы завершено.', sep='\n')


if __name__ == '__main__':
    for element in my_generator(args.directory, args.first_data, args.new_data, args.key):
        element