from PySide6.QtWidgets import *
import sys


class AddUserWidget(QWidget):
    def __init__(self):
        super(AddUserWidget, self).__init__()
        self.setWindowTitle('주소 추가')
        self.main_layout = QGridLayout()

        self.descriptive_label = QLabel()
        self.add_link_lineedit = QLineEdit()
        self.accept_button = QPushButton('추가')

        self._init_widget()
        self._init_ui()

    def _init_ui(self):
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.descriptive_label, 0, 0)
        self.main_layout.addWidget(self.add_link_lineedit, 1, 0, 1, 4)
        self.main_layout.addWidget(self.accept_button, 2, 3, 1, 1)

    def _init_widget(self):
        self.descriptive_label.setText('형식에 맞추어 작성해주세요. form: https://youtube.com')

        self.accept_button.clicked.connect(self.clicked_accept_button)
    def get_written_link(self):
        return self.add_link_lineedit.text()
    
    def clicked_accept_button(self):
        # TODO 중복 오류, 형식오류 검사
        self.close()

def open_AddUserWidget():
    widget = AddUserWidget()
    widget.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AddUserWidget()
    widget.show()
    sys.exit(app.exec())