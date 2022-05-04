def reader():
    file_obj = open("names.csv", 'r')
    for line in file_obj:
        string_obj = line.rstrip()
        yield string_obj.split(',')
    file_obj.close()
