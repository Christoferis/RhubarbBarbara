from PySide6 import QtGui, QtCore, QtWidgets
from os import path


#new ui powered by qt 

class main_ui(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        #elements

        self.layout = QtWidgets.QHBoxLayout(self)

        self.layout.addWidget(m_selector.mouthselector(self))


#class for one mouth selector -> just instance
class m_selector(QtWidgets.QWidget):

    #second constructor to actually create widget
    @staticmethod
    def mouthselector(parent):
        widget = QtWidgets.QWidget(parent=parent)

        widget.setLayout = QtWidgets.QVBoxLayout(widget)

        widget.mouthselector = list()

        for letter in ("A", "B", "C", "D", "E", "F", "G", "H", "X"):
            widget.mouthselector.append(m_selector(letter))
            
        #append to main ui
        for elem in widget.mouthselector:
            widget.layout().addWidget(elem)

        return widget

    #part widget constructor
    def __init__(self, type) -> None:
        super().__init__()

        self.image = f"bin/icons/lisa-{type}.png"

        #create the image
        self.preview = QtWidgets.QLabel(parent=self)
        self.preview.setPixmap(QtGui.QPixmap(self.image).scaled(80, 80, aspectMode=QtCore.Qt.KeepAspectRatio, mode=QtCore.Qt.SmoothTransformation))

        #buttons: x and select
        load_button = QtWidgets.QPushButton(text="Load", parent=self)
        x_button = QtWidgets.QPushButton(text="X", parent=self)

        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.LeftToRight, parent=self)
        self.layout.addWidget(QtWidgets.QLabel(parent=self, text=type))
        self.layout.addWidget(self.preview)
        self.layout.addWidget(load_button)
        self.layout.addWidget(x_button)
        
        
        load_button.clicked.connect(self.set_image)
        x_button.clicked.connect(self.set_image)

    def set_image(self):
        self.image = QtWidgets.QFileDialog.getOpenFileName()

        #set image as Icon Backgorund + scale to a normal size
        self.preview.setPixmap(QtGui.QPixmap(self.image[0]).scaled(80, 80, aspectMode=QtCore.Qt.KeepAspectRatio, mode=QtCore.Qt.SmoothTransformation))

        pass

    def remove_image(self):
        self.image = None

    def get_image(self):
        return self.image

class options(QtWidgets.QWidget):

    pass

#test routine
if __name__ == "__main__":

    app = QtWidgets.QApplication()

    m = main_ui()
    m.resize(1280, 720)
    m.show()

    app.exec()
    pass