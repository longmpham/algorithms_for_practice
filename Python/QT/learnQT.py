import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# https://www.youtube.com/watch?v=92zx_U9Nzf4
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # boiler plate init
        self.setWindowTitle("My First GUI")
        self.setGeometry(1600,300,500,500)
        

def main():
    app = QApplication(sys.argv) # boiler plate init
    window = MainWindow() # call your class which is your GUI app!
    window.show() # window is hidden by default
    sys.exit(app.exec_()) # this makes sure program exits when we close the window
    


if __name__ == "__main__":
    main()