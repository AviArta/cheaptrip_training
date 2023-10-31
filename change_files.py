import pathlib
import json

from my_logging import logger
from my_parser import args

def search_change_files(directory: str, first_data: str, new_data: str, key: str):  # key: str = 'images'
    ''' The function executes the search of files ".json" on the specified path 
    inside the all tree, modifies substrings of an element by key in the found files.
    It accepts parameters of path, first_data, new_data, key and overwrites files.
       To run code from the command line you need to enter the required parameters:
    '''
    counter_files = 0 
    counter_change_files = 0
   
    for one_file in pathlib.Path(directory).rglob('*.json'):
        try:
            # reading each file:
            with open(one_file, encoding='UTF-8') as input_file:
                lines = json.load(input_file)
                counter_files += 1

            # creating the dictionary with modified substrings by key:
            if isinstance(lines[key], list):
                lines[key] = [element if type(element) != str else element.replace(first_data, new_data) for element in lines[key]]
                counter_change_files += 1            
            elif isinstance(lines[key], str):
                lines[key] = lines[key].replace(first_data, new_data)
                counter_change_files += 1
            
            # recording modified data:
            with open(one_file, 'w', encoding='UTF-8') as input_file:
                json.dump(lines, input_file, indent=4)
                #logger.warning(f'File {entry.name} changed.')

        except FileNotFoundError:
            logger.error('Files ".json" are not found on the specified path.')
            continue
        except (json.JSONDecodeError, KeyError):
            continue
        except TypeError:
            logger.critical('Check the data type in the arguments of the function.')
        except:
            logger.error(f'Error working the file {one_file.name}.')
            continue
        
    print(f'Number of json files: {counter_files}', f'Number of modified files: {counter_change_files}.', f'The program is completed.', sep='\n')


if __name__ == '__main__':
    #search_change_files('C:/Users/kuvsh/Desktop/Стажировка', 'f', 'ch', 'images') 
    search_change_files(args.directory, args.first_data, args.new_data, args.key)