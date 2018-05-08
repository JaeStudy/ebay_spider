import pyquery
import re
class parse():
    def parse(self,content):
        newUrls=self.parseUrl(content)
        newData=self.parseData(content)
        nextUrl=self.parseNextUrl(content)
        return newUrls,newData,nextUrl

    def parseUrl(self,content):
        reStr=re.compile(r'class="lvtitle".+?href="(.*?)"')
        return re.findall(reStr,content)

    def parseData(self,content):
        return None

    def parseNextUrl(self,content):
        reStr=re.compile(r'class="pagn-next".+?href="(.*?)"')
        return re.findall(reStr,content)[0]