#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Consiglio: leggere questa guida per saperne di più su segnali e slot, definendo dei propri segnali: https://wiki.qt.io/Signals_and_Slots_in_PySide
Lista (quasi) completa di segnali: https://stackoverflow.com/questions/13916419/where-can-i-find-a-list-of-all-pyqt-pyside-signals
'''

import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class MainWindow(QtGui.QMainWindow):
      def __init__(self):
              QtGui.QMainWindow.__init__(self)
              self.setWindowTitle('Box example')
              widget = QtGui.QWidget(self)
			  #aggiunta griglia
			  grid = QtGui.QGridLayout(widget) 
			  
			  #aggiunta radio
			  radio1 = QtGui.QRadioButton("Radio 1", widget)
              radio2 = QtGui.QRadioButton("Radio 2", widget)
              radio3 = QtGui.QRadioButton("Radio 3", widget)
			  #aggiunto pulsante (in questo caso, non svolge alcuna funzione perché non c'è uno slot ad accogliere un eventuale segnale)
			  button1 = QtGui.QPushButton('Chiudi finestra');
			  button2 = QtGui.QPushButton('Maggiori informazioni');
			  
			  #aggiungo i widget alla griglia, nella posizione che preferisco: in questo caso, ho immaginato una griglia 3x2
			  grid.addWidget(radio1, 0, 0)
              grid.addWidget(radio2, 1, 0)
              grid.addLayout(radio3, 2, 0)
              grid.addLayout(button1, 1, 0)
			  grid.addLayout(button2, 1, 1)
			  
			  widget.setLayout(grid)
			  self.setCentralWidget(widget)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(test.exec_())

