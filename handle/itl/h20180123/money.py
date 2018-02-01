source = 1000.00
n = 0
count = 2
some_time_sum = 0
now = 967.60
other = 0

while n < count:
    this_time = source * (1.008 ** n)
    some_time_sum += this_time
    print(n + 1, this_time)
    n += 1

print(some_time_sum)
print(some_time_sum - (now - other))
