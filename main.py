##TODO Link newEntry and newModule
##Refactor a bunch of the GUI refresh stuff


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import sys
import sqlite3
import newModule
import mainUI
import sql
import newEntry
import moduleView

try:
    sql_conn = sql.Connection()
    sql_conn.create_position_table()
    sql_conn.create_module_table()
    all_modules = sql_conn.get_all_modules()
    top_positions = sql_conn.get_top_positions()
except Exception as e:
    print("Error connecting to database", e)
    sys.exit(1)

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


def select_module(MainWindow):
    if ui.module_list.selectedItems() != 0:
        current_mod = sql_conn.get_module_by_name(ui.module_list.currentItem().text())
        current_mod_entries = sql_conn.get_module_entries_by_code(current_mod[0][1])
        Form = QtWidgets.QWidget()
        selectedMod = moduleView.Ui_module_view()
        selectedMod.setupUi(Form)
        MainWindow.fourth_window = Form
        Form.setWindowTitle("Module View")
        Form.setFocus()
        selectedMod.label.setText(current_mod[0][1])
        selectedMod.module_entry_list.addItems([str(entry).strip("',)(") for entry in current_mod_entries])
        selectedMod.new_entry_specific_btn.clicked.connect(lambda: create_new_position(mainUI.Ui_MainWindow, current_mod[0][1]))

        MainWindow.fourth_window.show()

def create_new_position(MainWindow, default_module=None):
    Form = QtWidgets.QWidget()
    newPositionEntry = newEntry.Ui_Form()
    newPositionEntry.setupUi(Form)
    MainWindow.third_window = Form
    Form.setWindowTitle("New Entry")
    Form.setFocus()
    newPositionEntry.module_options_new.addItems([str(module).strip("',)(") for module in all_modules])
    if default_module != None:
        newPositionEntry.module_options_new.setCurrentText(default_module)
    newPositionEntry.cancel_new_entry_btn.clicked.connect(lambda: MainWindow.third_window.close())
    newPositionEntry.save_new_entry_btn.clicked.connect(lambda: sql_conn.create_position_entry(newPositionEntry.module_options_new.currentText(), newPositionEntry.current_text_new.toPlainText(), int(newPositionEntry.current_number_new.toPlainText())))
    MainWindow.third_window.show()
    newPositionEntry.save_new_entry_btn.clicked.connect(lambda: MainWindow.third_window.close())

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mainUI.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
MainWindow.setWindowTitle("Module Position Manager")
ui.menuNew.triggered.connect(lambda: create_newmodule_window(mainUI.Ui_MainWindow))
ui.create_position_btn.clicked.connect(lambda: create_new_position(mainUI.Ui_MainWindow))
ui.select_btn.clicked.connect(lambda: select_module(mainUI.Ui_MainWindow))
ui.module_list.addItems([str(module).strip("',)(") for module in all_modules])
ui.top_positions_table.addItems([str(position).strip("',)(") for position in top_positions])
sys.exit(app.exec_())




