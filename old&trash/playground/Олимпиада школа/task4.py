for k in range(100, 999):
    x = k % 10
    y = (k // 10) % 10
    z = k // 100
    if (x != y) and (y != z) and (x != z):
        print(k)
input('Для закрытия нажмите клавишу [Enter]')