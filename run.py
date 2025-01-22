import os
import platform
import time
fuck = platform.architecture()[0]
if fuck == '64bit':
    os.system('git pull')
    os.system('clear')
    print('\x1b[1;94m[√] \x1b[1;92mYour Device is 64 bit')
    time.sleep(2)
    from f64 import MX1
    MX1()
    return None
if fuck == '32bit':
    os.system('git pull')
    os.system('clear')
    print('\x1b[1;94m[√] \x1b[1;92mYour Device is 32 bit')
    time.sleep(2)
    exit()
    return None
os.system('clear')
print('\x1b[1;97m Soon Your Device Supported Tools ')
