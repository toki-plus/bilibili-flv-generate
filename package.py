import os, sys, shutil

#传入目录文件的路径，得到目录文件的第一行
def getFirstLine(path):
    f = open(path, mode='r+', encoding='utf-8')
    a = f.readline()
    lis = []
    lis.append(a)
    b = lis[0][0:-1]
    f.close()
    return b

#传入目录文件的路径，从目录文件得到目录的总行数
def grtDirLen(path):
    f = open(path, mode='r+', encoding='utf-8')
    lis = []
    for line in f.readlines():
        lis.append(line)
    lis.pop(0)
    f.close()
    return len(lis)

#传入目录文件的路径，根据目录文件制作一个.flv结尾的目录列表
def mkFlvDirList(path):
    f = open(path, mode='r+', encoding='utf-8')
    lis1 = []
    for line in f.readlines():
        lis1.append(line)
    lis1.pop(0)
    f.close()
    lislen = len(lis1)
    lis2 = []
    for i in range(lislen-1):
        lis2.append(lis1[i][0:-1] + ".flv")
    lis2.append(lis1[-1] + ".flv")
    return lis2

#传入目录长度，创建一个str型的数字列表，用于寻找文件夹
def mkStrNumList(num):
    lis = []
    for i in range(1,num+1):
        lis.append(str(i))
    return lis

#传入flv文件的上一级目录、目录长度、数字列表、目录列表，对所有flv重命名
def renameFlv(path, num, nlist, dlist):
    os.chdir(path)
    for i in range(num):
        os.chdir(nlist[i])
        dirs = os.listdir(os.getcwd())
        for j in dirs:
            if os.path.splitext(j)[1] == '.flv':
                os.rename(j, dlist[i])
                shutil.move(dlist[i], path)
        os.chdir(path)

#c传入目录长度、数字列表，删除所有文件夹和非flv文件
def removeNoFlv(num, nlist):
    for i in range(num):
        shutil.rmtree(nlist[i])
    dirs = os.listdir(os.getcwd())
    for k in dirs:
        if os.path.splitext(k)[1] != '.flv':
            os.remove(k)

#传入视频路径、视频代号、目录名称，重命名上一级目录名字为
def renameLastDir(path, num, name):
    mvname = os.path.splitext(name)[0]
    os.chdir(path)
    dirs = os.listdir(os.getcwd())
    for j in dirs:
            if j == num:
                os.rename(j, mvname)