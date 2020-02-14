import requests
import json
import time
from twilio.rest import Client

account_sid = Your account_sid  # account_sid=aaaaaaaaaaaaaaaa
auth_token = Your auth_token    # auth_token=aaaaaaaaaaaaaa
url = 'http://api.tianapi.com/txapi/wanan/index?key=Your key'   # key=aaaaaaaaaaaaaaa

#获取信息内容
page = requests.get(url=url)
content = json.loads(page.text)['newslist'][0]['content']

#发送信息
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="Your phone number", # to="+86123456"
    from_="server number",  #from_="+12123456"
    body=str(content))

# 输出日志
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(content)
print(message.sid)


