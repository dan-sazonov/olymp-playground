# 42 балла. Правильное: informatics 113757

from statistics import mean

a = int(input())
b = int(input())
c = int(input())
marks = [2] * a + [3] * b + [4] * c
counter = 0

while round(mean(marks)) < 4:
    marks.append(5)
    counter += 1

# print(marks, mean(marks))
print(counter)
