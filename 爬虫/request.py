import requests

# 目标URL
url = 'https://pan.baidu.com/s/17tYxXTL7pGJFrG1LYiQm9Q'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    print('请求成功！')
    # 打印响应内容
    print(response.text)
else:
    print('请求失败，状态码：', response.status_code)

















