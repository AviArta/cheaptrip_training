import pathlib
import json
import logging
from datetime import datetime


logger = logging.getLogger(__name__)
#logfile_name = f'{pathlib.Path(__file__).name}_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log'
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(f'{__name__}.log', mode='w')
formatter = logging.Formatter('%(funcName)s %(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def search_change_files(directory: str, first_data: str, new_data: str, key: str='images'):

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
            if key in lines.keys():
                if isinstance(lines[key], list):
                    lines[key] = [element.replace(first_data, new_data) for element in lines[key] if type(element) == str]
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
        except TypeError:
            logger.critical('Check the data type in the arguments of the function.')
        except:
            logger.error(f'Error working the file {entry.name}.')
            continue


#if __name__ == '__main__':
search_change_files('C:/Users/kuvsh/Desktop/Стажировка', 'f', 'ch') 