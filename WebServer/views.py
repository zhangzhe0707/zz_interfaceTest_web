from django.shortcuts import render

import logging
import os
import json
from datetime import datetime
from jsondiff import diff
from ZZ_InterfaceTest_web.settings import RESPORTS_DIR_PATH
from WebServer.models import TestCase
from lib.baseCode import BaseCode
from lib.baseHttp import BaseHttp

logger = logging.getLogger()


# Create your views here.
def runTestCase(request, envName, caseName):
    basecode = BaseCode()

    test_results_name = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    if not os.path.exists(RESPORTS_DIR_PATH):
        os.mkdir(RESPORTS_DIR_PATH)
    log_path = os.path.join(RESPORTS_DIR_PATH, test_results_name)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    case_data = TestCase.objects.filter(Name=caseName)
    logger.info("开始执行测试用例")
    baseHttp = BaseHttp(envName)
    for case in case_data:
        print(case)

    for case in case_data:
        # 发送接口请求
        if case.RequestMethod == 'post':
            response = baseHttp.post(case.ApiPath, basecode.body_decode(case.RequestData))
            logger.info('接口返回结果%s' % response)
        elif case.RequestMethod == 'get':
            response = baseHttp.get(case.ApiPath, basecode.body_decode(case.RequestData))
            logger.info('接口返回结果%s' % response)
        elif case.RequestMethod == "post_with_json":
            response = baseHttp.post_with_json(case.ApiPath, basecode.body_decode(case.RequestData))
            logger.info('接口返回结果%s' % response)
        else:
            logger.info("未找到正确的 Method 类型")
        # 返回结果验证
        response_data = json.loads(response.content)
        response_status_code = response.status_code
        if case.ReponseCheckType == 'FM':
            diff(response_data,json.loads(case.ReponseCheckPoint))
        # elif case.ReponseCheckPoint is 'PM':
        #     for response
    #
    # TestResults.objects.create(Name=test_results_name)

    # send_mail(os.path.join(log_path, 'report.html'))
    # logger.info(output.read())

    return render(request, 'run.html')
