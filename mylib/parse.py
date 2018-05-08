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
        title=self.parseTitle(content)
        productId=self.parseId(content)
        storeName=self.parseStoreName(content)
        storeLink=self.parseStoreLink(content)
        imgList=self.parseImg(content)
        bigImg=self.parseBigImg(content)
        price=self.parsePrice(content)
        attr=self.parseAttr(content)
        description=self.parseDescription(content)
        location=self.parseLocation(content)
        ship=self.parseShip(content)
        return (imgList,bigImg,title,price,attr,description,ship)

    def parseNextUrl(self,content):
        reStr=re.compile(r'class="pagn-next".+?href="(.*?)"')
        return re.findall(reStr,content)[0]