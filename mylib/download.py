import requests
import chardet

class download:
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 '}
    def download(self,url):
        try:
            
            content=requests.get(url,headers=self.headers)
            if content.status_code==200:
                text=content.content.decode(chardet.detect(content.content)['encoding'])
                return text
        except Exception as e:
            raise e