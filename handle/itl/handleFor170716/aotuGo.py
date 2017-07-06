"""
2017-07-16五彩石项目测试
数据初始化脚本
"""
from handle.itl.handleFor170716.menu.createMenu import CreateMenu

if __name__ == '__main__':
    # 创建管家端涉及到的所有菜单、以及角色对应这些菜单
    createMenu = CreateMenu()
    createMenu.handle()

    # 停车费

