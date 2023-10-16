import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(800,800))
        self.move(0, 0)
        
        self.setStatusBar(QStatusBar(self))
        self.status = self.statusBar()
        self.status.addPermanentWidget(QLabel("(c) ApplicationName"))
        self.status.showMessage("hello", 3000)

        self.btn_0 = QPushButton("Click 0", self)
        self.btn_1 = QPushButton("Click 1", self)
        self.btn_2 = QPushButton("Click 2", self)
        
        layout = QHBoxLayout()
        layout.addWidget(self.btn_0)
        layout.addWidget(self.btn_1)
        layout.addWidget(self.btn_2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.btn_0.clicked.connect(self.action_btn_0)
        self.btn_1.clicked.connect(self.action_btn_1)
        self.btn_2.clicked.connect(self.action_btn_2)


    def action_btn_0(self):
        print("heelo")
        QMessageBox.information(self, "titre", "TEXT")

    def action_btn_1(self):
        print("btn 1 clicked")

    def action_btn_2(self):
        self.status.showMessage("BTN 2 CLICKED", 10000)
        
app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("My window title")
window.show()

app.exec()
