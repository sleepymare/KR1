import string

def is_palindrome(my_string):
    new_str = ""
    reverse_str = ""

    for x in my_string.strip():
        new_str = new_str + x.replace(" ", "")
        reverse_str = x.replace(" ", "") + reverse_str

    # print(new_str)
    # print(reverse_str)

    new_str = new_str.translate(str.maketrans('', '', string.punctuation))
    # print(new_str)
    reverse_str = reverse_str.translate(str.maketrans('', '', string.punctuation))
    # print(reverse_str)

    new_str = ''.join([i for i in new_str if not i.isdigit()])
    reverse_str = ''.join([i for i in reverse_str if not i.isdigit()])

    # print(new_str)
    # print(reverse_str)

    if new_str.lower() == reverse_str.lower():
        print("YES")
    else:
        print("NO")



