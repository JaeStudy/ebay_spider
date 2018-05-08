from mylib import urlmanager,download,parse,intodb
class spider():
    def __init__(self):
        self.urlManager=urlmanager.urlManager()
        self.download=download.download()
        self.parse=parse.parse()
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
            except Exception as e:
                print(e)
                pass
            break

root_url='https://www.ebay.com/sch/ATV-Parts/43962/i.html?_fsrp=1%3F_fsrp%3D1&_pgn=2&_skc=25'
spider=spider()
spider.main(root_url)