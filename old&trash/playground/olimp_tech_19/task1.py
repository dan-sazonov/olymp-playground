with open('input.txt') as file_read:
    n = int(file_read.read())
    assert (n <= 10 ** 18)

with open('output.txt', 'w') as file_print:
    file_print.write('2' if n % 2 == 0 else '1')
