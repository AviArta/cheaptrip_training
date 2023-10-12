import pathlib
import json
import logging

logging.basicConfig(level='ERROR', filename='logs.log', filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()

def search_change_files(directory: str, first_data: str, new_data: str, key: str='images') -> list:

    ''' The function executes the search of files ".json" on the specified path 
    inside the all tree, modifies substrings of an element by key in the found files.
    It accepts parameters of path, first_data, new_data and returns overwritten files.'''

    file_list = list(pathlib.Path(directory).rglob('*.json'))
    
    for entry in file_list:
        logger.error(f'File name: {entry.name}')
        
        try:
            # reading each file:
            with open(entry, encoding='UTF-8') as input_file:
                lines = json.load(input_file)

            # creating the dictionary with modified substrings by key:
            for k, v in lines.items():
                if k != key:
                    continue
                if isinstance(lines[k], list): 
                    # changing substring 'first_data' to substring 'new_data':
                    lines[k][0] = lines[k][0].replace(first_data, new_data)
            logger.error(f'new lines: {lines}')
            
            # recording modified data:
            with open(entry, 'w', encoding='UTF-8') as input_file:
                json.dump(lines, input_file, indent=4)  # result_dict
            logger.error(f'File {entry.name} changed.')

        except FileNotFoundError:
            logger.error('Files ".json" are not found on the specified path.')
            continue
        except json.JSONDecodeError:
            logger.error(f'File {entry.name} is empty.')
            continue
        except TypeError:
            logger.error('Check the data type in the arguments of the function.')
        except:
            logger.error(f'Error working the file {entry.name}.')
            continue


if __name__ == '__main__':
    search_change_files('C:/Users/kuvsh/Desktop/Стажировка — копия', 'f', 'ch')   
