﻿#coded_by_UMAIRAFZAL
import itertools, threading, time, sys, os
import requests
import rich
import json,os,sys,random,datetime,time,re
from rich.console import Console as sol
from concurrent.futures import ThreadPoolExecutor as UMAIRthread
from rich import pretty
from random import choice as UMAIRchoice
A = '\x1b[0;97m' 
B = '\x1b[0;91m' 
C = '\x1b[0;92m' 
D = '\x1b[0;93m' 
E = '\x1b[0;94m'
F = '\x1b[0;95m' 
G = '\x1b[0;96m' 
H = '\x1b[0m'   
I='\x1b[0;32m'
J='\x1b[0;36m'
K='\x1b[0;31m'
L='\x1b[0;35m'
M='\x1b[0;33m'
N='\033[0;37m'
O='\x1b[00m'
P='\x1b[0;90m'
Q="\x1b[00m"
R='\x1b[0;32m'
S='\x1b[0;36m'
T='\x1b[0;31m'
U='\x1b[0;35m'
V='\x1b[0;33m'
W='\x1b[0;34m'
X='\033[0;37m'
Y='\x1b[00m'
Z='\x1b[0;90m'
ses=requests.Session()
def UMAIRflash(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
        
def UMAIRflashlogo(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

uid = []
linex = ('\033[0;97m═══════════════════════════════════════════════')

a = '\x1b[1;97m'
b = '\x1b[1;91m'
c = '\x1b[1;92m'
d = '\x1b[1;93m'
e = '\x1b[1;94m'
f = '\x1b[1;95m' 
g = '\x1b[1;96m'
h = '\x1b[0m'    
i = "\033[1;30m"
j = '\033[41m\x1b[1;97m'
k = '\33[m' # mix
l = '\x1b[1;91m' #lal +
m = '\033[93m' # pila +
n = '\x1b[1;92m' # hara +
o = '\033[32m' # hara2 -
p = '\033[95m' # gulabai
q = '\033[33m' # pila2 -
r = '\33[1;96m' # surkh -
s = '\x1b[0;34m' # halka nila +
UMAIRcol = random.choice([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R])



def sz__love(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    try:
        os.system('clear')
    except KeyError or IOError:
        os.system('cls')
def UMAIRgo():
	clear()
	UMAIRflashlogo(f'{UMAIRcol}   \n[UMAIR]😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘   \n[KING]😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈 \n[FREE]😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇 \n[FILE]😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎 \n[MAKING]❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️❣️\n[TOOL]😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍 ')
	UMAIRflashlogo(f'{linex}\n Author    : UMAIR AFZAL\n Version   : 1.0\n Github    : Umairafzal203\n Tool Type : File Making\n Contact   : 03032081002\n{linex}\n\t\tEnjoy Free Dumping Tools for Public')
def check_login():
	try:
		token = open('UMAIRtoken.txt','r').read()
		cok = open('UMAIRcok.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+token, cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except :login()
	except requests.exceptions.ConnectionError:
		li = 'Connection Problem'
		exit()
	except IOError:
		login()
'''
This source code is provided free by UMAIR AFZAL organization and if you use our source code you are requested to please follow and give us credits
'''
	
def login():
 try:
  clear()
  print('') 
  ses = requests.Session();UMAIRgo();print(linex)
  cookie = input('\nEnter Facebook Cookies : ')
  cookies = {'cookie':cookie}
  url = 'https://www.facebook.com/adsmanager/manage/campaigns'
  req = ses.get(url,cookies=cookies)
  set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
  nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
  roq = ses.get(nek,cookies=cookies)
  tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
  tokenw = open("UMAIRtoken.txt", "w").write(tok)
  cokiew = open("UMAIRcok.txt", "w").write(cookie)
  UMAIRflash(f'{linex}\nLogin SuccessFull\n ')
  check_login()
 except Exception as e:
  os.system("rm -f UMAIRtoken.txt")
  os.system("rm -f UMAIRcok.txt")
  print(f' Login Failed (May be Cookies are Expired)')
  exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(sy2,sy3):
	try:
		tok = open('UMAIRtoken.txt','r').read()
		cok = open('UMAIRcok.txt','r').read()
	except ValueError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		check_login()
	clear()
	UMAIRgo()
	ip = requests.get("https://api.ipify.org").text
	sz__love(f'{linex}\n\x1b[1;37m>> IP    : {ip}');sz__love(f'\x1b[1;37m>> Name  : {sy2}');sz__love(f'\x1b[1;37m>> UID   : {sy3}\n{linex}')
	print('[1] Create File Public (Unlimited)')
	print('[2] Remove Double Links')
	print('''[3] Seperate New ID's Links''')
	print('''[4] Removing Part of File''')
	print('''[5] Contact Owner''')
	print('''[6] Remove Cookies''')
	print('''[0] Exit''')
	UMAIRin = input(f'{linex}\n>> Select : ')
	print('')
	if UMAIRin in ['1' or '01']:
		filename()
	elif UMAIRin in ['2' or '02']:
		remove_double()
	elif UMAIRin in ['3' or '03']:
		sorting_file()
	elif UMAIRin in ['4'or'04']:
		part_remove()
	elif UMAIRin in ['5' or '05']:
		contact_author()
	elif UMAIRin in ['6' or '06']:
		rem_login()
	elif UMAIRin in ['0' or '00']:
		UMAIRflash('Thanks For Using My Tool')
	else:
		errorz()
def errorz():
	UMAIRflash(f'{k}>>Please Choose Correct Option {x}')
	time.sleep(3)
	check_login()
def rem_login():
	os.system('rm -rf sol*')
	UMAIRflash('Cookies SucessFully Removed')

#===========Filename
def filename():
    clear();UMAIRgo()
    UMAIRflash(f'{linex}\nExample : /sdcard/UMAIRfile.txt')
    filen=input(f'{linex}\nEnter File Path : ')
    superfile(filen)
#-------------------[ CRACK-PUBLIK ]-------------
###################################
def superfile(filen):
	try:token = open('UMAIRtoken.txt','r').read();cok = open('UMAIRcok.txt','r').read()
	except IOError:exit()
	kil = input(f'{linex}\nEnter Link of Public ID : ');namesep = kil.split('|'); kl = namesep[0];clear();UMAIRgo()
	uid.append(kl);print(f'{linex}\nDumping Started \nPress Ctrl+Z to stop\n{linex}\nFile Will be Saved in {filen}\n{linex}')
	for userr in uid:
		try:
			linkdump =ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for appui in linkdump['friends']['data']:
				try:
					UMAIRid = (appui['id']+'|'+appui['name'])
					if UMAIRid in id:pass
					else:id.append(UMAIRid)
					zxx=open(filen, "a+").write(UMAIRid+'\n');zxx.close()
				except:pass
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Network Error ')
			exit()
	try:
		with UMAIRthread(max_workers=30) as (UMAIRhacker):
			juma = open(filen,"r").readlines()
			for data in juma:
				data = data.replace("\n","")
				kiky = data.split("|")
				useriid = ("%s"%(kiky[0]))
				nm = ("%s"%(kiky[1]))
				UMAIRhacker.submit(multi_file, useriid,filen)

	except requests.exceptions.ConnectionError:
		print(f'{x}')
		UMAIRflash('>> Network Error ')
		check_login()
	except (KeyError,IOError):
		UMAIRflash(f'>>{k} This is Private Account {x}')
		time.sleep(3);check_login()
#============================
xz = []
def multi_file(useriid,filen):
	try:token = open('UMAIRtoken.txt','r').read();cok = open('UMAIRcok.txt','r').read()
	except IOError:exit()
	xaz=open(filen,'a+')
	try:
		linkdump =ses.get(f'https://graph.facebook.com/{useriid}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
		for appui in linkdump['friends']['data']:
				try:
					UMAIRid = (appui['id']+'|'+appui['name'])
					if UMAIRid in id:pass
					else:id.append(UMAIRid);xaz.write(UMAIRid+'\n')
				except:pass
		linkdump1 =ses.get(f'https://graph.facebook.com/{useriid}?fields=subscribers.limit(999999)&access_token={token}',cookies = {'cookies':cok}).json()
		for appzi in linkdump1['subscribers']['data']:
				try: 
					xui = (appzi['id']+'|'+appzi['name'])
					if xui in id:pass
					else:id.append(xui);xaz.write(xui+'\n')
					xaz.close()
				except:pass
	except KeyError:pass
	
	sys.stdout.write("\r%s[%sExtracted Accounts ]%s •> %s"%(Q,UMAIRchoice([U,I,K,h,M,C]),Q, len(id))); sys.stdout.flush()
#============================
def remove_double():
    clear();UMAIRgo()
    UMAIRflash(linex)
    file = input ('\033[0;92m Enter Your File Path : ')
    UMAIRflashlogo(linex)
    os.system(f'sort -u -r -o {file} {file} --quit 2>/dev/null')
    print ('\n[*] SuccessFully Removed Double Links')
    print ('[*] File Saved in : '+file)
    input(f'{linex} \nPress Enter to go back to Main Menu')
    clear()
    check_login()
    
def sorting_file():
    clear();UMAIRgo()
    UMAIRflashlogo(linex)
    try:linkslimit = int(input(' How many links do you want to Seperate : '))
    except:linkslimit = 1
    UMAIRflashlogo(f'{linex}\nPlease Enter File Path\nExample: /sdcard/mfile.txt')
    file = input (f'{linex}\nInput Your File Path : ')
    fileout = input(f'Where Do you want to save the File : ')
    y = 0
    UMAIRflashlogo(f"{linex}\n Links You Want To Keep\nExample : [100088,100089,100090etc]")
    os.system('rm -rf 1.txt');os.system('rm -rf .UMAIR.txt')
    for k in range(linkslimit):y+=1;links=input('Put Links : ');os.system('cat '+file+' | grep "'+links+'" >> '+fileout+' --quiet 2>/dev/null')
    os.system(f'sort -u -r -o {fileout} {fileout} --quit 2>/dev/null')
    UMAIRflashlogo(f'{linex}\n Accounts SuccessFully Extracted');print(' Total Accounts Extraced : '+str(len(open(fileout,'r',encoding='utf-8').read().splitlines())))
    print('\033[0m New Accounts File saved in : \033[0;32m'+fileout)
    input(f'{linex}\nPress Enter to go back to Main Menu')
    clear()
    check_login()
#=====================
def part_remove():
    clear();UMAIRgo()
    UMAIRflashlogo(f'''{linex}\nType (UMAIR) if you want help''')
    UMAIRflashlogo(f'''{linex}\nExaple : newfile.txt''')
    UMAIRinput1 = input(f'{linex}\nEnter The File You Want To Remove Part of :')
    if ('UMAIR' or 'UMAIR'or '(UMAIR)' or 'UMAIR') in UMAIRinput1:
        contact_author()
    else:
        UMAIRflashlogo(f'{linex}\nExample : If You want to remove first \n1000 lines enter : 1000')
        xasi = input(f'{linex}\nHow Much Lines of File do you want to Remove:')
        os.system('sed -i 1,'+xasi+'d '+UMAIRinput1)
        UMAIRflashlogo(f'{linex}\nYour File is Saved in {UMAIRinput1}\nFirst {xasi} lines are removed')
def contact_author():
	UMAIRflashlogo('Wait! You Will Be redirected to author of the tool')
	os.system('xdg-open https://wa.link/+9203032081002')
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('rm -rf ..UMAIR.txt')
	except:pass
	try:os.system('rm -rf .UMAIR.txt && rm -rf tmp')
	except:pass
	os.system('rm -rf ..ijs.txt')
	check_login()

#>>>>> ALLAH HAFEZ  <<<<<<<#
