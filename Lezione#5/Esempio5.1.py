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
              self.resize(400, 200)
              self.setWindowTitle('Finestra Principale')
			  
			  
test = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(test.exec_())

