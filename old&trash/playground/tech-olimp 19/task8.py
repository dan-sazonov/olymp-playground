sellers = [52518, 718438, 358883, 462189, 853171, 592966, 225788, 46977, 814826, 295697, 676256, 561479, 56545, 764281]
maximal = max(sellers)
credit = 0
for c in range(0, 14):
    credit +=  maximal - sellers[c]

print(credit)