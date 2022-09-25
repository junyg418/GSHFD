from PySide6.QtWidgets import *
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('GSHFD')

        self.main_layout = QGridLayout()
        self.left_layout = QHBoxLayout()

        self.link_set_button = QPushButton('주소추가', parent=self.left_layout)
        self.change_account_button = QPushButton('계정번경', parent=self.left_layout)
        self.start_button = QPushButton('실행', parent= self.left_layout)

        self.link_scroll_area = QScrollArea()
        self.link_widget = LinkWidget()
        
        # 왼쪽 주소 창 -> 객체화 -> main_layout ( 0, 1 ) 위치 예정
        self._init_widget()
        self._init_layout()

    def _init_widget(self):
        # linke set button
        self.link_set_button.setFixedSize(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # change account button
        self.change_account_button.setFixedSize(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # start button
        self.start_button.setFixedSize(QSizePolicy.Minimum, QSizePolicy.Minimum)
    
    def _init_layout(self):
        # main layout
        self.main_layout.addLayout(self.left_layout, 0, 0)
        self.main_layout.addWidget(self.link_scroll_area, 1, 0)

        # left layout
        self.left_layout.addWidget(self.link_set_buttonm, 1)
        self.left_layout.addWidget(self.change_account_button, 1)
        self.left_layout.addSpacerItem(QSpacerItem(1,100))
        self.left_layout.addWidget(self.start_button, 1)
        
    
    def set_link_scroll_widget(self):
        self.link_scroll_area.setWidget(self.link_widget)


class LinkWidget(QWidget):
    def __init__(self):
        super().__init__()

class LinkRadioButtonGroup(QButtonGroup):
    def __init__(self):
        super().__init__()
        self.setExclusive = False

        self.set_buttongroup()
    def set_buttongroup(self):
        # TODO : 로컬에 저장되어있는 link 를 불러오는 작업 필요
        pass
    
    def get_buttons(self):
        # TODO 선택된 버튼이 여러개일 떄는 어떻게 값이 나오는지 예외처리 -> 2개면 리스트려나
        buttons = self.checkedButton


class LinkRadioButton(QRadioButton):
    def __init__(self, link:str):
        super().__init__()
        self.link = link

        self.setText(link)

    def get_link(self):
        return self.link




def open_main_widget():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_)

open_main_widget()