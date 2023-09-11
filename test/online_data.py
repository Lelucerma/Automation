import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer

class TextUpdater(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('文本更新示例')
        self.setGeometry(100, 100, 400, 200)

        self.text1_label = QLabel('文本1:')
        self.text2_label = QLabel('文本2:')

        layout = QVBoxLayout()
        layout.addWidget(self.text1_label)
        layout.addWidget(self.text2_label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.timer.start(1000)  # 1秒钟更新一次文本

    def update_text(self):
        # 这里可以替换为你自己的文本数据生成逻辑
        text1 = f'文本1更新时间：{time.strftime("%H:%M:%S")}'
        text2 = f'文本2更新时间：{time.strftime("%H:%M:%S")}'

        self.text1_label.setText(text1)
        self.text2_label.setText(text2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextUpdater()
    window.show()
    sys.exit(app.exec())
