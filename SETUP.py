import time
import os
import json
from getpass import getpass
import subprocess
import time
import codecs
print('Welcome to')
print('''  ____        _ _______                _            
 |  _ \      | |__   __|              | |           
 | |_) | ___ | |_ | |_      _____  ___| |_ ___ _ __ 
 |  _ < / _ \| __|| \ \ /\ / / _ \/ _ \ __/ _ \ '__|
 | |_) | (_) | |_ | |\ V  V /  __/  __/ ||  __/ |   
 |____/ \___/ \__||_| \_/\_/ \___|\___|\__\___|_| v1.3.2\n''')

x = input("Do you want to begin the setup? (y/n): ")
if x != 'y' and x != 'yes':
    print('exiting')
    os._exit(0)
else:
    print('Installing packages...')
    os.system('cmd /c "python -m pip install tweepy"')
    os.system('cmd /c "python -m pip install pycryptodomex"')
    from Cryptodome.Cipher import AES
    print('\nPackages successfully installed!')
    auth = input('auth: ')
    authsecret = input('auth secret: ')
    key = input('key: ')
    keysecret = input('keysecret: ')
    
    uuid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip().split('-')
    ekey = uuid[0]+uuid[2]+uuid[1]
    encrypt = AES.new(ekey.encode("utf8"), AES.MODE_CFB, 'BotTweeterMadlad'.encode("utf8"))
    aesauth = encrypt.encrypt(auth.encode("utf8"))
    aesauthsecret = encrypt.encrypt(authsecret.encode("utf8"))
    aeskey = encrypt.encrypt(key.encode("utf8"))
    aeskeysecret = encrypt.encrypt(keysecret.encode("utf8"))

    data = [aesauth, aesauthsecret, aeskey, aeskeysecret]
    dataold = {'auth':str(aesauth), 'authsecret':str(aesauthsecret), 'key':str(aeskey), 'keysecret':str(aeskeysecret)}
    with open('auth.data', 'wb') as f:
        for item in data:
            f.write(item+'\n'.encode('utf-8'))
    print('\nSetup successful! You can now open BotTweeter.py!')
    time.sleep(5)
    exit()
