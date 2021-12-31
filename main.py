#-*-coding:utf8;-*-
__author__ = "nagayev"
__version__ = 1.1

import json

DEFAULT='/storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/Chili/local_storage.json'

class SBHack:
    def __init__(self,filename=DEFAULT):
        self.f=open(filename,'rb')
        content=self.f.read()
        try:
            self.obj=json.loads(content)
        except Exception as e:
            print('Error was occurred')
            if content==b'':
                print('File is empty')
            else:
                print(e,content)
            exit(1)
    def _raw_set(self,type,value):
        type=str(type)
        self.obj['Profile']['wallet']['currencies'][type]=value
    def set_money(self,value):
        self._raw_set(1,value)
    def set_keys(self,value):
        self._raw_set(2,value)
    def set_skates(self,value):
        self._raw_set(3,value)
    def set_headstarts(self,value):
        self._raw_set(4,value)
    def set_boosters(self,value):
        self._raw_set(5,value)
    def finish(self):
        #save changes to disk
         self.__del__()
         with open(DEFAULT,'w') as f:
            f.write(json.dumps(self.obj))  
         #self.__del__()
    def __del__(self):
        #close file
        self.f.close()
def inp(s):
    return int(input('Input '+s+' '))
if __name__ == "__main__":
    s=SBHack()
    #s.set_money(1000)
    print('Welcome to Subway Hacker')
    msg='Choose command\n'
    msg+='m-money\nk-keys\n'
    msg+='h-headstarts\nsb-core boosters\n'
    msg+='q-quit and save'
    while True:
        print(msg)
        c=input()
        if c=='q':
            s.finish()
            print('Succesful!')
            print('Bye')
            exit()
        elif c=='m':
            m=inp('money')
            s.set_money(m)
        elif c=='k':
            k=inp('keys')
            s.set_keys(k)
        elif c=='h':
            k=inp('headstarts')
            s.set_headstarts(k)
        elif c=='b':
            k=inp('boosters')
            s.set_boosters(k)
