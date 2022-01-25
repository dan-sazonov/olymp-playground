password = input()


def validator(password):
    return (len(password) in range(5, 11)) and (any((char.isdigit()) and (not char.isspace()) and (not char.isalpha())) for char in password)


print(validator(password))