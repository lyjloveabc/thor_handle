"""
数据定义
"""


class MenuData:
    # =========================== permission ===========================
    COMMON_PLUS = [
        {'code': 'commonTool_releaseTask', 'name': '发布任务', 'menu_type': '1', 'sort_num': '1', 'menu_kind': 'COMMONLY_TOOL'},
        {'code': 'commonTool_releaseMatter', 'name': '发布报事', 'menu_type': '2', 'sort_num': '2', 'menu_kind': 'COMMONLY_TOOL'},
        {'code': 'commonTool_releaseRepair', 'name': '发布报修', 'menu_type': '3', 'sort_num': '3', 'menu_kind': 'COMMONLY_TOOL'}
    ]

    TOOLS = [
        {'code': 'housekeeper_dataCenter', 'name': '数据中心', 'menu_type': '10001', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png',
         'sort_num': '1000', 'function_url': 'http://eye.itianluo.cn/#/login'},
        {'code': 'housekeeper_repair', 'name': '报修', 'menu_type': '1', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-baoxiu@3x.png',
         'sort_num': '999'},
        {'code': 'housekeeper_postThing', 'name': '报事', 'menu_type': '2', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-baoxiu@3x.png',
         'sort_num': '998'},
        {'code': 'housekeeper_complaint', 'name': '投诉', 'menu_type': '3', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-tousu@3x.png',
         'sort_num': '997'},
        {'code': 'housekeeper_praise', 'name': '表扬', 'menu_type': '4', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-biaoyang@3x.png',
         'sort_num': '996'},
        {'code': 'housekeeper_consulting', 'name': '咨询', 'menu_type': '5', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-zixun@3x.png',
         'sort_num': '995'},
        {'code': 'housekeeper_transformWork', 'name': '倒班', 'menu_type': '6', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-gangweitiaozheng@3x.png',
         'sort_num': '994'},
        {'code': 'housekeeper_staffInfo', 'name': '员工信息', 'menu_type': '7', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-yuangong@3x.png',
         'sort_num': '993'},
        {'code': 'housekeeper_propertyCharge', 'name': '物业收费', 'menu_type': '8', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-wuyeshoufei@3x.png',
         'sort_num': '992'},
        {'code': 'housekeeper_otherCharge', 'name': '其他收费', 'menu_type': '9', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-qitashoufei@3x.png',
         'sort_num': '991'},
        {'code': 'housekeeper_energyReading', 'name': '能耗抄表', 'menu_type': '10', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-nenghao@3x.png',
         'sort_num': '990'},
        {'code': 'housekeeper_accessManage', 'name': '出入管理', 'menu_type': '11', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-churu@3x.png',
         'sort_num': '989'},
        {'code': 'housekeeper_express', 'name': '快递', 'menu_type': '12', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-kuaidi@3x.png',
         'sort_num': '988'},
        {'code': 'housekeeper_household', 'name': '住户情况', 'menu_type': '13', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-zhuhu@3x.png',
         'sort_num': '987'},
        {'code': 'housekeeper_taskCenter', 'name': '任务中心', 'menu_type': '14', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-zhuhu@3x.png',
         'sort_num': '986'},
        {'code': 'housekeeper_patrolLog', 'name': '巡更记录', 'menu_type': '15', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-xungeng@3x.png',
         'sort_num': '985'},
        {'code': 'housekeeper_samplingLog', 'name': '抽检记录', 'menu_type': '16', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-choujian@3x.png',
         'sort_num': '984'},
        {'code': 'housekeeper_launchApproval', 'name': '发起审批', 'menu_type': '17', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-choujian@3x.png',
         'sort_num': '983'},
        {'code': 'housekeeper_bonusPoint', 'name': '加分扣分', 'menu_type': '18', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-jiafen@3x.png',
         'sort_num': '982'},
        {'code': 'housekeeper_summaryPlan', 'name': '总结计划', 'menu_type': '19', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-zongjie@3x.png',
         'sort_num': '981'},
        {'code': 'housekeeper_draftBox', 'name': '草稿箱', 'menu_type': '20', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png',
         'sort_num': '980'}
    ]

    MY = [
        {'code': 'HOUSEKEEPER_MY_TAB_更多', 'name': '更多', 'menu_type': '1', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_负责小区', 'name': '负责小区', 'menu_type': '2', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_岗位职责', 'name': '岗位职责', 'menu_type': '3', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_我发布的任务', 'name': '我发布的任务', 'menu_type': '4', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_我发布的报修', 'name': '我发布的报修', 'menu_type': '5', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_我发布的报事', 'name': '我发布的报事', 'menu_type': '6', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_我发布的审批', 'name': '我发布的审批', 'menu_type': '7', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_我的考勤', 'name': '我的考勤', 'menu_type': '8', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_待完成任务', 'name': '待完成任务', 'menu_type': '9', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_待我审批', 'name': '待我审批', 'menu_type': '10', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_收到的投诉', 'name': '收到的投诉', 'menu_type': '11', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'},
        {'code': 'HOUSEKEEPER_MY_TAB_收到的表扬', 'name': '收到的表扬', 'menu_type': '12', 'sort_num': '1000', 'icon_url': 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png'}
    ]
