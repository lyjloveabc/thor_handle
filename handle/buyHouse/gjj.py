base = 3218
average = 2000
sum_money = 0
month_num = 13

for index in range(1, month_num + 1):
    sum_money += (base + average * index)
    print(index, sum_money)

print("-----")
print("总额", sum_money)
print("月均余额", sum_money / month_num)
print("15倍计算", (sum_money / month_num) * 15)
