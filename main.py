import os

shutdown=input("do you wish to shutdown your pc/computer ?(yes/no):")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")