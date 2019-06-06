import sys
from PyQt4.QtSql import *
from PyQt4.QtCore import *

class Connect(QObject):
    def __init__(self, parent=None):
        super(Connect, self).__init__(parent)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('customer.db')
        if not self.db.open():
            QMessageBox.critical(self.par, qApp.tr("Cannot open database"),
            qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."), QMessageBox.Cancel)
            qApp.exit()
        print("connected")

    def query_db(self):
        query = QSqlQuery()
        query.setForwardOnly(False)
        if query.exec_("SELECT accName, pin FROM users where id = 1;"):
            return query
        return False

    def close_db(self):
        if self.db.close():
            print("DB closed")


def main():
    app = QCoreApplication(sys.argv)
    obj = Connect()
    obj.query_db()
    app.exec_()

if __name__ == '__main__':
    main()