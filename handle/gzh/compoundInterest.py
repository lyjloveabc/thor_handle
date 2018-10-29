"""
复利相关计算
"""


class CompoundInterest:
    @staticmethod
    def calc_after(n, year_money, year_increase):
        """
        计算n年后，的定投收益
        :param n: n年后
        :param year_money: 每年结余
        :param year_increase: 年收益
        :return: n年后本息总和
        """
        after_n_money = 0  # n年后总的钱
        for i in range(0, n):
            after_n_money = (year_money + after_n_money * (1 + year_increase))

        return after_n_money


if __name__ == '__main__':
    ci = CompoundInterest()

    CompoundInterest.calc_after(40, 24000, 0.1)
