import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow

class ExpenceTracker(QMainWindow):
    def __init__(self):
        super(ExpenceTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenceTracker()
    window.show()

    sys.exit(app.exec())