#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import time
import hashlib
import requests
from src import plugins
from lib.serialize import Json
from lib.log import Logger
from config import settings

from concurrent.futures import ThreadPoolExecutor


class AutoBase(object):
    def __init__(self):
        pass

 

    def process(self):
        """
        派生类需要继承此方法，用于处理请求的入口
        :return:
        """
        raise NotImplementedError('you must implement process method')


class AutoAgent(AutoBase):
    def __init__(self):
        super(AutoAgent, self).__init__()

    def process(self):
        """
        :return:
        """
        server_info = plugins.get_server_info()
        if not server_info.status:
            return
        server_json = Json.dumps(server_info.data)
        print(server_json)

        return server_json


class AutoSSH(AutoBase):
    def process(self):
        """
        根据主机名获取资产信息，将其发送到API
        :return:
        """
        #task = #{"data": [{"hostname": "c1.com"}, {"hostname": "c2.com"}], "error": null, "message": null, "status": true}
        """
        pool = ThreadPoolExecutor(10)
        for item in task['data']:
            hostname = item['hostname']
            pool.submit(self.run, hostname)
        pool.shutdown(wait=True)
        """
        #print('AutoSSH')
        #单线程
        """
        for hostname in settings.HOSTS:
            server_info = plugins.get_server_info(hostname)
            #print(hostname)
            server_json = Json.dumps(server_info.data)
            print(server_json)
            #return server_json
        """
        #多线程
        pool = ThreadPoolExecutor(2)
        for hostname in settings.HOSTS:
            pool.submit(self.run, hostname)
        pool.shutdown(wait=True)

    def run(self, hostname):
        server_info = plugins.get_server_info(hostname)
        server_json = Json.dumps(server_info.data)
        print(server_json)

        


class AutoSalt(AutoBase):
    def process(self):
        # 获取指定主机名的资产信息

        server_info = plugins.get_server_info('hostname')
        server_json = Json.dumps(server_info.data)
        return server_json

