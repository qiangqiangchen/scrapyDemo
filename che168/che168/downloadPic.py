# -*- coding: utf-8 -*-
import MySQLdb
import os
from multi_download import Multi_DownLoad

class DBHelper(object):
    def __init__(self,host,port,user,passwd,db):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
    def connectMysql(self):
        conn=MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,charset='utf8')
        return conn
    def connectDatabase(self):
        conn=MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset='utf8')
        return conn
    def insert(self,sql):
        conn=self.connectDatabase()
        cur=conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except:
            print 'Error:unable to insert data,sql is : %s'%sql
            conn.rollback()
        finally:
            cur.close()
            conn.close()
    def select(self,sql):
        conn=self.connectDatabase()
        cur=conn.cursor()
        try:
            cur.execute(sql)
            data=cur.fetchall()
            return data
        except:
            print 'Error:unable to fecth data'
            return None
        finally:
            cur.close()
            conn.close()
            
            
    def update(self,sql):
        conn=self.connectDatabase()
        cur=conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return True
        except:
            print 'Error:unable update data'
            conn.rollback()
            return False
        finally:
            cur.close()
            conn.close()
            
db=DBHelper("127.0.0.1",3306,"root","root","porn")

#获取需要下载的数据
def getDownData():
    sql="SELECT id,car_title,car_image FROM che WHERE is_down=0;"
    sql2="SELECT zipai_title,zipai_imgs FROM pornlist;"
    data=db.select(sql2.encode('utf-8'))
    return data
#更新数据库，已经下载的标记为下载
def updateData(id):
    sql="UPDATE che SET is_down=1 WHERE id=%s;"%id
    return db.update(sql)
#下载图片
def downpic():
    base_dir='E:\\down'
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    data=getDownData()
    for i in data:
        #拿到图片路径转换为列表
        imgs_url= i[2].split(',')
        #列表生成器，构造下载url和文件名称
        urls=[{'url':img,'name':img.split('/')[-1]} for img in imgs_url]
        #下载地址
        outpath=os.path.join(base_dir,i[1])
        #初始化下载器并开始下载
        print "++++++++++++++++> id=%s"%i[0]
        down=Multi_DownLoad(urls,threadCount=2,outDir=outpath)
        down.starDown()
        #更新数据库
        updateData(i[0])
        print "change downflag"
    
    
def write():
    data=getDownData()
    if data[1]:
        with open('E:\porn.txt','a') as f:
            for i in data:
                line=i[0]+"####"+i[1]+'\n'
                #print line
                f.write(line.encode('utf-8'))
        f.close()
    else:
        pass
if __name__=="__main__":
    #data=getDownData()
    #print data
    write()
    #downpic()
    print "done"
