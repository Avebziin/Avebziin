def reader(file_directory):
    try:
        with open(file_directory, 'r') as file_input:
            reader = file_input.readlines()
            list_of_int = []
            for each in reader:
                each = each.strip()
                list_of_int.append(int(each))
    except IOError as problem:
        print("Error:", problem)
        exit()
    
    return list_of_int

def is_armstrong_number(number):
    str_number = str(number)
    print(str_number)
    num_digits = len(str_number)
    sum_of_digits = 0

    for digit in str_number:
        sum_of_digits += int(digit) ** num_digits

    if sum_of_digits == number:
        return True
    else:
        return False

def write(file_directory_2, data):
    try:
        with open(file_directory_2, 'w') as file_input2:
            for item in data:
                if is_armstrong_number(item): #if true
                    file_input2.write(str(item) + '\n')
    except IOError as problem:
        print("Error2:", problem)
        exit()

file_path = "numbers.txt"
file_path2 = "armstrong.txt"

data = reader(file_path)
write(file_path2, data)