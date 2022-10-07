from PySide6.QtWidgets import *

class ErrorDialog(QDialog):
    def __init__(self, error_message: str):
        super().__init__()
        self.error_message = error_message

        self.setWindowTitle('오류 메세지')
        self.setFixedSize(270, 130)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.message_label = QLabel()
        self.close_button = QPushButton('확인')

        self._init_ui()
        self._init_widget()
        self.show()

    def _init_ui(self):
        self.main_layout.addWidget(self.message_label, 0, 0, 1, 3)
        self.main_layout.addWidget(self.close_button, 1, 2)

    def _init_widget(self):
        # ----- message_label -----
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setText(self.error_message)

        # ----- close_button -----
        self.close_button.clicked.connect(self.click_close_button)

    def click_close_button(self):
        self.close()