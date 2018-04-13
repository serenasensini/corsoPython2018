# Installare PyQt4 su Windows

> Verificare di aver installato Python. Se non è installato Python 2.x, seguire il tutorial a questo [link](https://github.com/serenasensini/corsoPython2018/blob/master/Tutorial/Installare%20Python%20su%20Windows.md). Per verificare che siano installati, è sufficiente digitare 
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
- Scaricare il pacchetto PyQt in formato .whl da questo [sito](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4), scegliendo tra la versione a 32-bit o 64-bit.

### Istruzioni
- Digitare dalla riga di comando (è possibile aprirla digitando "cmd" cliccando sul pulsante "Start")
```
pip install \path\to\pyqt4\whl\file
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

- E' possibile eseguire direttamente il codice da riga di comando salvando il precedente codice in un file ed eseguendo:
'''
python \path\to\file
'''


> Suggerimento: a questo [link](https://www.python.it/wiki/show/qttutorial/) esiste un tutorial in italiano che fornisce una panoramica dell'uso di PyQt.