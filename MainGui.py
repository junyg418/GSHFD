from PySide6.QtWidgets import *
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('GSHFD')

        self.main_layout = QGridLayout()
        self.left_layout = QHBoxLayout(self.main_layout)

        self.link_set_button = QPushButton('주소추가', parent=self.left_layout)
        self.change_account_button = QPushButton('계정번경', parent=self.left_layout)
        self.start_button = QPushButton('실행', parent= self.left_layout)

        # 왼쪽 주소 창 -> 객체화 -> main_layout ( 0, 1 ) 위치 예정
        