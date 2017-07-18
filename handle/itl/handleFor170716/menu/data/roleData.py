"""
数据定义
"""


class RoleData:
    # =========================== role ===========================
    ROLE = [
        {'old_code': 'firstPermissionSystemAdmin', 'code': '第一权限管理员'},
        {'old_code': 'projectManager', 'code': '项目负责人'},
        {'old_code': 'customerServiceManager', 'code': '客服负责人'},
        {'old_code': 'cleanerManager', 'code': '保洁负责人'},
        {'old_code': 'cleaner', 'code': '保洁'},
        {'old_code': 'gardenerManager', 'code': '绿化负责人'},
        {'old_code': 'gardener', 'code': '绿化'},
        {'old_code': 'securityManager', 'code': '保安负责人'},
        {'old_code': 'gateSentry', 'code': '门岗'},
        {'old_code': 'patrolPost', 'code': '巡逻岗'},
        {'old_code': 'monitoringPost', 'code': '监控岗'},
        {'old_code': 'carportSecurity', 'code': '车库岗'},
        {'old_code': 'engineeringManager', 'code': '工程负责人'},
        {'old_code': 'maintainer', 'code': '工程'},
        {'old_code': 'outsideMaintainer', 'code': '外部维修商'},
        {'old_code': 'subFinance', 'code': '财务'},
        {'old_code': 'schrodinger', 'code': '外围观测者'},
        {'old_code': 'toAppStore', 'code': '苹果审核专用'},

        {'old_code': 'patrolExecutive', 'code': '巡更'},
        {'old_code': 'industry Committee', 'code': '业委会'},

        {'old_code': 'customerService', 'code': '管家客服'},
    ]

    ROLE_ADD = [
        {'code': '前台客服'},
        {'code': '保安领班'},
        {'code': '高配'},
        {'code': '弱电'},
        {'code': '行政内务'},
        {'code': '抽检'},
        {'code': '小二'},
        {'code': '物业公司管理员'},
        {'code': '后台项目管理员'},
    ]

    ROLE_ALL = {'第一权限管理员': '第一权限管理员', '项目负责人': '项目负责人', '客服负责人': '客服负责人', '保洁负责人': '保洁负责人',
                '保洁': '保洁', '绿化负责人': '绿化负责人', '绿化': '绿化', '保安负责人': '保安负责人', '门岗': '门岗',
                '巡逻岗': '巡逻岗', '监控岗': '监控岗', '车库岗': '车库岗', '工程负责人': '工程负责人', '工程': '工程', '外部维修商': '外部维修商',
                '财务': '财务', '外围观测者': '外围观测者', '苹果审核专用': '苹果审核专用', '巡更': '巡更', '业委会': '业委会',
                '管家客服': '管家客服', '前台客服': '前台客服', '保安领班': '保安领班', '高配': '高配', '弱电': '弱电',
                '行政内务': '行政内务', '抽检': '抽检', '小二': '小二', '物业公司管理员': '物业公司管理员', '后台项目管理员': '后台项目管理员'
                }
