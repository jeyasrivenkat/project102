import os
import shutil

frompath='C:/Users/jeyas/Downloads'
topath='C:/Users/jeyas/Downloads/Coding/C102_assets-main/img'

listof=os.listdir(frompath)
print(list)

for i in listof:
    name,extension=os.path.splitext(i)
    #print(name)
    print(extension)
    if(extension==''):
        continue
    if(extension in['.txt','.doc','.docx','.pdf']):
        path1=frompath+'/'+i
        path2=topath+'/'+'img'
        path3=topath+'/'+'img'+i
        if os.path.exists(path2):
            print('moving'+i+'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving'+i+'...')
            shutil.move(path1,path3)