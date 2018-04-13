# Installare pip su Ubuntu (e similari)

> Verificare di aver installato Python.  
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