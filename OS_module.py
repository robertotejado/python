print("OS Module")

import os
home=os.getcwd()
print(home)

############################
#Lanza el navegador firefox
#import os
#browser=os.system('firefox')


#######################################
##Lanza el chrome con la web de youtube musica
#import os 
#os.system('google-chrome "https://youtube.com/feed/music" ')

#################################################
#Lanza el navegador brave a una web indicada
#import os
#os.system('brave-browser "https://bdmpublications.com" ')

#####################################################
#Lanza navegador chrome con variable
#import os 
#a=('google-chrome "http://www.facebook.com"  ')
#os.system(a)

######################################################

import os
print("crea carpeta folder")
os.mkdir("./folder")
print("renombra carpeta folder a carpeta")
os.rename("./folder", "./carpeta")
print("elimina la carpeta carpeta")
os.rmdir("./carpeta")

############################################################


import os , shutil ,  time
t= str(time.strftime("%Y-%m-%d %H-%M"))
root_src_dir = './documents' #Path del directorio fuente
root_dst_dir = './backup' + t #Path para el directorio de copias de seguridad

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
for file_ in files:
    src_file = os.path.join(src_dir, file_)
    dst_file = os.path.join(dst_dir, file_)
    if os.path.exists(dst_file):
        os.remove(dst_file)
    shutil.copy(src_file, dst_dir)
print(">>>>>>>>>>Backup complete<<<<<<<<<<")