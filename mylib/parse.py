from pyquery import PyQuery as pq
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
        # bigImg=imgList[0]
        price=self.parsePrice(content)
        attr=self.parseAttr(content)
        description=self.parseDescription(content)
        location=self.parseLocation(content)
        ship=self.parseShip(content)
        return (imgList,bigImg,title,price,attr,description,ship)

    def parseNextUrl(self,content):
        reStr=re.compile(r'class="pagn-next".+?href="(.*?)"')
        return re.findall(reStr,content)[0]

    def parseTitle(self,content):
        html=pq(content)
        return html('.it-ttl').remove('span').text()

    def parseId(self,content):
        html=pq(content)
        return html('#descItemNumber').text()

    def parseStoreName(self,content):
        html=pq(content)
        return html('#mbgLink').text()

    def parseStoreLink(self,content):
        html=pq(content)
        return html('#mbgLink').attr('href')

    def parseImg(self,content):
        html=pq(content)
        imgs=set()
        img=html('.tdThumb').find('img')
        for i in range(len(img)):
            src=img.eq(i).attr('src').replace('s-l64.jpg','s-l640.jpg')
            imgs.add(src)
        return imgs

    def parsePrice(self,content):
        html=pq(content)
        return html('.notranslate').text()

    def parseAttr(self,content):
        html=pq(content)
        return html('.itemAttr').text()

    def parseDescription(self,content):
        html=pq(content)
        if html('#desc_ifr').text() =='':
            print(1)
        else:
            print(22)  
