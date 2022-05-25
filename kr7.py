def substring_slice(path2file_1, path2file_2):
    given_file1 = open(path2file_1, 'r')
    given_file2 = open(path2file_2, 'r')
    result = ''
    lines1 = given_file1.readlines()
    lines2 = given_file2.readlines()

    for x in range(len(lines1)):
        arr = lines2[x].split()
        result += lines1[x][int(arr[0]):int(arr[1])+1] + ' '

    given_file1.close()
    given_file2.close()

    return result[:len(result)-1]




