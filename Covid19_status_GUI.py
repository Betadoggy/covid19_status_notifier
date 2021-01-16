import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Covid-19 Status')
        self.setWindowIcon(QIcon()) # 아이콘 파일
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 객체를 생성해야함
    ex = MyApp()
    sys.exit(app.exec_())