from PyQt5.Qt import *
from resource.mainFrom import Ui_Form


class MainPane(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainPane()
    # window.setWindowTitle('登录')
    window.show()
    sys.exit(app.exec())