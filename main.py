from change_files import search_change_files
import sys

if __name__ == '__main__':
    #search_change_files('C:/Users/kuvsh/Desktop/Стажировка', 'f', 'ch', 'images') 
    search_change_files(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    #python main_pathlib.py C:/Users/kuvsh/Desktop/Стажировка f ch images
    help(search_change_files)