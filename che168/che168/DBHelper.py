import MySQLdb
from scrapy.utils.project import get_project_settings
class DBHelper(object):
    def __init__(self):
        self.settings=get_project_settings()
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
        #print self.host
        #print self.port
        #print self.passwd
        #print self.db
        #print self.user
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
            cur.close()
            conn.close()
    def select(self,sql):
        conn=self.connectDatabase()
        cur=conn.cursor()
        try:
            cur.execute(sql)
            data=cur.fetchone()
            return data
        except:
            print 'Error:unable to fecth data'
            cur.close()
            conn.close()
            return None