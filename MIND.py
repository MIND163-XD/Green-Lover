import os, platform, time
os.system('termux-setup-storage')
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')  
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
print('\n\x1b[1;37m[✓] Checking Update...');time.sleep(0.5)
os.system('git pull')
def mind():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m[✓] Congratulations ! Your Device Support this Tools")
            print('[✓] Join My Facebook Group ')
            os.system('xdg-open https://facebook.com/groups/587970852914505/')
            import XD
        else:
            exit('\033[1;31m[×] Sorry, Your Device Not Support This Tool')
mind()
