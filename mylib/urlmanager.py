import requests

class urlManager:
    def __init__(self):
        self.newUrls=set()
        self.oldUrls=set()
        self.nextUrls=set()
        self.oldNextUrls=set()

    def addUrl(self,url):
        if not url:
            return
        if url in self.oldUrls:
            return
        self.newUrls.add(url)

    def addNextUrl(self,url):
        if not url:
            return
        if url in self.oldNextUrls:
            return
        self.nextUrls.add(url)

    def addUrls(self,urls):
        if not urls:
            return
        for url in urls:
            self.addUrl(url)

    def hasNewUrl(self):
        return len(self.newUrls)!=0

    def getUrl(self):
        if len(self.newUrls)!=0:
            
            if len(self.newUrls)<10 and len(self.nextUrls)!=0:
                url=self.newUrls.pop()
                self.oldNextUrls.add(url)
            else:
                url=self.newUrls.pop()
                self.oldUrls.add(url)
            return url