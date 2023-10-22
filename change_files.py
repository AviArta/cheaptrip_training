from my_logging import logger
import pathlib
import json
from datetime import datetime, date


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
            #with open(entry, 'w', encoding='UTF-8') as input_file:
                #json.dump(lines, input_file, indent=4)
                #logger.warning(f'File {entry.name} changed.')

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
    