from PySide6.QtWidgets import QApplication
from bin.ui import main_ui

def main():
    #create new Application
    app = QApplication()

    #new ui
    ui = main_ui()
    ui.resize(1280, 720)
    ui.show()

    app.exec()
    pass



if __name__ == "__main__":
    main()