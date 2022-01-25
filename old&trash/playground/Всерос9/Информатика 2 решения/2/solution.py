s = input()
ans = 0
digits = {"I": 1, "V": 5, "X": 10, "IV": 4, "IX": 9, "L": 50, "C": 100, "XL": 40, "XC": 90, "D": 500, "M": 1000, "CD": 400, "CM": 900}
i = len(s) - 1
while i >= 0:
    num2 = s[i - 1:i + 1]
    num1 = s[i]
    if i > 0 and num2 in digits:
        ans += digits[num2]
        i -= 2
    else:
        ans += digits[num1]
        i -= 1
print(ans)
