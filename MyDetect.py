# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, gui

import detect, time

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    while not ui.select:
        app.exec_()
    path = ui.path_img
    view = ui.view_img
    detect.start(path, view)
