# Customized_Automated_Message
For sending messages automatically.

### 功能 ###
向指定的手机号码发送问候短信

### 使用方法 ###
* 在[twilio](https://www.twilio.com)注册账号，获得account_sid与auth_token。然后在[控制台](https://www.twilio.com/console/)获取手机号。
* 在[天行](https://www.tianapi.com)注册账号，然后在[短信功能](https://www.tianapi.com/apiview/142)获取key，以获得问候内容。
* 设置发送号码为第一步中获取的手机号，接收方为第一步中注册账号时的手机号，设置account_sid、auth_token、key。（若要指定接收信息的手机号，需先在第一步的控制台中验证该手机号）
* 运行，检查是否收到短信。

### 注意事项 ###
1. 需安装twilio库，可使用pip安装。
2. 可在自己的服务器上添加定时任务，达到定时发送短信的效果。
3. 信息内容不局限于问候，可自主选择内容接口。
