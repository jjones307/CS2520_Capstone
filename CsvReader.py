def reader():
    file_obj = open("GermanNames.csv", 'r')
    for line in file_obj:
        string_obj = line.strip().replace(' ', '')
        yield string_obj.split(',')
    file_obj.close()


def main():
    str_obj = reader()
    while True:
        try:
            print(next(str_obj))
        except StopIteration:
            break
    print("end of program")


if __name__ == '__main__':
    main()
