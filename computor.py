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
    print(res)
    for i in range(1, len(digits), 2):
        res[int(digits[i])] = res[int(digits[i])] + float(digits[i - 1])
    return res


def calculate_final_coefficients(left_digits, right_digits):
    for i in range(len(left_digits)):
        left_digits[i] = left_digits[i] - right_digits[i]
    return left_digits

def get_reduced_form(coefficients):
    reduced_form = ""
    for coeff in coefficients:
        reduced_form = reduced_form + str(coeff) + ' * ' + 'X^' + coefficients.index(coeff)
    return reduced_form


def print_answer(coefficients, degree):
    print('Reduced form: ' + get_reduced_form(coefficients))


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



