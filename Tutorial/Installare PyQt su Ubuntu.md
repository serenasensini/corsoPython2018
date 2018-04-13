# Installare PyQt4 su Ubuntu (e similari)

> Verificare di aver installato pip. Se non è installato pip, seguire il tutorial a questo [link](https://github.com/serenasensini/corsoPython2018/blob/master/Tutorial/Installare%20pip%20su%20Ubuntu.md). Per verificare che siano installati, è sufficiente digitare 
``` python ```
e verificare che ci sia un output del tipo:
```
Python 2.7.0a2 (...)  
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Fare la stessa cosa per pip: digitare
``` pip ```
e verificare che ci sia un output del tipo:
```
Usage:         
pip <command> [options]         
Commands:                                                                                                                 
install                     Install packages.       
```
### Passi preliminari
Aggiornare il sistema con il comando:
```
sudo apt update && sudo apt -y upgrade
```

### Istruzioni
-Digitare il seguente comando per installare:
```
sudo apt-get install python-qt4
```
- Per verificare che l'installazione sia andata a buon fine, importare il modulo pyqt4 in un progetto Python e verificare che non dia errori di compilazione. Si può usare il seguente codice per testare:
```
import sys
import PyQt4.QtGui
app = QApplication(sys.argv)
button = QPushButton("Hello World!", None)
button.show()
app.exec_()
```

> Suggerimento: a questo [link](https://www.python.it/wiki/show/qttutorial/) esiste un tutorial in italiano che fornisce una panoramica dell'uso di PyQt.