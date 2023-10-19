import pathlib
import json
import logging
import sys
from datetime import datetime, date


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logfile_name = f'{pathlib.Path(__file__).name}_{date.today()}_{str(datetime.now().time().strftime("%X")).replace(":", ".")}'
handler = logging.FileHandler(f'{logfile_name}.log', mode='w')
formatter = logging.Formatter('%(funcName)s %(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def search_change_files(directory: str, first_data: str, new_data: str, key: str):

    ''' The function executes the search of files ".json" on the specified path 
    inside the all tree, modifies substrings of an element by key in the found files.
    It accepts parameters of path, first_data, new_data and returns overwritten files.'''

    file_list = list(pathlib.Path(directory).rglob('*.json'))
    
    for entry in file_list:
        
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
        except json.JSONDecodeError:
            logger.warning(f'File {entry.name} is empty.')
            continue
        except KeyError:
            logger.warning(f'There is no key "{key}" in the file {entry.name}.')
            continue
        except TypeError:
            logger.critical('Check the data type in the arguments of the function.')
        except:
            logger.error(f'Error working the file {entry.name}.')
            continue

    #except IndexError:
            #logger.error('Not all parameters are entered!')
            #directory = input('Enter the directory: ')
            #first_data = input('Enter the first_data: ')
            #new_data = input('Enter the new_data: ')
            #key = input('Enter the key: ')

if __name__ == '__main__':
    #search_change_files('C:/Users/kuvsh/Desktop/Стажировка', 'f', 'ch', 'images') 
    search_change_files(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    #python main_pathlib.py C:/Users/kuvsh/Desktop/Стажировка f ch images