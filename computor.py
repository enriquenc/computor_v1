import re


def split_equals(string):
    string = string.replace(' ', '')
    return string.split('=')


def check_degree(splited):
    return max(filter(lambda a: splited.index(a) % 2 != 0, splited))


def parse_digits(str):
    digits = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+|=", str)
    if len(digits) == 1:
        return []
    return digits


def structure_coefficients(digits, degree):
    res = [0] * (degree + 1)
    for i in range(1, len(digits), 2):
        res[int(digits[i])] = res[int(digits[i])] + float(digits[i - 1])
    return res


def calculate_final_coefficients(left_digits, right_digits):
    for i in range(len(left_digits)):
        left_digits[i] = left_digits[i] - right_digits[i]
    return left_digits


def put_sign(digit, index):
    if digit == 0:
        return ' + 0'
    if index > 0:
        if digit > 0:
            return ' + ' + str(digit).rstrip('.0')
        else:
            return ' - ' + str(digit * -1).rstrip('.0')
    return str(digit).rstrip('.0')

def get_reduced_form(coefficients):
    reduced_form = ""
    for i in range(len(coefficients)):
        reduced_form = reduced_form + put_sign(coefficients[i], i) + ' * ' + 'X^' + str(i)
    reduced_form = reduced_form + ' = 0'
    return reduced_form


def print_answer(coefficients, degree):
    print('Reduced form: ' + get_reduced_form(coefficients))
    print('Polynomial degree: ' + str(degree))


if __name__ == '__main__':
    input_string = input()
    splited = split_equals(input_string)
    left_digits = parse_digits(splited[0])
    right_digits = parse_digits(splited[1])
    degree = int(max(check_degree(left_digits), check_degree(right_digits)))
    left_digits = structure_coefficients(left_digits, degree)
    right_digits = structure_coefficients(right_digits, degree)
    coefficients = calculate_final_coefficients(left_digits, right_digits)
    print_answer(coefficients, degree)



