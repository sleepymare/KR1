import json
import re

def decode_ch(string_of_elements):
    with open("periodic_table.json", encoding='utf-8') as read_file:
        periodic_table = json.load(read_file)

    result = ''
    arr = re.findall('[A-Z][^A-Z]*', string_of_elements)
    # print(arr)
    for elem in arr:
        result += periodic_table[elem]
    return result



