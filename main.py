import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
                             QMessageBox,QPlainTextEdit)
from PyQt5.QtGui import QIcon



class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()
        
    def init_UI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정
        
        self.btn1=QPushButton('Messsage',self) # 버튼 추가
        self.btn1.clicked.connect(self.activate_message) # 버튼 클릭 시 핸들러 함수 연결
        
        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addStretch(1) # 빈 공간
        vbox.addWidget(self.btn1) # 버튼 위치
        vbox.addStretch(1)
        
        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정
        
         
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) # 윈도 아이콘 추가
        self.resize(256,256)
        self.show()
        
    def activate_message(self): # 핸들러 함수 수정 : 메시지가 텍스트 에디트에 출력되도록
        #QMessageBox.information(self,"information", "Button clicked!")
        self.te1.appendPlainText("Butteon clicked!")
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
    