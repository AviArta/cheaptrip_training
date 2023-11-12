from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
from pydantic import BaseModel
from typing import Union

from my_logging import logger
from my_parser import args
from my_decorators import working_time_decorator


@working_time_decorator
def search_change_files(directory: str, first_substr: str, new_substr: str, key: str='images'):  
    ''' The function executes the search of files ".json" on the specified path 
    inside the all tree, modifies substrings of an element by key in the found files.
    It accepts parameters of path, first_data, new_data, key and overwrites files.
       To run code from the command line you need to enter the required parameters:
    '''
    counter_files = 0 
    counter_change_files = 0
   
    for one_file in Path(directory).rglob('*.json'):
        try:
            start_data = read_file(one_file)
            counter_files += 1
            if start_data[key]:
                start_value = start_data[key]
                modify_d = Modify_Data(st_val=start_value, f_substr=first_substr, n_substr=new_substr, k=key)
                start_data[key] = modify_d.modify_data(start_value, first_substr, new_substr, key)
                overwrite_file(one_file, start_data)
                counter_change_files += 1
            
        except (json.JSONDecodeError, KeyError):
            continue
        except:
            logger.error(f'Error working the file {one_file.name}.')
            continue

    print(f'Number of json files: {counter_files}.', f'Number of modified files: {counter_change_files}.',
           f'The program is completed.', sep='\n')


#@working_time_decorator
def read_file(one_file: str) -> list: 
    ''' The function read file. It accepts parameter of file path and returns list of data
    from file.
    '''
    with open(one_file, encoding='UTF-8') as input_file:
        return json.load(input_file)


class Modify_Data(BaseModel):
    st_val: Union[str, list]
    f_substr: str
    n_substr: str
    k: str

    #@working_time_decorator
    def modify_data(self, start_value: list or str, first_substr: str, new_substr: str, key: str) -> list:
        ''' The function creats the modified value-substrings by key. 
        It accepts parameters: value by key, first substring, new substring, key for changing value,
        variable for counting modified files. The function returns modify list.
        '''
        if isinstance(start_value, list):
            start_value = [element if type(element) != str else element.replace(first_substr, new_substr) for element in start_value]           
        elif isinstance(start_value, str):
            start_value = start_value.replace(first_substr, new_substr)
        return start_value


#@working_time_decorator
def overwrite_file(one_file: str, result_lines: list):
    ''' The function overwrites modified data to the file. It accepts file path and 
    modified list, it doesn't return anything.
    '''
    with open(one_file, 'w', encoding='UTF-8') as input_file:
        json.dump(result_lines, input_file, indent=4)
        #logger.warning(f'File {entry.name} changed.')


if __name__ == '__main__': 
    #search_change_files(args.directory, args.first_data, args.new_data, args.key)
    #search_change_files(args.directory, args.first_data, args.new_data, args.key)
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        future = executor.submit(search_change_files, args.directory, args.first_data, args.new_data, args.key)
        result = future.result()
# input in console line: python change_files_fp.py --help
# input in console line: python change_files.py C:/Users/kuvsh/Desktop/Стажировка f ch -k images