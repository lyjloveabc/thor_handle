"""
2017-07-16五彩石项目测试
数据初始化脚本
"""
from handle.itl.handleFor170716.fee.createParking import CreateParking
from handle.itl.handleFor170716.menu.createMenu import CreateMenu
from handle.itl.handleFor170716.paddingData.paddingData import PaddingData

if __name__ == '__main__':
    # 创建管家端涉及到的所有菜单、以及角色对应这些菜单
    createMenu = CreateMenu()
    createMenu.handle()

    # 账单数据填充，user_id字段填充
    paddingData = PaddingData()
    paddingData.handle()

    # 创建一个车位费，翡翠城订阅这个车位费
    createParking = CreateParking()
    createParking.handle()
