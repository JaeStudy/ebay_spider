from mylib import urlmanager,download,parse,intodb
class spider:
    def __init__(self):
        self.urlManager=urlmanager.urlManager()
        self.download=download.download()
        self.parse=parse.parse(self.download)
        self.intoDb=intodb.intoDb()

    # 爬虫调度程序
    def main(self,root_url):
        self.urlManager.addUrl(root_url)
        while self.urlManager.hasNewUrl():
            try:
                newUrl=self.urlManager.getUrl()
                content=self.download.download(newUrl)
                newUrls,newData,nextUrl=self.parse.parse(content)
                self.urlManager.addUrls(newUrls)
                self.urlManager.addNextUrl(nextUrl)
                self.intoDb.collect(newData)
                print('success')
            except Exception as e:
                print('nonono')
                print(e)
                
            break

root_url='https://www.ebay.com/itm/Yamaha-Grizzly-660-700-Wheel-Bearing-Greaser-fits-OEM-AB25-1496-bearings/282952351312?hash=item41e1463e50:g:ULIAAOSwmfhX2ygV&vxp=mtr'
spider=spider()
spider.main(root_url)