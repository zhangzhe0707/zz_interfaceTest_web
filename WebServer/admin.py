from django.contrib import admin
from .models import TestCase, TestResults, EnvConfig, TestResultsDetail

# Register your models here.
admin.site.site_header = "接口测试管理系统"
admin.site.site_title = "InterFaceTest"


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Name', 'Label', 'RequestData', 'ApiPath', 'RequestMethod',
                    'ReponseCheckPoint',
                    'HttpCodeCheck']


class EnvConfigAdmin(admin.ModelAdmin):
    list_display = ['Id', 'EnvName', 'EnvBaseUrl', 'EnvTimeout', 'DatabaseHost',
                    'Database_Database']


admin.site.register(EnvConfig, EnvConfigAdmin)
admin.site.register(TestCase, TestCaseAdmin)

# class TestResultsAdmin(admin.ModelAdmin):
#     list_display = ['Id', 'Name', 'Result', 'Create_Time']


# class TestResultsDetailAdmin(admin.ModelAdmin):
#     list_display = ['Id', 'TestCase', 'Result', 'Expected_Return_Result', 'Actual_Return_Result', 'Create_Time']
##
# ]
# admin.site.register(TestResultsDetail, TestResultsDetailAdmin)
# admin.site.register(TestResults, TestResultsAdmin)
