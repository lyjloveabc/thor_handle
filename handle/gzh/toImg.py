# 复利计算
year_money = 24000  # 每年结余
year_increase = 0.1  # 年收益
after_n_money = 0  # n年后总的钱

n = 40  # 计算n年

for i in range(0, n):
    after_n_money = (year_money + after_n_money * (1 + year_increase))

print(after_n_money)


