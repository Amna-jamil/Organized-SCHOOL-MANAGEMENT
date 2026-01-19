# main.py
import sys
from PyQt5.QtWidgets import QApplication
from menu import MenuWindow

def main():
    app = QApplication(sys.argv)
    win = MenuWindow()
    win.show()
    print("✅ GUI Started...")   # debug ke liye
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

