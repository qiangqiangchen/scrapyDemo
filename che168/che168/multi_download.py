# -*- coding: utf-8 -*-
import threading
import time
import requests
from contextlib import closing
import os
import Queue
import random



#下载器，继承threading.Thread
class download(threading.Thread):
    def __init__(self,que,out_dir):
        threading.Thread.__init__(self)
        self.que=que
        self.timeout=5
        self.out_dir=out_dir
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
            }
        self.agent=[
                'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
                'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
                'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
                'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
                'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
                'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
                'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3']
    def run(self):
        while True:
            #当队列不为空，从队列中取值
            if not self.que.empty():
                img=self.que.get()
                #调用下载方式
                self.down(img["url"], img["name"])
            else:
                break
    def down(self,img_url, img_name):
        agent_index=random.randrange(0,9)
        headers = {
            'User-Agent':self.agent[agent_index]
            }
        if os.path.isfile(os.path.join(self.out_dir, img_name)):
            return
        with closing(requests.get(img_url, stream=True, headers=headers, timeout=self.timeout)) as r:
            rc = r.status_code
            if 299 < rc or rc < 200:
                print('returnCode%s\t%s' % (rc, img_url))
                return
            content_length = int(r.headers.get('content-length', '0'))
            if content_length == 0:
                print('size0\t%s' % img_url)
                return
            try:
                with open(os.path.join(self.out_dir, img_name), 'wb') as f:
                    for data in r.iter_content(1024):
                        f.write(data)
                f.close()
            except:
                print('savefail\t%s' % img_url)
                
#下载器
#参数：(url,name)字典集合，线程数（默认1），下载路径（默认本地），下载间隔（默认0秒）
class Multi_DownLoad():
    
    def __init__(self,urls,threadCount=5,outDir='.\\outdir',times=0):
        self.urls=urls
        self.threadCount=threadCount
        self.outDir=outDir
        self.times=times
        self.tsk=[]
        
         #创建文件夹
        if not os.path.exists(self.outDir):
            os.mkdir(self.outDir)
        
    def starDown(self):
        que=Queue.Queue()
        for l in self.urls:
            que.put(l)
        for i in range(self.threadCount):
            d=download(que,self.outDir)
            time.sleep(self.times)
            d.start()
            self.tsk.append(d)
        for i in self.tsk:
            i.join()

    
   
if __name__=="__main__":
    
    ur12="http://g.91p11.space/attachments/18050512364587347f25d896c4.jpg,http://g.91p11.space/attachments/1805051236c347871a1f3c9c55.jpg,http://g.91p11.space/attachments/1805051237a97ea211eab849c9.jpg,http://g.91p11.space/attachments/1805051237fb77a53ac539e633.jpg,http://g.91p11.space/attachments/180505123734e8db94399880a7.jpg,http://g.91p11.space/attachments/1805051238e465935579b42a54.jpg,http://g.91p11.space/attachments/1805051238f9d85d76350b3550.jpg,http://g.91p11.space/attachments/1805051239a578a40450fa2fd4.jpg,http://g.91p11.space/attachments/1805051239a9c9f1b0af1e3451.jpg,http://g.91p11.space/attachments/18050512407c5b7edc723fd142.jpg,http://g.91p11.space/attachments/1805051240d2aae052b8e4d5d2.jpg,http://g.91p11.space/attachments/18050512416f06c837e864343c.jpg,http://g.91p11.space/attachments/180505124166eb1f040b62cbd0.jpg".split(',')
    url_list=[{'url':i,'name':i.split("/")[-1]} for i in ur12 ]
    time1=time.clock()
    down=Multi_DownLoad(url_list,outDir='E:\\down')
    down.starDown()
    print ("done")
    print time.clock()-time1