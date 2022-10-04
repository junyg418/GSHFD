from PySide6.QtWidgets import *
from CsvDataProcessingModule import get_link_to_list
import sys


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GSHFD')
        self.setFixedSize(300, 300)

        self.main_layout = QGridLayout()
        self.left_layout = QVBoxLayout()

        self.link_set_button = QPushButton('주소추가')
        self.change_account_button = QPushButton('계정번경')
        self.start_button = QPushButton('실행')

        self.link_scroll_area = QScrollArea()
        self.link_widget = LinkWidget()

        # 왼쪽 주소 창 -> 객체화 -> main_layout ( 0, 1 ) 위치 예정
        self._init_widget()
        self._init_layout()
        self.set_link_scroll_widget()

    def _init_widget(self):
        # link set button
        self.link_set_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.link_set_button.setMaximumHeight(40)

        # change account button
        self.change_account_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.change_account_button.setMaximumHeight(40)

        # start button
        self.start_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.start_button.setMaximumHeight(70)

    def _init_layout(self):
        self.setLayout(self.main_layout)

        self.main_layout.addLayout(self.left_layout, 0, 0)
        self.main_layout.addWidget(self.link_scroll_area, 0, 1)
        # main layout

        # left layout
        self.left_layout.addWidget(self.link_set_button)
        self.left_layout.addWidget(self.change_account_button)
        self.left_layout.addSpacerItem(QSpacerItem(1, 70))
        self.left_layout.addWidget(self.start_button)

    def set_link_scroll_widget(self):
        self.link_scroll_area.setWidget(self.link_widget)


def get_button_list() -> list:
    # TODO : 로컬에 저장되어있는 link 를 불러오는 작업 필요
    local_links = get_link_to_list()  # 변경 해야함
    button_list = list()

    for link in local_links:
        button = LinkRadioButton(link)
        button_list.append(button)
    return button_list


class LinkWidget(QWidget):
    def __init__(self):
        super().__init__()
        print('LinkWidget 생성')
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self._init_widget()

    def _init_widget(self):
        button_list = get_button_list()
        self.set_buttons_in_LinkWidget(button_list)
        self.button_group = self.init_LinkRadioButtonGroup(button_list)

    def set_buttons_in_LinkWidget(self, button_list: list) -> None:
        """
        위젯 내의 버튼을 추가해주는 메소드
        :param button_list:
            들어갈 버튼들의 리스트 -> list
        :return:
            None
        """
        for button in button_list:
            self.main_layout.addWidget(button)

    def init_LinkRadioButtonGroup(self, button_list: list) -> QButtonGroup:
        """
        LinkRadioButtonGroup 을 초기화 시키고, 반환하는 메소드
        :param button_list:
            Widget 에 들어갈 버튼들의 리스트 -> list
        :return:
            PySide6.QButtonGroup
        """
        return LinkRadioButtonGroup(button_list)


class LinkRadioButtonGroup(QButtonGroup):
    def __init__(self, button_list: list):
        super().__init__()
        self.setExclusive = False

        self.button_list = button_list

        self.set_buttongroup()

    def set_buttongroup(self):
        for button in self.button_list:
            self.addButton(button)


class LinkRadioButton(QRadioButton):
    def __init__(self, link: str):
        super().__init__()
        self.link = link

        self.setText(link)

    def get_link(self):
        return self.link


def open_main_widget():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())


open_main_widget()
