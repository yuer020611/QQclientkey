import requests
import re
s = requests.Session()
s.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=636014201&s_url=http%3A%2F%2Fwww.qq.com%2Fqq2012%2FloginSuccess.htm&style=20&border_radius=1&target=self&maskOpacity=40")

pt_local_tk = s.cookies.get_dict()['pt_local_token']

url = "https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&pt_local_tk=" + pt_local_tk

head = {'Referer':'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=636014201&s_url=http%3A%2F%2Fwww.qq.com%2Fqq2012%2FloginSuccess.htm'}

r = s.get(url , headers=head )

uin = re.findall(r'account":"(.*?)","',r.text)

clientkey={}

for each_uin in uin :
    url = "https://localhost.ptlogin2.qq.com:4301/pt_get_st?clientuin=" + each_uin + "&callback=ptui_getst_CB&pt_local_tk=" + pt_local_tk
    s.get(url,headers=head)
    clientkey[each_uin]=s.cookies.get_dict()['clientkey']
    
for each in clientkey.keys():
    result =  each +":"+ clientkey[each];
    print(result);
input()
