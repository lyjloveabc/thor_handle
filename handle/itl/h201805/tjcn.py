with open('he.txt', 'r') as f:
    sum = 0
    idx = 0
    for line in f.readlines():
        sum += int(line.replace('\n', ''))
        idx += 1

print(idx)
print(sum)
print(sum / idx)
