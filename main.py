from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import sys
import sqlite3
import newModule
import mainUI
import sql
import newEntry
import newModule

sql_conn = sql.Connection()
sql_conn.create_module_table()
sql_conn.create_position_table()
all_modules = sql_conn.get_all_modules()

def create_newmodule_window(MainWindow):
    Form = QtWidgets.QWidget()
    newMod = newModule.Ui_Form()
    newMod.setupUi(Form)
    MainWindow.second_window = Form
    Form.setWindowTitle("New Module")
    Form.setFocus()
    newMod.mod_name_input.setPlaceholderText("Enter module name..")
    newMod.mod_code_input.setPlaceholderText("Enter module code..")
    newMod.mod_year_input.setPlaceholderText("Enter module year..")
    newMod.new_mod_cancel.clicked.connect(lambda: MainWindow.second_window.close())
    MainWindow.second_window.show()
    Form.update()
    newMod.new_mod_confirm.clicked.connect(lambda: sql_conn.create_module(newMod.mod_name_input.toPlainText(), newMod.mod_code_input.toPlainText(), newMod.mod_year_input.toPlainText(), False))
    ui.module_list.clear()
    ui.module_list.addItems([str(module).strip("',)(") for module in all_modules])
    newMod.new_mod_confirm.clicked.connect(lambda: MainWindow.second_window.close())


def select_module():
    current_mod_entries = sql_conn.get_module_entries_by_code(ui.module_list.currentItem().text())
    ui.module_list.clear()
    ui.module_list.addItems([str(module).strip("',)(") for module in current_mod_entries])

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mainUI.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
MainWindow.setWindowTitle("Module Position Manager")
ui.menuNew.triggered.connect(lambda: create_newmodule_window(mainUI.Ui_MainWindow))
ui.select_btn.clicked.connect(lambda: select_module())
ui.module_list.addItems([str(module).strip("',)(") for module in all_modules])
sys.exit(app.exec_())




