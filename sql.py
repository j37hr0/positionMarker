import sqlite3


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('modules.db')
        self.conn_cursor = self.conn.cursor()

    def create_module_table(self):
        self.conn_cursor.execute("""CREATE TABLE if not exists modules(
            module_code TEXT PRIMARY KEY,
            module_name TEXT UNIQUE,
            module_year INT,
            module_archived BOOLEAN
        );""")

    def create_position_table(self):
        self.conn_cursor.execute("""CREATE TABLE if not exists positions(
            id INT PRIMARY KEY,
            module_code TEXT,
            position_name TEXT,
            position_page INT,
            position_datetime DATETIME
        );""")

    def create_position_entry(self, position_name, position_page, position_datetime):
        with self.conn:
            self.conn_cursor.execute("INSERT INTO positions VALUES (:position_name, :position_page, :position_datetime)", {'position_name': position_name, 'position_page': position_page, 'position_datetime': position_datetime})

    def create_module(self, module_name, module_code, module_year, module_archived):
        with self.conn:
            self.conn_cursor.execute("INSERT INTO modules VALUES (:module_name, :module_code, :module_year, :module_archived)", {'module_name': module_name, 'module_code': module_code, 'module_year': module_year, 'module_archived': module_archived})

    def get_module_by_name(self, module_name):
        self.conn_cursor.execute("SELECT * FROM modules WHERE module_name=:module_name", {'module_name': module_name})
        return self.conn_cursor.fetchall()

    def get_module_by_code(self, module_code):
        self.conn_cursor.execute("SELECT * FROM modules WHERE module_code=:module_code", {'module_code': module_code})
        return self.conn_cursor.fetchall()

    def get_module_by_year(self, module_year):
        self.conn_cursor.execute("SELECT * FROM modules WHERE module_year=:module_year", {'module_year': module_year})
        return self.conn_cursor.fetchall()

    def get_all_modules(self):
        self.conn_cursor.execute("SELECT module_name FROM modules where module_archived = 0")
        return self.conn_cursor.fetchall()

    def update_module_name(self, module_name, new_module_name):
        with self.conn:
            self.conn_cursor.execute("UPDATE modules SET module_name = :new_module_name WHERE module_name = :module_name", {'module_name': module_name, 'new_module_name': new_module_name})

    def update_module_code(self, module_code, new_module_code):
        with self.conn:
            self.conn_cursor.execute("UPDATE modules SET module_code = :new_module_code WHERE module_code = :module_code", {'module_code': module_code, 'new_module_code': new_module_code})

    def update_module_year(self, module_year, new_module_year):
        with self.conn:
            self.conn_cursor.execute("UPDATE modules SET module_year = :new_module_year WHERE module_year = :module_year", {'module_year': module_year, 'new_module_year': new_module_year})

    def update_module_archived(self, module_archived, new_module_archived):
        with self.conn:
            self.conn_cursor.execute("UPDATE modules SET module_archived = :new_module_archived WHERE module_archived = :module_archived", {'module_archived': module_archived, 'new_module_archived': new_module_archived})

    def get_module_entries_by_code(self, module_code):
        self.conn_cursor.execute("SELECT * FROM positions WHERE module_code=:module_code", {'module_code': module_code})
        return self.conn_cursor.fetchall()




#Create database connection
#conn = sqlite3.connect('modules.db')
#Create cursor
#conn_cursor = conn.cursor()