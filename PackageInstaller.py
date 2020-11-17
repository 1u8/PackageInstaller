import subprocess
import sys
import pkg_resources
import argparse
import time
import sys
import threading
import itertools


print('[-]---------------PYTHON PACKAGE INSTALLER---------------[-]')
print('\n[-Developed by @1u8 on github/@SkidTheNoob on Twitter.-]')
print('\n[-] Installing packages (This might take some time) [-]')


done = False
def animate():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if done:
            break
        sys.stdout.write('\r[+] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r[!] New packages found [!] ')
    print('\n[+] Installing.. [+]')

t = threading.Thread(target=animate)
t.start()

time.sleep(10)
done = True	

required = {'numpy','pandas','toml','aiohttp-socks','apparmor','numpy','helpdev','onboard','pillow','pycparser','pyperclip','pynacl','protonvpn-cli','astroid','pyaes','whoosh','regex','celery','pycrypto','setuptools-git','ladon'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed


if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',*missing])

print('\n[!] No new packages! [!] ')

print('\nNow listing all installed packages..')

print('\n[+] Currently loading Installed User Packages-[=]')
done = False
def animate():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if done:
            break
        sys.stdout.write('\r[+] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r[!] Finished, all packages installed! [!]    ')

t = threading.Thread(target=animate)
t.start()

time.sleep(5)
done = True	
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)
