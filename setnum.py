import package as pk

def bilibili(path):
    dirpath = "C:\\Users\\Toki\\Desktop\\" + path
    mvpath = "D:\\bilibili\\"
    mvnum = pk.getFirstLine(dirpath)
    flvpath =  mvpath + mvnum
    dirlength = pk.grtDirLen(dirpath)
    dirlist = pk.mkFlvDirList(dirpath)
    numlist = pk.mkStrNumList(dirlength)
    pk.renameFlv(flvpath, dirlength, numlist, dirlist)
    pk.removeNoFlv(dirlength, numlist)
    pk.renameLastDir(mvpath, mvnum, path)
    