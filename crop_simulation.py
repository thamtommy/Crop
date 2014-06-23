import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *

class CropWindow(QMainWindow):

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

    def create_select_crop_layout(self):
        #this is the initial layout of the window - to select the crop type

        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop", ("Wheat", "Potato"))
        self.instantiate_button = QPushButton("Create Crop")

        #create layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec

if __name__ == "__main__":
    main()
