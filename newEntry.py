# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEntry.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.current_text_new = QtWidgets.QTextEdit(Form)
        self.current_text_new.setGeometry(QtCore.QRect(140, 50, 104, 71))
        self.current_text_new.setObjectName("current_text_new")
        self.current_number_new = QtWidgets.QTextEdit(Form)
        self.current_number_new.setGeometry(QtCore.QRect(260, 50, 104, 31))
        self.current_number_new.setObjectName("current_number_new")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.module_options_new = QtWidgets.QComboBox(Form)
        self.module_options_new.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.module_options_new.setObjectName("module_options_new")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Current Text"))
        self.label_2.setText(_translate("Form", "Page Number"))
        self.label_3.setText(_translate("Form", "Module"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
