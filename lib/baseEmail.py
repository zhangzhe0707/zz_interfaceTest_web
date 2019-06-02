#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author: zz

@License: (C) Copyright 2013-2017, 

@Contact: zhangzhe0707@gmail.com

@Software: PyCharm

@File: baseEmail.py

@Time: 2019-05-18 23:25

@Desc:

'''

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import operationConfig
import time

local_read_config = operationConfig.OperationConfig()


def send_mail(result_path):
    # 添加邮件发送信息及标题:
    msg = MIMEMultipart()
    msg['From'] = local_read_config.get_mail('from_addr')
    msg['To'] = str(local_read_config.get_mail('to_addr'))
    msg['Subject'] = Header(u'测试的请求', 'utf-8').encode()
    # 添加邮件正文
    msg.attach(MIMEText('接口自动化测试执行完成！测试结果详见附件', 'plain', 'utf-8'))
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    # 添加附件
    with open(result_path, 'rb') as f:
        mime = MIMEBase('image', 'png', filename=now + 'result.html')
        mime.add_header('Content-Disposition', 'attachment', filename=now + 'result.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        html_load = f.read()
        msg.attach(MIMEText(html_load, 'html', 'utf-8'))
        mime.set_payload(html_load)
        encoders.encode_base64(mime)
        msg.attach(mime)

    # 进行发送操作
    # 连接 SMTP 服务器
    try:
        server = smtplib.SMTP(local_read_config.get_mail('smtp_server'), 25)
        server.set_debuglevel(1)
        # 登录账号
        server.login(local_read_config.get_mail('from_addr'), local_read_config.get_mail('password'))
        # 发送邮件
        server.sendmail(local_read_config.get_mail('from_addr'),
                        str(local_read_config.get_mail('to_addr'), msg.as_string()))
        server.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('邮件发送失败')
