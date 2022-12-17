calc_str = ' '

def get_calc_str():
    global calc_str
    return calc_str

def set_calc_str(smth):
    global calc_str
    calc_str = smth

def calculate_str(sm_str: str):
    sm_list = sm_str.split()
    for i in range(len(sm_list)):
        if sm_list[i].isdigit():
            sm_list[i] = int(sm_list[i])
    while ('*' in sm_list) or ('/' in sm_list):
        i = 0
        while i < len(sm_list):
            if sm_list[i] == "*":
                sm_list[i-1] = sm_list[i-1] * sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])

            elif sm_list[i] == "/":
                sm_list[i-1] = sm_list[i-1] / sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])

            else:
                i += 1

    while ('+' in sm_list) or ('-' in sm_list):
        i = 0
        while i < len(sm_list):
            if sm_list[i] == "+":
                sm_list[i-1] = sm_list[i-1] + sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])

            elif sm_list[i] == "-":
                sm_list[i-1] = sm_list[i-1] - sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])
            else:
                i += 1

    return sm_list[0]