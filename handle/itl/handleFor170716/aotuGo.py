"""
2017-07-16五彩石项目测试
数据初始化脚本
"""
from handle.itl.handleFor170716.dbUtil import DbUtil
from handle.itl.handleFor170716.fee.createParking import CreateParking
from handle.itl.handleFor170716.menu.createMenu import CreateMenu
from handle.itl.handleFor170716.paddingData.paddingData import PaddingData

if __name__ == '__main__':
    dbUtil = DbUtil()

    # 创建管家端涉及到的所有菜单、以及角色对应这些菜单
    createMenu = CreateMenu(**{'dbUtil': dbUtil})
    createMenu.handle()

    # 账单数据填充，user_id字段填充
    paddingData = PaddingData(**{'dbUtil': dbUtil})
    paddingData.handle()

    # 创建一个车位费，翡翠城订阅这个车位费
    createParking = CreateParking(**{'dbUtil': dbUtil})
    createParking.handle()
