import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(1000,1000))
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        btn = QPushButton('Bouton 1')
        layout.addWidget(btn, 0, 0)

        layout.addWidget(QPushButton('Button2'), 1, 0)
        layout.addWidget(QLabel('label'), 2, 0)
        layout.addWidget(QTextEdit(),3, 0)
        layout.addWidget(QCalendarWidget(), 4, 0)
        
        lcd_number = QLCDNumber()
        lcd_number.setMinimumHeight(50)
        lcd_number.display(5123)
        layout.addWidget(lcd_number, 5, 0)

        form_layout = QFormLayout()
        layout.addLayout(form_layout, 0, 1, 5, 1)
        
        line_edit = QLineEdit()
        line_edit.setText('Richnou')
        form_layout.addRow('Line Edit:', line_edit)

        form_layout.addRow('Text Edit:', QTextEdit())
        form_layout.addRow('Text Edit:', QTextEdit())

        form_layout.addRow('Time:', QTimeEdit())
        form_layout.addRow('Date:', QDateEdit())
        form_layout.addRow('Date Time:', QDateTimeEdit())

        form_layout.addRow('', QCheckBox('Signup ?'))
        colors = ['Rouge', 'Vert', 'Jaune', 'Bleu']
        color_group = QButtonGroup(self)
        color_layout = QHBoxLayout()
        for index, color in enumerate(colors):
            r = QRadioButton(color)
            color_group.addButton(r)
            color_layout.addWidget(r)
            if index == 0:
                r.setChecked(True)
        form_layout.addRow('Couleurs:', color_layout)
        
        combo = QComboBox()
        combo.addItem("Chouette")
        combo.addItem("Croissant")
        combo.addItem("Chocolatine")
        combo.addItems(colors)
        combo.setCurrentIndex(0)
        form_layout.addRow('Liste', combo)


app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("My window title")
window.show()

app.exec()
