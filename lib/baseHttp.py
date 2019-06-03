#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author: zz

@License: (C) Copyright 2013-2017, 

@Contact: zhangzhe0707@gmail.com

@Software: PyCharm

@File: baseHttp.py

@Time: 2019-05-18 17:07

@Desc:

'''

import requests
import json
import logging
from lib.baseCode import BaseCode


class BaseHttp:
    """
    http请求封装类
    """

    def __init__(self):
        baseCode = BaseCode()
        self.logger = logging.getLogger()
        self.env_data = baseCode.get_env_data()
        self.timeout = self.env_data['envTimeout']
        if self.env_data['envPort']:
            self.url = self.env_data['envScheme'] + '://' + self.env_data['envBaseUrl'] +\
                       ':' + self.env_data['envPort']
        else:
            self.url = self.env_data['envScheme'] + '://' + self.env_data['envBaseUrl']


    def change_type(self, value):
        """
        对字典中的value值的中文进行识别转换
        :param value:
        :return:
        """
        try:
            if isinstance(eval(value), str):
                return value
            if isinstance(eval(value), dict):
                result = eval(json.dumps(value))
                return result
        except BaseException as e:
            self.logger.error("change_type 转换错误:{0}".format(e))

    def get(self, uri, params,headers):
        """
        Get请求方法
        :return:
        """
        # 拼装接口请求地址
        url = self.url + uri
        # headers = {'Content-Type': "application/x-www-form-urlencoded"}
        try:
            response = requests.get(url, headers=headers, params=params)
            # self.log.info("GET 请求成功，返回体内容：{0} ".format(response))
            # self.log.info("GET 请求成功，返回体data：{0} ".format(response.content))
            return response
        except TimeoutError:
            self.logger.error("请求超时失败!")

    def post(self, uri, data,headers):
        """
        Post 请求方法
        """
        # headers = {'Content-Type': "application/x-www-form-urlencoded"}
        # 拼装接口请求地址
        url = self.url + uri
        try:
            response = requests.post(url, headers=headers, data=data,
                                     timeout=float(self.timeout))
            self.logger.info("POST 请求成功，返回体内容：{0} ".format(response))
            self.logger.info("POST 请求成功，返回体data：{0} ".format(response.content))
            return response
        except TimeoutError:
            self.logger.error("请求超时失败!")
            return None

    def post_with_json(self, uri, data,headers):
        """
        Post 请求，数据体为 json
        :return:
        """
        # headers = {'Content-Type': 'application/json'}
        # 拼装接口请求地址
        url = self.url + uri
        try:
            response = requests.post(url=url, headers=headers, json=data, timeout=float(self.timeout))
            self.logger.info("POST 请求发送Json成功，返回体：{0} ".format(response))
            self.logger.info("POST 请求发送Json成功，返回体data：{0} ".format(response.content))
            return response
        except TimeoutError:
            self.logger.error("请求超时失败!")
            return None
