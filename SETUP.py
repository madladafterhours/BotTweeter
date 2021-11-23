import time
import os
import json
print('Welcome to')
print('''  ____        _ _______                _            
 |  _ \      | |__   __|              | |           
 | |_) | ___ | |_ | |_      _____  ___| |_ ___ _ __ 
 |  _ < / _ \| __|| \ \ /\ / / _ \/ _ \ __/ _ \ '__|
 | |_) | (_) | |_ | |\ V  V /  __/  __/ ||  __/ |   
 |____/ \___/ \__||_| \_/\_/ \___|\___|\__\___|_| v1.2\n''')

x = input("Do you want to begin the setup? (y/n): ")
if x != 'y' and x != 'yes':
    print('exiting')
    os._exit(0)
else:
    os.system('cmd /c "python -m pip install tweepy"')
    auth = input('auth: ')
    authsecret = input('auth secret: ')
    key = input('key: ')
    keysecret = input('keysecret: ')
    data = {'auth':auth, 'authsecret':authsecret, 'key':key, 'keysecret':keysecret}
    with open('auth.data', 'w') as f:
        json.dump(data, f)
    print('\nSetup successful! You can now open BotTweeter.py!')
