def arithmetic(first_number, second_number, sign):
    if sign == '+':
        return first_number + second_number
    elif sign == '-':
        return first_number - second_number
    elif sign == '*':
        return first_number * second_number
    elif sign == '/':
        return first_number / second_number
    else:
        return "Неизвестная операция"