from PySide6.QtWidgets import *
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('GSHFD')

        self.main_layout = QGridLayout()
        self.left_layout = QHBoxLayout()

        self.link_set_button = QPushButton('주소추가')
        self.change_account_button = QPushButton('계정번경')
        self.start_button = QPushButton('실행')

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
        self.left_layout.addWidget(self.link_set_button)
        self.left_layout.addWidget(self.change_account_button)
        self.left_layout.addSpacerItem(QSpacerItem(1,100))
        self.left_layout.addWidget(self.start_button)
        
    
    def set_link_scroll_widget(self):
        self.link_scroll_area.setWidget(self.link_widget)


class LinkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setlayout(self.layout)
        
        self.set_Linkwidget()
        
    def set_Linkwidget(self) -> None:
        """
        위젯의 기초 설정해주는 함수
        :return:
            None
        """
        button_list = self.get_button_list()
        LinkRadioButtonGroup(button_list)
    
    def set_button_widget(self):
        """
        버튼들을 위젯에 추가하는 함수
        """
        button_list = self.get_button_list()
        for button in button_list:
            self.addwidget(button) #TODO 이부분 오류 검사 확인 필요
            
        
    def get_button_list(self) -> list:
        """
        리스트에 포함된 QRadioButton 들의 나열하는 버튼을 반환하는 함수
        """
        # TODO : 로컬에 저장되어있는 link 를 불러오는 작업 필요
        local_links = list() # 변경 해야함
        button_list = list()

        for link in local_links:
            button = LinkRadioButton(link)
            button_list.append(button)
        return button_list


class LinkRadioButtonGroup(QButtonGroup):
    def __init__(self, button_list:list):
        super().__init__()
        self.setExclusive = False

        self.button_list = button_list

        self.set_buttongroup()

    def set_buttongroup(self):
        for button in self.button_list:
            self.addButton(button)

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
    sys.exit(app.exec_())

open_main_widget()
