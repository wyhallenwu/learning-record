# -*- coding:utf-8 -*-
import requests
import sys
import time
import json

# your student id and passwd
username = "***"  # input id here
password = "***"  # input passwd here
# turn to baidu page
BAIDU = "http://www.baidu.com"
valid_code = False

re = requests.session()

if __name__ == '__main__':
    try:
        # 获取登录用的参数，系统会校验格式，但不校验有效性
        parameters = re.get(BAIDU, timeout=5).text
        # 判断是否进入登录界面（有拦截地址）
        serach_index = parameters.find(".jsp?")
        if serach_index == -1:
            print("Alrearedy Login!")
            sys.exit(0)

        # 从 302 跳转 URL 中把需要的参数掐头去尾取出来
        queryString = parameters[serach_index + 5:-12]

        # 获取验证码
        payload = {
            'queryString': queryString
        }
        response = re.post("http://10.10.9.9:8080/eportal/InterFace.do?method=pageInfo", data=payload)
        validCodeUrl = json.loads(response.text)['validCodeUrl']
        if validCodeUrl != '':
            valid_code = True
            html = re.get('http://10.10.9.9:8080' + validCodeUrl)
            with open('./code.jpg', 'wb') as file:
                file.write(html.content)

    except requests.exceptions.RequestException:
        print("Timeout or other network ererror!")
        sys.exit(-1)

    # 请求登录地址
    login_url = "http://10.10.9.9:8080/eportal/InterFace.do?method=login"
    if valid_code:
        code = input("Please input the code in this directory named code.jpg: ")
    else:
        code = ''
    # 参数体
    print(queryString)
    payload = {
        'userId': username,
        'password': password,
        'service': 'shu',
        'queryString': queryString,
        'operatorPwd': '',
        'operatorUserId': '',
        'vaildcode': code
        # 'passwordEncrypt': 'true'
    }
    # 发送 POST 请求，提交登录表单
    response = re.post(login_url, data=payload)
    print(response.text)
    # 结果判断
    if response.text.find("success") >= 0:
        print("login success!")
        sys.exit(0)
    else:
        print("login failure!")
        sys.exit(-1)
