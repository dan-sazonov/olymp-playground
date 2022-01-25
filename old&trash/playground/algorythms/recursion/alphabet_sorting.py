with open('in.txt', encoding='windows-1251') as f_read:
    items = f_read.read().split('\n')


def sort(names):
    if len(names) < 2:
        return names
    else:
        pivot = names[0]
        less = [i for i in names[1:] if i <= pivot]
        greater = [i for i in names[1:] if i > pivot]

        return sort(less) + [pivot] + sort(greater)


with open('out.txt', 'w') as f_print:
    for item in sort(items):
        f_print.write(item + '\n')
