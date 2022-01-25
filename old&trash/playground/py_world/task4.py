def season(month):
    if (month >= 1) and (month <= 2) or month == 12: #надо так: if month in (12, 1, 2)
        return 'зима'
    elif (month >= 3) and (month <= 5):
        return 'весна'
    elif (month >= 6) and (month <= 8):
        return 'лето'
    elif (month >= 9) and (month <= 11):
        return 'осень'
    else:
        return 'invalid'
''' 
#DEBUGING
for c in range(1, 13):
    print(c, season(c))
'''