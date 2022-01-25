def is_year_leap(year):
    if (year % 400) == 0: #Почему?!
        return True
    if year % 4 == 0 and year % 100 != 0: #Почему?!
        return True
    return False