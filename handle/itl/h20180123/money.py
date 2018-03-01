source = 1000.00
n = 1
count = 3
some_time_sum = 0
now = 1754.41
other = 0

while n <= count:
    this_time = source * (1.008 ** (n - 1))
    some_time_sum += this_time
    print(n, this_time)
    n += 1

print(some_time_sum)
print(some_time_sum - (now - other))


# 6134.65
