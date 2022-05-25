def calculate(path2file):
    given_file = open(path2file, 'r')
    result = ''
    lines = given_file.readlines()

    for line in lines:
        arr = line.split()
        num = eval(f'{arr[1]}{arr[0]}{arr[2]}')
        result += str(num) + ','

    given_file.close()

    return result[:len(result)-1]



