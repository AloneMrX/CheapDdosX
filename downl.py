import requests

f = open('proxy.txt','wb')
http_api = [
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
]
for api in http_api:
    try:
        r = requests.get(api,timeout=5)
        f.write(r.content)
    except:
        pass
f.close()
