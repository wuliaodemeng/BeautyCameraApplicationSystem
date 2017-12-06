from BeautyGUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from whiten import BalanceColor
from grind import mopi
import sys
import cv2
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    filename = ""
    cur_image = None
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.find_files.clicked.connect(self.open_file)
        self.whiten.clicked.connect(self.whiten_click)
        self.grind.clicked.connect(self.grind_click)
        self.filter.clicked.connect(self.filter_click)
        self.complete_button.clicked.connect(self.complete_button_click)

    def open_file(self):
        file = QFileDialog.getOpenFileName(self, 'open file', sys.path[0])
        self.pic_path.setText(str(file[0]))
        self.filename = str(file[0])
        self.cur_image = self.load_image(self.filename)
        png = QtGui.QPixmap(file[0])
        self.origin_image_label.setPixmap(png.scaled(self.origin_image_label.size()))

    # 解决中文路径问题
    def load_image(self, file_path):
        cv_image = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        return cv_image

    def complete_button_click(self):
        cv2.imwrite('beauty_pic.png', self.cur_image)

    def whiten_click(self):
        whiten_image = self.whiten_func(self.cur_image)
        cv2.imwrite('temp_pic.png', self.cur_image)
        png = QtGui.QPixmap('temp_pic.png')
        os.remove('temp_pic.png')
        self.beauty_image_label.setPixmap(png.scaled(self.beauty_image_label.size()))
        self.cur_image = whiten_image

    def grind_click(self):
        grind_image = self.grind_func(self.cur_image)
        cv2.imwrite('temp_pic.png', self.cur_image)
        png = QtGui.QPixmap('temp_pic.png')
        os.remove('temp_pic.png')
        self.beauty_image_label.setPixmap(png.scaled(self.beauty_image_label.size()))
        self.cur_image = grind_image

    def filter_click(self):
        filter_image = self.filter_func(self.cur_image)
        cv2.imwrite('temp_pic.png', self.cur_image)
        png = QtGui.QPixmap('temp_pic.png')
        os.remove('temp_pic.png')
        self.beauty_image_label.setPixmap(png.scaled(self.beauty_image_label.size()))
        self.cur_image = filter_image

    def whiten_func(self, image):
        return BalanceColor(image, 15)

    def grind_func(self, image):
        return mopi(image)

    def filter_func(self, image):
        return image

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


