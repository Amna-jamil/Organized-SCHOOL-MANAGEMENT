import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Test Window")
window.resize(300, 200)
window.show()

sys.exit(app.exec_())
