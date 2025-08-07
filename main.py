import requests
import json
import urllib.parse
import os

# API配置
LOGIN_URL = "https://starapi.qxzhi.cn/SProUsers/userLogin"
QIANDAO_URL = "https://starht.qxzhi.cn/Plugins/sy_starpro/api.php?act=qiandao&uid={}"

# 请求头配置
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# 从环境变量获取登录数据
login_data = {
    "name": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD")
}

def main():
    # 准备登录请求数据
    json_string = json.dumps(login_data, separators=(',', ':'))
    encoded_data = urllib.parse.quote(json_string)
    data_string = f"params={encoded_data}"

    # 发送登录请求
    response = requests.post(LOGIN_URL, headers=headers, data=data_string)

    # 处理登录响应
    try:
        login_result = response.json()
        
        if response.status_code == 200 and login_result.get('code') == 1:
            # 提取用户信息
            token = login_result['data']['token']
            screen_name = login_result['data']['screenName']
            uid = login_result['data']['uid']
            
            # 显示用户信息
            print(f"NAME: {screen_name}")
            print(f"UID:  {uid}")
            
            # 执行签到
            perform_qiandao(token)
            
        else:
            print("登录失败，无法获取token")
            
    except Exception as e:
        print(f"登录响应解析失败: {e}")

def perform_qiandao(token):
    """执行签到功能"""
    try:
        # 构建签到URL并发送请求
        qiandao_url = QIANDAO_URL.format(token)
        qiandao_response = requests.get(qiandao_url)
        
        # 解析签到响应
        qiandao_result = qiandao_response.json()
        print(f"MSG:  {qiandao_result['msg']}")
        
    except Exception as e:
        print(f"签到失败: {e}")

if __name__ == "__main__":
    main()

