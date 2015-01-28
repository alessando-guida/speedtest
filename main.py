#!/usr/bin/python3.4
__author__ = 'ale'

# Descrizione
# ===========
# Python script che esegue principalmente la funzione di testare
# la velocità di internet e di salvare i dati in un file di log.
# Si divide quindi in 3 fase:
#   - eseguire speedtest
#   - parse the output
#   - aggiunge l'output al file di log.
#
# Dependency:  python 3.4
#              speedtest-cli - https://github.com/sivel/speedtest-
#

import subprocess
import re
import time
import os


#CONFIGURA LA POSIZIONE DELLE CARTELLE in variabili GLOBALI
#posizione dello script
MYPATH = "/home/ale/Documents/Projects/monitor-internetband/"
#posizione del file
SPEEDTEST_PATH = "/usr/local/bin/"


#get data e ora and print it
mytime = (time.strftime("%d/%m/%Y\t%H:%M:%S"))
print(mytime+"\n-----------------")

#RUN THE COMMAND
print("Testing the internet speed...")
try:
    mycommand = subprocess.check_output([SPEEDTEST_PATH+"speedtest", "--simple"], stderr=subprocess.STDOUT)
    #converti il file da bytes-like a stringa
    mycommand = mycommand.decode("utf-8")

    #DEBUG MODE: fake commnad
    #mycommand = "b'Ping: 12.96 ms\nDownload: 1.17 Mbits/s\nUpload: 0.79 Mbits/s\n'" #FAKE COMMAND
    #mycommand = subprocess.check_output(["cat", "baabasd asdasd"], stderr=subprocess.STDOUT) # exit with 1

except Exception:
    print("!!! Problema riscontrato nel test di connessione a internet !!!")
    #aggiunta di una finta stringa, in caso di problema di connessione fa il parsi di questa stringa.
    mycommand = 'Ping: 2000.00 ms\nDownload: 0.00 Mbits/s\nUpload: 0.00 Mbits/s\n'


#stampa a video i risultati del test
print(mycommand)

#CAPTURE THE OUTPUT TEXT
print("parsing data...")
#find Ping
ping = re.search(r"Ping: (.*) ms", mycommand).group(1)
#find Download
download = re.search(r"Download: (.*) Mbits", mycommand).group(1)
#find Upload
upload = re.search(r"Upload: (.*) Mbits", mycommand).group(1)

#LEGGI FILE
print("updating the log file...")
try:
    myfile = open(os.path.join(MYPATH+"speed_log.txt"), "a")
    myfile.write(mytime+"\t"+ping+"\t"+download+"\t"+upload+"\n")
    myfile.close()
    print("DONE")
except IOError:
    raise IOError("OPSS, can't open/find the file??? ")
