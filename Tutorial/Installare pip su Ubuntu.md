# Installare pip su Ubuntu (e similari)

> Verificare di aver installato Python. Se non è installato Python 2.x, seguire il tutorial a questo [link](https://github.com/serenasensini/corsoPython2018/blob/master/Tutorial/Installare%20Python%20su%20Windows.md). Per verificare che siano installati, è sufficiente digitare 
``` python ```
e verificare che ci sia un output del tipo:
```
Python 2.7.0a2 (...)  
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Passi preliminari
Aggiornare il sistema con il comando:
```
sudo apt update && sudo apt -y upgrade
```

### Istruzioni
-Digitare il seguente comando per installare:
```
sudo apt-get install python-pip
```
- Per verificare che l'installazione sia andata a buon fine, digitare
``` pip ```
e verificare che ci sia un output del tipo:
```
Usage:         
pip <command> [options]         
Commands:                                                                                                                 
install                     Install packages.       
```

> Suggerimento: a questo [link](https://www.rosehosting.com/blog/how-to-install-pip-on-ubuntu-16-04/) ci sono molte informazioni utili su come usare il comando pip.