import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def window():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QHBoxLayout()

    textlabel = QLabel(window)
    textlabel.setText("Kotak Angka")
    textlabel.move(25, 50)

    for i in range(5):
        button = QPushButton(str(i + 1))
        layout.addWidget(button)
        button.setGeometry(50, 50, 100, 50)
        button.setFont(QFont('Arial', 24))
        button.setStyleSheet("font-size: 24pt; background-color: grey; color: white")

    # __menentukan ukuran window, + title dan menampilkan
    window.setGeometry(100, 100, 200, 200)
    window.setWindowTitle("PyQt5 Example")
    window.setLayout(layout)
    window.setStyleSheet("background-color: pink")
    window.show()
    app.exec_()


if __name__ == '__main__':
    window()
