from PyQt5 import QtCore, QtGui, QtWidgets
from data_karyawan import *
from fungsi_pengurutan import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 599)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 781, 551))
        self.frame.setToolTipDuration(-1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 551, 531))
        self.listWidget.setObjectName("listWidget")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 20, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 311, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)

        header = ['NIP', 'Nama Karyawan', 'Jabatan']
        self.tableWidget.setHorizontalHeaderLabels(header)

        for i in range(len(data_final)):
            row_kosong = self.tableWidget.rowCount()

            self.tableWidget.insertRow(row_kosong)
            self.tableWidget.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.tableWidget.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.tableWidget.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

        

        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(30, 120, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.label_2.setObjectName("label_2")

        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 120, 101, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 120, 82, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(46, 500, 191, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 500, 25, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 120, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 498, 75, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 80, 551, 20))
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 551, 20))
        self.line_2.setLineWidth(4)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(self.action_pengurutan)
        self.pushButton.clicked.connect(self.action_cari)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def action_pengurutan(self):

        if self.radioButton.isChecked():
            pengurut_nip(data_final)
        elif self.radioButton_2.isChecked():
            pengurut_pegawai(data_final)
        elif self.radioButton_3.isChecked():
            pengurut_jabatan(data_final)

        self.tableWidget.setRowCount(0)
        
        for i in range(len(data_final)):
            row_kosong = self.tableWidget.rowCount()

            self.tableWidget.insertRow(row_kosong)
            self.tableWidget.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.tableWidget.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.tableWidget.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

    def action_cari(self):

        target = self.lineEdit.text()
        self.tableWidget.setRowCount(0)
        
        for i in range(len(data_final)):
            if target in data_final[i][0]:
                while data_final[i][0] == self.lineEdit.text():
                    row_kosong = self.tableWidget.rowCount()

                    self.tableWidget.insertRow(row_kosong)
                    self.tableWidget.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                    self.tableWidget.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                    self.tableWidget.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
                    break
                
            elif target in data_final[i][1]:
                while data_final[i][1] == self.lineEdit.text():
                    row_kosong = self.tableWidget.rowCount()

                    self.tableWidget.insertRow(row_kosong)
                    self.tableWidget.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                    self.tableWidget.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                    self.tableWidget.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
                    break
                
            elif target in data_final[i][2]:
                while data_final[i][2] == self.lineEdit.text():
                    row_kosong = self.tableWidget.rowCount()

                    self.tableWidget.insertRow(row_kosong)
                    self.tableWidget.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                    self.tableWidget.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                    self.tableWidget.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
                    break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DATA KARYAWAN RUMAH SAKIT"))
        self.radioButton.setText(_translate("MainWindow", "NIP"))
        self.label_2.setText(_translate("MainWindow", "Urut berdasarkan :"))
        self.radioButton_2.setText(_translate("MainWindow", "Nama Pegawai"))
        self.radioButton_3.setText(_translate("MainWindow", "Jabatan"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "search"))
        self.label_3.setText(_translate("MainWindow", "Cari"))
        self.pushButton_2.setText(_translate("MainWindow", "Urutkan"))
        self.pushButton.setText(_translate("MainWindow", "Cari"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


