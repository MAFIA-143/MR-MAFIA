import os
import platform
import time
os.system("pip install requests")
fuck = platform.architecture()[0]
if fuck == '64bit':
    os.system('git pull')
    os.system('clear')
    print('\x1b[1;94m[√] \x1b[1;92mYour Device is 64 bit')
    time.sleep(2)
    from MX3 import MX3
    MX3()
if fuck == '32bit':
    os.system('git pull')
    os.system('clear')
    print('\x1b[1;94m[√] \x1b[1;92mYour Device is 32 bit')
    time.sleep(2)
    MX3() 
os.system('clear')
print('\x1b[1;97m Soon Your Device Supported Tools ')
