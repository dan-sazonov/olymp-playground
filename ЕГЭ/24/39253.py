with open('16.txt') as f:
    f = f.read().strip()

seq = list(map(len, f.split('D')))
result = max(map(sum, zip(seq, seq[1:])))+1 if len(seq) > 1 else len(f)

print(result)