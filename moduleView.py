# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moduleView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_module_view(object):
    def setupUi(self, module_view):
        module_view.setObjectName("module_view")
        module_view.resize(431, 329)
        self.tableView = QtWidgets.QTableView(module_view)
        self.tableView.setGeometry(QtCore.QRect(25, 80, 371, 192))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(module_view)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(module_view)
        self.label.setGeometry(QtCore.QRect(190, 40, 81, 21))
        self.label.setObjectName("label")

        self.retranslateUi(module_view)
        QtCore.QMetaObject.connectSlotsByName(module_view)

    def retranslateUi(self, module_view):
        _translate = QtCore.QCoreApplication.translate
        module_view.setWindowTitle(_translate("module_view", "Form"))
        self.pushButton.setText(_translate("module_view", "New Entry"))
        self.label.setText(_translate("module_view", "CurrentModule"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    module_view = QtWidgets.QWidget()
    ui = Ui_module_view()
    ui.setupUi(module_view)
    module_view.show()
    sys.exit(app.exec_())
