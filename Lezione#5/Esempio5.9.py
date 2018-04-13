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
              self.setWindowTitle('Menu di prova')
			  #pulsante esci
              quit = QtGui.QAction("Quit", self)
              quit.setShortcut("Ctrl+Q")
              self.connect(quit, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
			  #separatore tra i bottoni
              sep = QtGui.QAction(self)
              sep.setSeparator(True)
			  #pulsante informazioni
              info = QtGui.QAction("Information", self)
              info.setShortcut("Ctrl+I")
              self.connect(info, QtCore.SIGNAL('clicked()'), self.mySlot)
			  #mostro toolbar
              self.statusBar().show()
			  #creo menu
              menu = self.menuBar()
              home = menu.addMenu('&Home')
              home.addAction(quit)
              home.addAction(sep)
              home.addAction(info)
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(test.exec_())

