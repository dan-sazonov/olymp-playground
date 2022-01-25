from operator import itemgetter

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(list(map(itemgetter(0), sorted(my_dict.items(), key=itemgetter(1))[-3:])))

# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3] - в одну строку
