import argparse


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