from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(432, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Allzapisi = QtWidgets.QPushButton(self.centralwidget)
        self.Allzapisi.setGeometry(QtCore.QRect(90, 40, 261, 41))
        self.Allzapisi.setStyleSheet("")
        self.Allzapisi.setObjectName("Allzapisi")
        self.findeFIO = QtWidgets.QPushButton(self.centralwidget)
        self.findeFIO.setGeometry(QtCore.QRect(90, 90, 261, 31))
        self.findeFIO.setObjectName("findeFIO")
        self.findeName = QtWidgets.QPushButton(self.centralwidget)
        self.findeName.setGeometry(QtCore.QRect(90, 130, 261, 31))
        self.findeName.setObjectName("findeName")
        self.findeNomer = QtWidgets.QPushButton(self.centralwidget)
        self.findeNomer.setGeometry(QtCore.QRect(90, 170, 261, 31))
        self.findeNomer.setObjectName("findeNomer")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(90, 210, 261, 31))
        self.create.setObjectName("create")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(90, 250, 261, 31))
        self.change.setObjectName("change")
        self.delet = QtWidgets.QPushButton(self.centralwidget)
        self.delet.setGeometry(QtCore.QRect(90, 290, 261, 31))
        self.delet.setObjectName("delet")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(90, 330, 261, 31))
        self.exit.setObjectName("exit")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, -20, 441, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 154, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 154, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 204, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 154, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.graphicsView.setPalette(palette)
        self.graphicsView.setTabletTracking(False)
        self.graphicsView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet("selection-background-color: rgb(186, 154, 200);\n"
"background-color: rgb(192, 204, 255);")
        self.graphicsView.setInteractive(False)
        self.graphicsView.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.graphicsView.raise_()
        self.Allzapisi.raise_()
        self.findeFIO.raise_()
        self.findeName.raise_()
        self.findeNomer.raise_()
        self.create.raise_()
        self.change.raise_()
        self.delet.raise_()
        self.exit.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????????"))
        self.Allzapisi.setText(_translate("MainWindow", "???????????????? ?????? ????????????"))
        self.findeFIO.setText(_translate("MainWindow", "?????????? ?????????? ???? ??????????????"))
        self.findeName.setText(_translate("MainWindow", "?????????? ?????????? ???? ??????????"))
        self.findeNomer.setText(_translate("MainWindow", "?????????? ?????????? ???? ???????????? ????????????????"))
        self.create.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.change.setText(_translate("MainWindow", "???????????????? ????????????"))
        self.delet.setText(_translate("MainWindow", "?????????????? ????????????"))
        self.exit.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.graphicsView.setToolTip(_translate("MainWindow", "<html><head/><body><p>file:///C:/Users/DNS/Downloads/wq7XKSzSNe9q_ga3sUTm9lNKresa55LpO_QOisJtRSpZmo4PDZcP8ftbitrz0XSfUxUOim_ctj8wpd3Okg14kF1s.jpg</p></body></html>"))
        self.label.setText(_translate("MainWindow", "???????????????????? ???????????????????? 2.0"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    self.add_functions()

import user_interface as ui
import generator as gen
import crud

crud.init_data_base('base_phone.csv')
ui.ls_menu()

    

def add_function(self):
    self.Allzapisi.cliced.connect()
    self.findeFIO.cliced.connect()
    self.findeName.cliced.connect()
    self.findeNomer.cliced.connect()
    self.create.cliced.connect()
    self.exit.cliced.connect(exit)