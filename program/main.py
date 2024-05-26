import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        symbCtrVar = 10

        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("fPwd")

        self.genpwdText = QLabel("Generate password")

        self.symbCtrText = QLabel("Symbols count: {ctr}".format(
            ctr = symbCtrVar))
        self.symbCtrSlider = QSlider(orientation=Qt.Orientation.Horizontal)
        self.symbCtrSlider.setMinimum(1)
        self.symbCtrSlider.setMaximum(20)
        self.symbCtrSlider.setValue(10)
        self.symbCtrSlider.valueChanged.connect(self.symbCtrSliderChange)

        Vertlayout = QVBoxLayout()
        Vertlayout.setSpacing(1)
        HorLayout = QHBoxLayout()

        Vertlayout.addWidget(self.genpwdText, alignment=Qt.AlignmentFlag.AlignCenter |
                         Qt.AlignmentFlag.AlignTop)
        HorLayout.addWidget(self.symbCtrText, alignment=Qt.AlignmentFlag.AlignTop |
                         Qt.AlignmentFlag.AlignLeft)
        HorLayout.addWidget(self.symbCtrSlider, alignment=Qt.AlignmentFlag.AlignTop |
                                                     Qt.AlignmentFlag.AlignRight)

        Vertlayout.addLayout(HorLayout)

        widget = QWidget()
        widget.setLayout(Vertlayout)
        self.setCentralWidget(widget)

    def symbCtrSliderChange(self, value):
        self.symbCtrVar = value
        self.symbCtrText.setText("Symbols count: {ctr}".format(
            ctr = self.symbCtrVar))



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()
