import requests
import chardet

class download():
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    def download(self,url):
        try:
            
            content=requests.get(url,headers=self.headers)
            if content.status_code==200:
                text=content.content.decode(chardet.detect(content.content)['encoding'])
                return text
        except Exception as e:
            raise e