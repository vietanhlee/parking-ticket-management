# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1398, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(30, 100, 601, 431))
        self.label_main.setStyleSheet("border: 2px solid black")
        self.label_main.setText("")
        self.label_main.setObjectName("label_main")
        self.text_header = QtWidgets.QLabel(self.centralwidget)
        self.text_header.setGeometry(QtCore.QRect(440, 10, 621, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.text_header.setFont(font)
        self.text_header.setStyleSheet("border: 6px solid yellow")
        self.text_header.setObjectName("text_header")
        self.label_in = QtWidgets.QLabel(self.centralwidget)
        self.label_in.setGeometry(QtCore.QRect(240, 540, 391, 261))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_in.setFont(font)
        self.label_in.setStyleSheet("border: 2px solid black")
        self.label_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_in.setObjectName("label_in")
        self.button_check_in = QtWidgets.QPushButton(self.centralwidget)
        self.button_check_in.setGeometry(QtCore.QRect(1060, 690, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.button_check_in.setFont(font)
        self.button_check_in.setObjectName("button_check_in")
        self.label_digits = QtWidgets.QLabel(self.centralwidget)
        self.label_digits.setGeometry(QtCore.QRect(990, 290, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_digits.setFont(font)
        self.label_digits.setStyleSheet("border: 4px solid black")
        self.label_digits.setAlignment(QtCore.Qt.AlignCenter)
        self.label_digits.setObjectName("label_digits")
        self.button_check_out = QtWidgets.QPushButton(self.centralwidget)
        self.button_check_out.setGeometry(QtCore.QRect(1060, 750, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.button_check_out.setFont(font)
        self.button_check_out.setObjectName("button_check_out")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(990, 470, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("border: 4px solid black")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setEnabled(True)
        self.label_price.setGeometry(QtCore.QRect(990, 560, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_price.setAutoFillBackground(False)
        self.label_price.setStyleSheet("border: 4px solid black")
        self.label_price.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.label_price.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price.setObjectName("label_price")
        self.label_plate = QtWidgets.QLabel(self.centralwidget)
        self.label_plate.setGeometry(QtCore.QRect(990, 140, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_plate.setFont(font)
        self.label_plate.setStyleSheet("border: 4px solid black")
        self.label_plate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_plate.setObjectName("label_plate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 170, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 480, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 570, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1170, 10, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(770, 390, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setEnabled(True)
        self.label_status.setGeometry(QtCore.QRect(990, 380, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_status.setAutoFillBackground(False)
        self.label_status.setStyleSheet("border: 4px solid black")
        self.label_status.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.label_status.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 650, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1398, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_header.setText(_translate("MainWindow", "Hệ thống nhận diện biển số trạm thu vé"))
        self.label_in.setText(_translate("MainWindow", "Không nhận dạng được"))
        self.button_check_in.setText(_translate("MainWindow", "Xác nhận vào"))
        self.label_digits.setText(_translate("MainWindow", "Không nhận diện được"))
        self.button_check_out.setText(_translate("MainWindow", "Xác nhận ra"))
        self.label_time.setText(_translate("MainWindow", "18 : 30 : 20"))
        self.label_price.setText(_translate("MainWindow", "3000 VND"))
        self.label_plate.setText(_translate("MainWindow", "Không nhận thấy"))
        self.label.setText(_translate("MainWindow", " Ảnh biển số:"))
        self.label_2.setText(_translate("MainWindow", "Đọc biển:"))
        self.label_3.setText(_translate("MainWindow", "Thời gian vào bến:"))
        self.label_4.setText(_translate("MainWindow", "Giá vé:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Giá vé gửi xe</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sáng: 3000 VND</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Tối: 5000 VND</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Trạng thái:"))
        self.label_status.setText(_translate("MainWindow", "Đã vào bến"))
        self.label_6.setText(_translate("MainWindow", "Ảnh lúc vào:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
