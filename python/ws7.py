def file_handling():
    '''
    This functions handles files, reads single line, multi line
    '''
    my_file = open(" file.txt",'r')
    one_line = my_file.readline()
    multiple_lines = my_file.readlines()

    print(one_line)
    print(multiple_lines)
    my_file.close()
file_handling()