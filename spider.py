from mylib import urlmanager,download,parse,intodb,ips
import time
import threading
class spider:
    def __init__(self):
        self.urlManager=urlmanager.urlManager()
        self.download=download.download()
        self.parse=parse.parse(self.download)
        self.intoDb=intodb.intoDb()
        self.ips=ips.ips()

    # 爬虫调度程序
    def main(self,root_url):
        self.urlManager.addUrl(root_url)
        count=1
        ipList=self.ips.getIps()
        while self.urlManager.hasNewUrl():
            try:
                ip=ipList[count-1]
                self.ips.setLastTime(ip[0])
                newUrl=self.urlManager.getUrl()
                # 线程数量控制在10个以下
                th=threading.active_count()
                if th>10:
                    time.sleep(1)
                    continue
                # 代理ip
                proxie={
                'http':'http://111.121.193.214:3218'
                }
                # 设置代理ip
                self.download.setProxie(proxie)
                # 多线程
                threading.Thread(target=self.theadAction,args=(newUrl,count,ip)).start()
                
            except Exception as e:
                print('nonono')
                print(e)
            
            count +=1
            time.sleep(10)
            # 网址管理器没有网址时，并且运行线程不为0，休眠10秒等待线程可能取出地址
            if not self.urlManager.hasNewUrl() and threading.active_count()!=0:
                time.sleep(10)
            break
            

    def theadAction(self,newUrl,count,ip):
        content=self.download.download(newUrl,ip)
        newUrls,newData,nextUrl=self.parse.parse(content)
        self.urlManager.addUrls(newUrls)
        self.urlManager.addNextUrl(nextUrl)
        self.intoDb.collect(newData,newUrl)
        print('%s success'%count)

root_url='https://www.ebay.com/sch/Brakes-Suspension-/178919/i.html?_fsrp=1'
spider=spider()
spider.main(root_url)