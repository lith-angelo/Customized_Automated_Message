import requests
import json
from twilio.rest import Client
import time

account_sid = "AC360aff664a181761414840b4f1754324"
auth_token = "b336fc6efc02ee7a5d377f2aa3eab818"
url = 'http://api.tianapi.com/txapi/wanan/index?key=4a611d178bf4a853f0e6c754efdb8fe3'

page = requests.get(url=url)
content = json.loads(page.text)['newslist'][0]['content']
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8618827189301",
    from_="+12566079294",
    body=str(content))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(message.sid)
print(message.status)


