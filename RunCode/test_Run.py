import pytest
import json
from jsondiff import diff
from lib.baseCode import BaseCode
from lib.baseHttp import BaseHttp
import lib.log as Loglib

import operationConfig

local_read_config = operationConfig.OperationConfig()
reportPath = operationConfig.RESPORTS_DIR_PATH
base_code = BaseCode()
Log = Loglib.Log()


@pytest.mark.parametrize('case_data', base_code.get_case_data())
def test_all_run(case_data):
    base_http = BaseHttp()
    response = None
    Log.logger.info(case_data['caseName'])
    if case_data['caseMethod'] == 'post':
        response = base_http.post(case_data['caseUri'], case_data['caseData'])
    elif case_data['caseMethod'] == 'get':
        response = base_http.get(case_data['caseUri'], case_data['caseData'])
    elif case_data['caseMethod'] == "post_with_json":
        response = base_http.post_with_json(case_data["caseUri"], case_data["caseData"])
    else:
        Log.logger.info("未找到正确的 Method 类型")

    # 日志记录返回体内容
    base_code.show_retrun_msg(response)

    # # 验证返回 http code
    assert int(case_data["caseStatusCode"]) == response.status_code
    #


    # 验证response
    response_data = json.loads(response.text)
    if case_data['caseResponseCheckType'] == 'FM':#全量校验
        fm_response_check_point = json.loads(case_data["caseResponseCheckPoint"])
        assert diff(response_data, fm_response_check_point) == {}
    elif case_data['caseResponseCheckType'] == 'PM':#部分校验
        pm_response_check_point = json.loads(case_data["caseResponseCheckPoint"])
        # diff函数判断 check_itme 是否被response_data包含，如果包含response_data-check_itme的内容，
        # 如果不包含或不一致返回，response_data原内容
        check_Result = diff(pm_response_check_point, response_data)

        assert check_Result != response_data

    Log.add_end_line(case_data["caseName"])

