def up_to_end(start_share_price, position_num, change_rate, change_num):
    """
    # 情况1：一路上涨
    :param start_share_price: 初始股价
    :param position_num: 持仓股数
    :param change_rate: 上涨比率
    :param change_num: 卖出股数
    :return: 最终多少钱
    """
    final_money = 0

    this_time_sp = start_share_price
    normal_time = int(position_num / change_num)
    tail_num = position_num % change_num

    for time in range(0, normal_time):
        this_time_sp = this_time_sp * (1 + change_rate)
        print(this_time_sp)
        final_money += this_time_sp * change_num

    if tail_num > 0:
        this_time_sp = this_time_sp * (1 + change_rate)
        final_money += this_time_sp * tail_num
    return final_money


start_share_price = 31.1
position_num = 700

print(up_to_end(start_share_price, position_num, 0.03, 200))

# print(up_to_end(start_share_price, position_num, 0.02, 100))
# print(up_to_end(start_share_price, position_num, 0.02, 200))
# print(up_to_end(start_share_price, position_num, 0.03, 100))
# print(up_to_end(start_share_price, position_num, 0.03, 200))
# print(up_to_end(start_share_price, position_num, 0.04, 100))
# print(up_to_end(start_share_price, position_num, 0.05, 200))

#
# print(32.344 * 200 + 33.63776 * 200 + 34.9832704 * 200 + 36.382601216000005 * 100)
# print(21770 + 12233.68)
# print((21770 + 12233.68) - (32.344 * 200 + 33.63776 * 200 + 34.9832704 * 200 + 36.382601216000005 * 100))
# print(10172.4137984 / 34003.68)


