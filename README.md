Monitor banda connessione internet
=======================================

### DESCRIZIONE:
Applicazione semplice per creare un log dello stato della connessione a internet. 
Questo programma utilizza il seguente comando:

    $ speedtest --simple

e cattura l'output generato nel formato:

    > Ping: 12.96 ms
    > Download: 1.17 Mbits/s
    > Upload: 0.79 Mbits/s
 
Lo script in python eseguite il parsing e aggiorna il file _**speed_log.txt**_. 
In caso il testo non vada a buon fine, viene catturata l'eccezione e automaticamente 
aggiornati i valori di banda di connessione pari a "0".
L'output generato è un TAB spaced table. Questo script è stato studiato per essere 
utilizzato in congiunta con "Crontab". Modificare Crontab ed aggiungere quindi l'intervallo 
di tempo desiderato per eseguire i test.

### DIPENDENZE: 
- **speedtest-cli** - version 0.3.1 - https://github.com/sivel/speedtest-
- **Python 3.4**

### INSTALLAZIONE DIPENTENZE:
    $ pip install speedtest-cli

###USAGE:
modificare lo script e cambiare le variabili globali che puntano al eseguibile __speedtest__ e la __PATH__ dove si trovano gli scripts

    $ python main.py

###NOTE:
La tabella puo' quindi successivamente essere importata in excell per visualizzare graficamente il tutto.
Per configurare crontab e far partire lo scrip ogni 30 minuti usare
 
    crontab -e
 
e aggiungere la seguente riga: 

    */30 * * * * /usr/bin/python3.4 /PATH/main.py /PATH/croneout.txt 2>&1

questo fara partire lo script ogni 30 minuti e manda lo STDOUT e STDERR output nel file __croneout.txt__ specificato. 


