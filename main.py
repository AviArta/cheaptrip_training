from change_files import search_change_files, args


if __name__ == '__main__':
    #search_change_files('C:/Users/kuvsh/Desktop/Стажировка', 'f', 'ch', 'images') 
    search_change_files(args.directory, args.first_data, args.new_data, args.key)