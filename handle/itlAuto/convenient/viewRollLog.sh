#!/usr/bin/env bash
# Created by Thor on 2018-09-30

MAIN_PATH=/home/lufei/lyj

case "$1" in
    "m")
        echo "      "
        echo "      "
        echo "****************** welcome view log ******************"
        echo "      "
        echo "./viewRollLog.sh   不带参数或带1个参数都是有效的"
        echo "m -> menu          打印菜单"
        echo "a -> admin         查看物业后台系统的日志"
        echo "c -> cloud         查看app支撑服务的日志"
        echo "e -> eye           查看天眼后台系统的日志"
        echo "o -> operation     查看小二后台系统的日志"
        echo "  -> cloud         不输入任何参数则查看app支撑服务的日志"
        echo "      "
        echo "****************** ^_^ happy coding ******************"
        echo "      "
        echo "      "
        ;;
    "c")
        tail -f ${MAIN_PATH}/logs/cloud-web/roll.log
        ;;
    "a")
        tail -f ${MAIN_PATH}/logs/admin-web/roll.log
        ;;
    "e")
        tail -f ${MAIN_PATH}/logs/eye-web/roll.log
        ;;
    "o")
        tail -f ${MAIN_PATH}/logs/operation-web/roll.log
        ;;
    "")
        tail -f ${MAIN_PATH}/logs/cloud-web/roll.log
        ;;
    *)
        tail -f ${MAIN_PATH}/logs/$1-web/roll.log
        ;;
esac

# cloud
# admin
# eye
# operation
# auth

# 同志们，服务端日志进行了革命性优化。解决了实时滚动日志一直增大(还无法被删除)、日志增长服务器存储爆炸、发布后的遗留日志、各Java系统日志存储混乱、查看日志不方便等灾难性问题。

# 针对大家的切身需求，查看日志直接运行服务器上的[viewRollLog.sh]shell脚本文件(不带参数或带1个参数都是有效的)，没包括业委会项目，烦请 @龙环 节后回来看下。

# [viewRollLog.sh]这个文件一般在Java服务的主目录，即线上在/home/lyj、预发布在/root/zSky、测试在/home/lufei/lyj

# 启动方式不变，还是在那些脚本运行就行了。

# 注意：Java服务的主目录里面的任务文件千万不要去删除！！！
