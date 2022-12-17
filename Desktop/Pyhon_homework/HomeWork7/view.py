
def input_str():
    calc_str = input('Введите выражение для подсчета: ')
    calc_str = calc_str.replace(' ', '')
    calc_str = calc_str.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    return calc_str

def print_result(smth):
    print(smth)

