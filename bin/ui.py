from PySide6 import QtGui, QtCore, QtWidgets
from os import path


#new ui powered by qt 

class main_ui(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        #elements

        self.layout = QtWidgets.QVBoxLayout(self)

        self.mouthselector = list()

        for letter in ("A", "B", "C", "D", "E", "F", "G", "H", "X"):
            self.mouthselector.append(m_selector(self, letter))

        #append to main ui
        for elem in self.mouthselector:
            self.layout.addWidget(elem)


#class for one mouth selector -> just instance
class m_selector(QtWidgets.QWidget):

    def __init__(self, parent, type) -> None:
        super().__init__(parent=parent)

        self.image = None
        self.layout = QtWidgets.QHBoxLayout(parent=self)

        #create the image
        self.preview = QtWidgets.QLabel(parent=self)
        pic = QtGui.QPixmap(f"bin/icons/lisa-{type}.png").scaled(QtCore.QSize(80, 80), aspectMode=QtCore.Qt.KeepAspectRatio, mode=QtCore.Qt.SmoothTransformation)
        self.preview.setPixmap(pic)

        #buttons: x and select
        load_button = QtWidgets.QPushButton(text="Load", parent=self)
        x_button = QtWidgets.QPushButton(text="X", parent=self)

        self.layout.addWidget(self.preview)
        self.layout.addWidget(QtWidgets.QLabel(parent=self, text=type))
        self.layout.addWidget(x_button)
        self.layout.addWidget(load_button)
        
        load_button.clicked.connect(self.set_image)
        x_button.clicked.connect(self.set_image)

    def set_image(self):
        self.image = QtWidgets.QFileDialog.getOpenFileName()

        #set image as Icon Backgorund
        self.preview.setPixmap(QtGui.QPixmap(self.image))

        pass

    def remove_image(self):
        self.image = None

    def get_image(self):
        return self.image

        

#test routine
if __name__ == "__main__":

    app = QtWidgets.QApplication()

    m = main_ui()
    m.resize(1280, 720)
    m.show()

    app.exec()
    pass