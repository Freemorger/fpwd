import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QVBoxLayout, QLabel, QSlider, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Alphabets():
    def __init__(self):
      self.AllLeters = {'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 
                      'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 
                      'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 
                      'w', 'X', 'x', 'Y', 'y', 'Z', 'z'}

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        self.symbCtrVar = 10
        self.generatedPwd = ""

        super(MainWindow, self).__init__()
        self.InitUI()
    
    def InitUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("fPwd pre-v0.1")

        Vertlayout = QVBoxLayout()
        #Vertlayout.setContentsMargins(0, 0, 0, 0)  # Adjust the margins
        #Vertlayout.setSpacing(0)  # Adjust the spacing

        HorLayout = QHBoxLayout()

        self.genpwdText = QLabel("Generate password")
        Vertlayout.addWidget(self.genpwdText, alignment=Qt.AlignmentFlag.AlignCenter |
                         Qt.AlignmentFlag.AlignTop)

        self.symbCtrText = QLabel("Symbols count: {ctr}".format(
            ctr = self.symbCtrVar))
        HorLayout.addWidget(self.symbCtrText, alignment=Qt.AlignmentFlag.AlignTop |
                         Qt.AlignmentFlag.AlignLeft)
        
        self.symbCtrSlider = QSlider(orientation=Qt.Orientation.Horizontal)
        self.symbCtrSlider.setMinimum(1)
        self.symbCtrSlider.setMaximum(20)
        self.symbCtrSlider.setValue(10)
        self.symbCtrSlider.valueChanged.connect(self.symbCtrSliderChange)
        HorLayout.addWidget(self.symbCtrSlider, alignment=Qt.AlignmentFlag.AlignTop |
                                                     Qt.AlignmentFlag.AlignRight)
        
        self.genButton = QPushButton("Generate")
        Vertlayout.addWidget(self.genButton, alignment= Qt.AlignmentFlag.AlignBottom |
                             Qt.AlignmentFlag.AlignCenter)

        
        

        Vertlayout.addLayout(HorLayout)

        widget = QWidget()
        widget.setLayout(Vertlayout)
        self.setCentralWidget(widget)
    
    def symbCtrSliderChange(self, value):
        self.symbCtrVar = value
        self.symbCtrText.setText("Symbols count: {ctr}".format(
            ctr = self.symbCtrVar))
    
    def generatePwd(self):
      self.generatedPwd = ""



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()
