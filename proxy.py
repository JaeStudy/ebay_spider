import requests
from pyquery import PyQuery as pq
import re
import telnetlib
import time
import pymysql
import threading

# 代理ip池
class proxy:
    def __init__(self):
        self.webUrl='http://www.gatherproxy.com/proxylist/country/?c=China'
        self.data={'Country':'china','PageIdx':1}
        self.headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36","Referer":'http://www.gatherproxy.com/proxylistbycountry',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':'_lang=en-US; _ga=GA1.2.2144581557.1525937424; _gid=GA1.2.1441561688.1525937424; ASP.NET_SessionId=1mksikfjuujfgipij3ydayjy',
        'Host':'www.gatherproxy.com',
        'Proxy-Connection':'keep-alive'
        }
        self.proxie={
                'http':'http://61.145.194.26:8080'
                }
        self.ip='50.233.137.37'
        self.port='80'
    # 爬取代理ip
    def spider(self):
        for i in range(37):
            i+=1
            self.data['PageIdx']=i
            print(i)
            html=requests.post(self.webUrl,json=self.data,headers=self.headers)
            reStr=re.compile(r'<tr>.*?<td><script>document.write\(\'(.*?)\'\).+?gp.dep\(\'(.*?)\'\)',re.S)
            ipList=re.findall(reStr,html.text)
            self.intodb(ipList)
    def checkIp(self,ip,port):
        try:
            telnetlib.Telnet(ip, port=port, timeout=10)
        except:
            print('ok')
            return True
        else:
            print('fail')
            return False
    # 检查ip是否可用
    def check(self):
        conn=pymysql.connect('127.0.0.1','root','123','pytest')
        cursor=conn.cursor()
        sql='select * from ip'
        cursor.execute(sql)
        ipList=cursor.fetchall()
        self.ids=set()
        for ip in ipList:
            threading.Thread(target=self.threadIp,args=(ip,)).start()
        while threading.active_count()>1:
            print(threading.active_count())
            time.sleep(1)
        sql='update ip set used=1 where id in (%s)'%str(self.ids)[1:-1]
        cursor.execute(sql)
        conn.commit()
        
    # ip线程
    def threadIp(self,ip):
        if self.checkIp(ip[1],ip[2]):
            print(ip[0])
            self.ids.add(ip[0])

    def intodb(self,list):
        if not list:
            return
        sql='insert into iptmp (ip,port,time) values'
        for i in list:
            port=self.toTen(i[1])
            ctime=time.strftime('%Y-%m-%d',time.localtime())
            sql+='("%s","%s","%s"),'%(i[0],port,ctime)
        conn=pymysql.connect('127.0.0.1','root','123','pytest')
        cursor=conn.cursor()
        sql=sql[0:-1]
        try:
            self.setIpTmp(cursor)
            cursor.execute(sql)
            self.ipTmpToIp(cursor)
            conn.commit()
            print('insert db ok')
        except Exception as e:
            conn.rollback()
            print(e)
        cursor.close()
        conn.close()

    # 新建非正常临时表iptmp
    def setIpTmp(self,cursor):
        dropSql='drop TABLE if exists iptmp'
        cursor.execute(dropSql)
        createSql="CREATE  TABLE `iptmp` (`id` int(11) NOT NULL,`ip` varchar(100) NOT NULL,`port` varchar(20) NOT NULL,`time` date NOT NULL) ENGINE=Myisam DEFAULT CHARSET=utf8"
        cursor.execute(createSql)

    # 将不重复的ip记录存进ip表
    def ipTmpToIp(self,cursor):
        sql='insert into ip (ip,port,time) select ip,port,time from iptmp where id not in (select iptmp.id from ip ,iptmp where ip.ip=iptmp.ip)'
        cursor.execute(sql)
        dropSql='drop TABLE if exists iptmp'
        cursor.execute(dropSql)

    # 十六进制转十进制
    def toTen(self,info):
        return int(info, 16)


obj=proxy()
# obj.checkIp()
# obj.spider()
obj.check()
