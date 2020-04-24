#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 错误日志
ERROR_LOG_FILE = os.path.join(BASEDIR, "log", 'error.log')
# 运行日志
RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'run.log')


# 是否测试模式，测试模时候数据从files目录下读取
TEST_MODE = False

# 采集资产的方式，选项有：agent(默认), salt, ssh
MODE = 'ssh'

# 如果采用SSH方式，则需要配置SSH的KEY和USER
SSH_PRIVATE_KEY = "/home/auto/.ssh/id_rsa"
SSH_USER = "root"
SSH_PORT = 22
SSH_PASSWD = '1qazXDR%'
HOSTS=["192.168.149.129","192.168.149.139"]

# 采集硬件数据的插件
PLUGINS_DICT = {
    'cpu': 'src.plugins.cpu.CpuPlugin',
    'disk': 'src.plugins.disk.DiskPlugin',
    'main_board': 'src.plugins.main_board.MainBoardPlugin',
    'memory': 'src.plugins.memory.MemoryPlugin',
    'nic': 'src.plugins.nic.NicPlugin',
}
