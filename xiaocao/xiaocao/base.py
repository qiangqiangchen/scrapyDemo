# -*- coding: utf-8 -*-
class Base(object):
    def __init__(self):
        self.id=""
        self.title=""
        self.user_nick=""
        self.creat_date=""
        
    def set_id(self,id):
        self.id=id
    def get_id(self):
        return self.id
        
    def set_title(self,title):
        self.title=title
    def get_title(self):
        return self.title
    
    def set_user_nick(self,user_nick):
        self.user_nick=user_nick
    def get_user_nick(self):
        return self.user_nick
    
    def set_creat_date(self,creat_date):
        self.creat_date=creat_date
    def get_creat_date(self):
        return self.creat_date
        
        
class xc_video(Base):
    def __init__(self):
        self.video_path=""
    def set_video_path(self,video_path):
        self.video_path=video_path
    def get_video_path(self):
        return self.video_path
        
class xc_forum(Base):
    def __init__(self):
        self.images=[]
        self.magnets=[]
    def set_images(self,images):
        self.images=images
    def get_images(self):
        return self.images
        
    def set_magnets(self,magnets):
        self.magnets=magnets
    def get_magnets(self):
        return self.magnets

class xc_picture(Base):
    def __init__(self):
        self.imgs=""
    def set_imgs(self,imgs):
        self.imgs=imgs
    def get_imgs(self):
        return self.imgs
        
class xc_text(Base):
    def __init__(self):
        self.text=""
    def set_text(self,text):
        self.text=text
    def get_text(self):
        return self.text

        
if __name__=="__main__":
    xc_text=xc_text()
    xc_text.id="10086"
    print xc_text.get_id()
