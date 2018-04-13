# Installare pip su Windows

> Verificare di aver installato Python. Se non è installato Python 2.x, seguire il tutorial a questo [link](https://github.com/serenasensini/corsoPython2018/blob/master/Tutorial/Installare%20Python%20su%20Windows.md). Per verificare che siano installati, è sufficiente digitare 
``` python ```
e verificare che ci sia un output del tipo:
```
Python 2.7.0a2 (...)  
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Istruzioni
- Cercare la cartella di installazione di Python e posizionarsi nella cartella \Pythonx.x\Scripts\;
- Al suo interno, dovrebbe essere presente un file chiamato "pip"; per installarlo, sarà sufficiente aggiungerlo alle variabili di ambiente di sistema;
- Per aggiungere pip alle variabili di ambiente, recarsi sulle Impostazioni/Pannello di Controllo e cercare "Variabili di Ambiente";
- Si aprirà una finestra chiamata "Proprietà di sistema"; in fondo, cliccare sul pulsante "Variabili di ambiente";
- Aggiungere alla variabile "Path" di sistema (e dell'utente) il path recuperato al primo punto.
Nota: per versioni di Windows > 8, sarà sufficiente cliccare su "Nuovo" per aggiungere una variabile d'ambiente; per le versioni precedenti, bisognerà assicurarsi che la stringa già presente termini con un punto e virgola. Solo dopo si potrà aggiungere il path trovato al primo punto!

- Per verificare che l'installazione sia andata a buon fine, digitare da riga di comando (è possibile aprirla digitando "cmd" cliccando sul pulsante "Start")

``` python ```
e verificare che ci sia un output del tipo:
```
Python 2.7.0a2 (...)  
Type "help", "copyright", "credits" or "license" for more information.
>>>
```