import requests
import re

url = "https://xui.ptlogin2.qq.com/cgi-bin/xlogin"
querystring = {"appid":"715030901","daid":"73","hide_close_icon":"1","pt_no_auth":"1","s_url":"https://qun.qq.com/member.html"}
payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "7fab37a5-bf12-4c08-b952-030c828135bb"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
cookies = str(response.cookies)
#print(cookies)
ret = re.findall(r"Cookie pt_local_token=(.*?) for",cookies)
pt_local_token = ret[0]
#print(pt_local_token)

url = "https://localhost.ptlogin2.qq.com:4301/pt_get_uins"
querystring = {"callback":"ptui_getuins_CB","r":"0.0760575656488639","pt_local_tk":pt_local_token}
cookie = "pt_local_token=" + pt_local_token
payload = ""
headers = {
    'Referer': "https://xui.ptlogin2.qq.com",
    'Cookie': cookie,
    'cache-control': "no-cache",
    'Postman-Token': "90c27990-deed-4283-a909-f097e63a4e78"
    }
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
body = response.text
qquin = re.findall(r'"uin":(.*?),"face_index',body)
#print (qquin)
for test in qquin:
    url = "https://localhost.ptlogin2.qq.com:4301/pt_get_st"

    querystring = {"clientuin":test,"callback":"ptui_getst_CB","r":"0.7284667321181328","pt_local_tk":pt_local_token}

    payload = ""
    headers = {
        'Referer': "https://xui.ptlogin2.qq.com",
        'Cookie': cookie,
        'cache-control': "no-cache",
        'Postman-Token': "e8292a8c-a09a-4f27-ac23-b945c92b5894"
        }
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    ret =  str(response.cookies)
    QQclientkey = re.findall(r'Cookie clientkey=(.*?) for .ptlogin2.qq.com' ,ret)
    QQnum = re.findall(r'<Cookie clientuin=(.*?) for .ptlogin2.qq.com/>' ,ret)
    i = 0
    result = QQnum[i] + ": " + QQclientkey[i]
    i = i+1
    print(result)
