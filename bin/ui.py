from PySide6 import QtGui, QtCore, QtWidgets

#new ui powered by qt 

class main_ui(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()



        #elements
        t = QtWidgets.QDoubleSpinBox()
        txt = QtWidgets.QLabel(text="hey guys")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(t)
        self.layout.addWidget(txt)


#class for one mouth selector
class m_selector(QtWidgets.QWidget):

    def __init__(self, parent, image) -> None:
        super().__init__(parent=parent)

        self.layout = QtWidgets.QHBoxLayout()

        #create the image
        self.layout.addWidget(QtWidgets.QLabel().setPicture(QtGui.QPicture().load(image)))

        #buttons: x and select
        self.layout.addWidget(QtWidgets.QPushButton)

    def set_image(self):
        pass

        




if __name__ == "__main__":

    app = QtWidgets.QApplication()

    m = main_ui()
    m.resize(800, 600)
    m.show()

    app.exec()
    pass