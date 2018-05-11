import requests

class download:
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
        self.proxie={}
    def download(self,url,ip):
        try:
            
            content=requests.get(url,headers=self.headers,proxies={'http':'http://'+ip[1]+':'+ip[2]})
            if content.status_code==200:
                text=content.content.decode('utf-8')
                return text
        except Exception as e:
            raise e

    # 设置代理
    def setProxie(self,proxie):
        self.proxie=proxie