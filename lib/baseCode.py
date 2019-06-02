#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author: zz

@License: (C) Copyright 2013-2017, 

@Contact: zhangzhe0707@gmail.com

@Software: PyCharm

@File: baseCode.py

@Time: 2019-05-08 00:57

@Desc:

'''
import os
import json
import logging
import operationConfig as Config
from lib.baseDB import BaseDB


class BaseCode:

    def __init__(self):
        self.LOCAL_READ_CONFIG = Config.OperationConfig()
        self.PRO_DIR = Config.PROJECT_DIR
        self.logger = logging.getLogger()
        self.ENV_NAME = self.LOCAL_READ_CONFIG.get_env('env_name')

    def show_retrun_msg(self, response):
        '''
        输出response中 msg 信息
        :param response:
        :return:
        '''
        url = response.url
        msg = response.text

        self.logger.info('请求地址:{0}'.format(url))
        self.logger.info('请求返回值:{0}'.format(json.dumps(json.loads(msg),
                                                       ensure_ascii=False, sort_keys=True, indent=4)))

    def get_env_data(self):
        db = BaseDB()
        env_data = {}

        if self.ENV_NAME:
            db_data = db.get_one_data(
                'Select Id,EnvName,EnvBaseUrl,EnvScheme,EnvPort,EnvTimeout from '
                'WebServer_envconfig where EnvName="{0}"'.format(
                    self.ENV_NAME))
        else:
            self.logger.error('测试环境名称不能为空！')

        if db_data:
            env_name = db_data[self.LOCAL_READ_CONFIG.get_db_index('env_name')]
            env_base_url = db_data[self.LOCAL_READ_CONFIG.get_db_index('env_base_url')]
            env_scheme = db_data[self.LOCAL_READ_CONFIG.get_db_index('env_scheme')]
            env_port = db_data[self.LOCAL_READ_CONFIG.get_db_index('env_port')]
            env_timeout = db_data[self.LOCAL_READ_CONFIG.get_db_index('env_timeout')]

            env_data = {'envName': env_name, 'envBaseUrl': env_base_url,
                        'envScheme': env_scheme,
                        'envPort': env_port,
                        'envTimeout': env_timeout}
            self.logger.info('测试环境数据{0}完成读取.'.format(env_name))
        else:
            self.logger.error('未查询匹配的测试环境数据')
            return '未查询匹配的测试环境数据'
        return env_data

    def get_case_data(self, name=None, label=None):
        '''
        从数据库中读取测试数据
        :param
            envName:测试环境名称
            name:测试用例名称
            label:测试用例标签名称
        :return:
            case_data：测试数据集列表
        '''

        db = BaseDB()
        case_data = []

        if name is None and label is None:
            db_data = db.get_all_data('Select * from WebServer_testcase')
        elif name is not None:
            db_data = db.get_all_data('Select * from WebServer_testcase where Name={0}'.format(name))
        elif label is not None:
            db_data = db.get_all_data('Select * from WebServer_testcase where Label={0}'.format(label))

        if db_data:
            self.logger.info('测试用例{0}完成测试数据读取.'.format(db_data))
            for db_itme in db_data:
                no = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_no')]
                name = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_name')]
                label = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_label')]
                front_sql = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_front_sql')]
                api_path = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_api_path')]
                method = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_method')]
                request_data = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_request_data')]
                response_check_type = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_response_check_type')]
                response_check_point = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_response_check_point')]
                http_code_check = db_itme[self.LOCAL_READ_CONFIG.get_db_index('case_http_code_check')]

                case_dict = {'caseNo': no, 'caseName': name, 'caseLabel': label, 'caseFrontSQL': front_sql,
                             'caseUri': api_path,
                             'caseData': request_data, 'caseMethod': method,
                             'caseResponseCheckType': response_check_type,
                             'caseResponseCheckPoint': response_check_point,
                             'caseStatusCode': http_code_check}
                case_data.append(case_dict)
                self.logger.info('测试用例{0}完成测试数据读取.'.format(db_data))
        else:
            self.logger.error('未查询匹配的测试数据')
            return '未查询匹配的测试数据'

        return case_data


if __name__ == "__main__":
    dc = BaseCode()
    print(dc.get_case_data())
