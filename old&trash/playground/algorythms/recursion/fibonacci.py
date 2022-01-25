# Мое:
def fib(number):
    if number < 3:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)



n = 4000000
print(fib(n))
