import pymysql
class intoDb():
    def __init__(self):
        pass
    def collect(self,data):
        sql='insert into ebay (title,productId,storeName,storeLink,imgList,price,attr,description,location,ship) values('
        for k in data:
            s=self.changeStr(data[k])
            sql+="'%s',"%s
        sql=sql[0:-1]
        sql+=')'
        # print(sql)
        conn=pymysql.connect('127.0.0.1','root','123','py')
        cursor=conn.cursor()
        try:
            cursor.execute(sql)
            print('insert ok')
        except Exception as e:
            conn.rollback()
            raise 'insert no'
        conn.commit()
        cursor.close()
        conn.close()

    # 转义字符串的\ ' "等
    def changeStr(self,cStr):
        if len(cStr)==0:
            return
        retStr=''
        for c in cStr:
            if c =='"':
                c='\\\"'
            if c =="'":
                c="\\\'"
            if c=='\\':
                c='\\\\'
            retStr+=c
        return retStr

        