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

        self.image = None
        self.layout = QtWidgets.QHBoxLayout(parent=self)

        #create the image
        self.preview = QtWidgets.QLabel(parent=self).setPicture(QtGui.QPicture().load(image))

        #buttons: x and select
        load_button = QtWidgets.QPushButton(text="Load", parent=self)
        x_button = QtWidgets.QPushButton(text="X", parent=self)

        self.layout.addWidget(self.preview)
        self.layout.addWidget(QtWidgets.QLabel(parent=self, text="A"))
        self.layout.addWidget(load_button)
        self.layout.addWidget(x_button)
        
        load_button.clicked.connect(self.set_image)


    
    @QtCore.Slot
    def set_image(self):
        self.image = QtWidgets.QFileDialog.getOpenFileName()

        #set image as Icon Backgorund
        self.preview.setPicture(QtGui.QPicture().load(self.image))

        pass

    def remove_image(self):
        self.image = None

    def get_image(self):
        return self.image

        




if __name__ == "__main__":

    app = QtWidgets.QApplication()

    m = main_ui()
    m.resize(800, 600)
    m.show()

    app.exec()
    pass