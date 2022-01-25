seat = int(input('Введите номер места: '))
if seat <= 36:
    coupe = (seat - 1) // 4 + 1
elif seat <= 54:
    coupe = (54 - seat) // 2 + 1
else:
    coupe = 'error'
    print('Ошибка при вводе. Попробуйте снова')
print('Номер купе: ', coupe)
input('Для закрытия нажмите клавишу [Enter]')