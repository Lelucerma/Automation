import auto_ui
import motor
import sys
from PySide6.QtWidgets import QApplication

def pump_ui():
    
    app = QApplication([])
    stats = auto_ui.Stats()
    stats.ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    motor.ser_open('com5')
    pump_ui()
    motor.ser_close()
