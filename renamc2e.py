#!/usr/bin/env python
#coding:utf-8

#目标文件夹
path=u"D:\opt"
#是否递归处理下级目录.1为递归,0为不递归
recursive=1

import os
from xpinyin import Pinyin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def setnewname(path,filenamec,filename2=''):
    p=Pinyin()
    filename=p.get_pinyin(filenamec, '')
    if not filename2 and filenamec == filename:
        print "略过",os.path.join(path,filename)
        return 0
    if filename2:
        filename=filename2
    if os.path.exists(os.path.join(path,filename)):
        ure='0'
        if "." in  filename:
            file_format=filename.split('.')[-1:][0]
            file_head_name='.'.join(filename.split('.')[:-1])
            if '_' in file_head_name:
                try:
                    ure=int(file_head_name.split('_')[-1:][0])+1
                    newfilename='%s_%s.%s' % ('_'.join(file_head_name.split('_')[:-1]),ure,file_format)
                except ValueError:
                    newfilename='%s_%s.%s' % (file_head_name,ure,file_format)
            else:
                newfilename='%s_%s.%s' % (file_head_name,ure,file_format)
        else:
            if '_' in filename:
                try:
                    ure=int(filename.split('_')[-1:][0])+1
                    newfilename='%s_%s' % ('_'.join(filename.split('_')[:-1]),ure)
                except ValueError:
                    pass
            else:
                newfilename='%s_%s' % (filename,ure)

        if os.path.exists(os.path.join(path,newfilename)):
            setnewname(path,filenamec,newfilename)
        else:
            #这里存在一个奇怪问题,下面的return 在我测试时返回始终是None,不得其解.
            os.rename(os.path.join(path,filenamec),os.path.join(path,newfilename))
            if os.path.isdir(os.path.join(path,newfilename)):
                return os.path.join(path,newfilename)
    else:

        os.rename(os.path.join(path,filenamec),os.path.join(path,filename))
        if os.path.isdir(os.path.join(path,filename)):
            return os.path.join(path,filename)




def filenamecover(path,recursive=1):
    #print "开始处理目录",path
    for file in  os.listdir(path):
        fullpath=os.path.join(path,file)
        runreturn=setnewname(path,file)
        #print "runreturn",runreturn
        if runreturn and  recursive == 1:
            filenamecover(runreturn,recursive)
        if os.path.isdir(fullpath) and  recursive == 1:
            #print fullpath
            filenamecover(fullpath,recursive)







filenamecover(path,recursive)







