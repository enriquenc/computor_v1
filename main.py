import re

def parse_string(str):
    str = str.replace(' ', '')
    print(str)
    res = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+|=", str)
    print(res)

if __name__ == '__main__':
    input_string = input()
    parse_string(input_string)
