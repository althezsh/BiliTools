import os

path=input('请输入文件路径')

f=os.listdir(path)

n = 0
for i in f:
    oldname = path + f[n]
    
    print(f[n])

    truename = input('请输入学生姓名\n')

    newname = oldname  + truename + '.jpg'
    os.rename(oldname,newname)
    print(oldname,"=====>",newname)
    n+=1