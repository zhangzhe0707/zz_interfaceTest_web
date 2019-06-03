from django.db import models


# Create your models here.

class EnvConfig(models.Model):
    Id = models.AutoField(primary_key=True)
    EnvName = models.CharField(max_length=50, blank=False, verbose_name='测试环境名称')
    EnvBaseUrl = models.CharField(max_length=50, blank=False, verbose_name='被测服务基础Url')
    EnvScheme = models.CharField(max_length=50, blank=False, verbose_name='被测服务协议')
    EnvPort = models.CharField(max_length=8, blank=True, verbose_name='被测服务端口号')
    EnvTimeout = models.CharField(max_length=4, blank=False, verbose_name='请求超时时间')
    DatabaseHost = models.CharField(max_length=50, blank=False, verbose_name='数据库服务器地址')
    Database_Username = models.CharField(max_length=50, blank=False, verbose_name='数据库用户名')
    Database_Password = models.CharField(max_length=50, blank=False, verbose_name='数据库密码')
    Database_Port = models.CharField(max_length=50, blank=False, verbose_name='数据库端口号')
    Database_Database = models.CharField(max_length=50, blank=False, verbose_name='数据库名称')
    Create_Time = models.DateTimeField(auto_now=True, verbose_name='创建时间（自动获取当前时间）')

    class Meta:
        verbose_name = "环境配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.EnvName


class TestCase(models.Model):
    CHECK_TYPE=(
        ('FM', '全量匹配'),
        ('PM', '部分匹配'),)
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, blank=False, verbose_name='测试用例名称')
    Label = models.CharField(max_length=200, blank=True, verbose_name='测试用例标签')
    FrontSQL = models.CharField(max_length=200, blank=True, verbose_name='前置数据命令')
    ApiPath = models.CharField(max_length=200, blank=False, verbose_name='接口路径')
    Headers = models.CharField(max_length=200, blank=False, verbose_name='接口头信息')
    RequestMethod = models.CharField(max_length=200, blank=False, verbose_name='请求方法')
    RequestData = models.TextField(max_length=50000, blank=False, verbose_name='接口请求体')
    ReponseCheckType = models.CharField(max_length=2, choices=CHECK_TYPE,verbose_name='验证机制')
    ReponseCheckPoint = models.TextField(max_length=2000, blank=False, verbose_name='响应体检查点')
    HttpCodeCheck = models.CharField(max_length=200, blank=False, verbose_name='HTTPCode检查点')
    Create_Time = models.DateTimeField(auto_now=True, verbose_name='创建时间（自动获取当前时间）')

    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name


class TestResultsDetail(models.Model):
    Id = models.AutoField(primary_key=True)
    TestCase = models.CharField(max_length=200, blank=False, verbose_name='测试用例名称')
    Result = models.CharField(max_length=200, blank=False, verbose_name='测试结果')
    Expected_Return_Result = models.CharField(max_length=1000, blank=False, verbose_name='预计返回结果')
    Actual_Return_Result = models.CharField(max_length=1000, blank=False, verbose_name='实际返回结果')
    Create_Time = models.DateTimeField(auto_now=True, verbose_name='创建时间（自动获取当前时间）')

    class Meta:
        verbose_name = "测试结果明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Id


class TestResults(models.Model):
    Id = models.AutoField(primary_key=True)
    TestResultsDetail = models.ForeignKey(TestResultsDetail, on_delete=True)
    Name = models.CharField(max_length=50, blank=False, verbose_name='测试结果名称')
    Result = models.CharField(max_length=200, blank=False, verbose_name='测试结果')
    Create_Time = models.DateTimeField(auto_now=True, verbose_name='创建时间（自动获取当前时间）')

    class Meta:
        verbose_name = "测试结果"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name

class BaseConfig(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, verbose_name='系统配置名称')

    class Meta:
        verbose_name = "系统配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
