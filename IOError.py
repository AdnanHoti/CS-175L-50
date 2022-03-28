try:
    read_file = open('numbers.txt','r')

    file_numbers = read_file.read()

    read_file.close()

    list_values = file_numbers.split()

    list_length = len(list_values)

    try:
        for i in range(list_length):
            list_values[i] = float(list_values[i])
            List_sum = sum(list_values)
            Average_value = (List_sum)/list_length
            print(Average_value)

    except ValueError:
        print('File must have only numbers.')

except IOError:
    print('Trouble opening file')
