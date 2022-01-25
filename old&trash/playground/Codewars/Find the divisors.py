def divisors(integer):
    divs = [i for i in range(2, integer) if integer % i == 0]
    return divs if divs else '{} is prime'.format(integer)
