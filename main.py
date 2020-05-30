from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from UI import Ui_MainWindow
import sys
import cv2
import time
import common


class PhVioEditor(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(PhVioEditor,self).__init__()
        self.setupUi(self)
        global image_q
        global fliplr_mark
        global updown_mark
        global rotate_mark
        global RGBToWhite_mark
        global histogram_mark
        global image_video
        global adjustS_mark
        global fourcc
        global image_or_video
        global image
        global thread_exit
        global thread_exit_v



        fliplr_mark = 1
        updown_mark = 1
        rotate_mark = 1
        RGBToWhite_mark = 1
        histogram_mark = 1
        adjustS_mark = 0
        image_video = ""
        image_or_video = 2
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        image=""
        thread_exit = 0
        thread_exit_v = 0


    def image(self):
        global image_q
        global image
        global image_or_video
        global thread_exit
        image, type = QFileDialog.getOpenFileName(self, "Select file", "./", "Image Files (*.jpg)")
        print(type)

        if image:
            image_or_video = 0
            if thread_exit ==0:
                th_im = Thread_image(self)
                th_im.changePixmap_image.connect(self.setImage)
                th_im.start()
                thread_exit = 1


    def video_open(self):
        global video
        global image_or_video
        global thread_exit_v
        video, type = QFileDialog.getOpenFileName(self, "Select file", "./", "Video Files (*.mp4)")

        if video:
            image_or_video = 1
            if thread_exit_v == 0:
                th = Thread(self)
                th.changePixmap.connect(self.setImage)
                th.start()

    def flipLeftToRight(self):
        global fliplr_mark
        fliplr_mark=fliplr_mark*(-1)

    def upsidedown(self):
        global updown_mark
        updown_mark=updown_mark*(-1)

    def rotate(self):
        global rotate_mark
        rotate_mark = rotate_mark * (-1)

    def RGBToWhite(self):
        global RGBToWhite_mark
        RGBToWhite_mark = RGBToWhite_mark * (-1)

    def histogram_equalization(self):
        global histogram_mark
        histogram_mark = histogram_mark * (-1)

    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def adjustS(self):
        global adjustS_mark
        adjustS_mark = self.horizontalSlider.value()

    def save(self):
        global record
        global fourcc
        global record_mark
        global out_mark
        global image_or_video
        global image_save

        if image_or_video == 0:
            if image:
                image_save, ok2 = QFileDialog.getSaveFileName(self, "Save record", "./", "Video Files (*.jpg)")
                if image_save:
                    ths_im= Thread_Save_image(self)
                    ths_im.start()

        if image_or_video == 1:
            if video:
                record, ok2 = QFileDialog.getSaveFileName(self, "Save record", "./", "Video Files (*.mp4)")
                if record:
                    ths = Thread_Save(self)
                    ths.start()
                    self.pushButton_11.setText("Processing")


class Thread_image(QThread):
    changePixmap_image = pyqtSignal(QImage)

    def run(self):

        while True:
            frame = cv2.imread(image)

            if fliplr_mark == -1:
                frame = common.flipLeftToRight(frame)
            if updown_mark == -1:
                frame = common.upsidedown(frame)
            if rotate_mark == -1:
                frame = common.rotate(frame)
            if RGBToWhite_mark == -1:
                frame = common.RGBToWhite(frame)
            if histogram_mark == -1:
                frame = common.histogram_equalization_opti(frame)

            frame = common.adjustS(frame, adjustS_mark)
            print(adjustS_mark)

            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            v = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            if image_or_video == 0:
                self.changePixmap_image.emit(v)
                time.sleep(0.01)


class Thread_Save_image(QThread):

    def run(self):
        frame = cv2.imread(image)

        if fliplr_mark == -1:
            frame = common.flipLeftToRight(frame)
        if updown_mark == -1:
            frame = common.upsidedown(frame)
        if rotate_mark == -1:
            frame = common.rotate(frame)
        if RGBToWhite_mark == -1:
            frame = common.RGBToWhite(frame)
        if histogram_mark == -1:
            frame = common.histogram_equalization_opti(frame)
        frame = common.adjustS(frame, adjustS_mark)
        cv2.imwrite(image_save, frame)

        window.pushButton_11.setText("Record/Save")

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(video)

        while True:
            ret, frame = cap.read()
            if ret:
                if fliplr_mark == -1:
                    frame = common.flipLeftToRight(frame)
                if updown_mark == -1:
                    frame = common.upsidedown(frame)
                if rotate_mark == -1:
                    frame = common.rotate(frame)
                if RGBToWhite_mark == -1:
                    frame = common.RGBToWhite(frame)
                if histogram_mark == -1:
                    frame = common.histogram_equalization_opti(frame)

                frame = common.adjustS(frame, adjustS_mark)



                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                v = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                if image_or_video ==1:
                    self.changePixmap.emit(v)
                    time.sleep(0.01)
            else:
                break


class Thread_Save(QThread):
    def run(self):
        cap = cv2.VideoCapture(video)
        out = cv2.VideoWriter(record, fourcc, cap.get(cv2.CAP_PROP_FPS),
                              (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), True)
        while True:
            ret, frame = cap.read()
            if ret:
                if fliplr_mark == -1:
                    frame = common.flipLeftToRight(frame)
                if updown_mark == -1:
                    frame = common.upsidedown(frame)
                if rotate_mark == -1:
                    frame = common.rotate(frame)
                if RGBToWhite_mark == -1:
                    frame = common.RGBToWhite(frame)
                if histogram_mark == -1:
                    frame = common.histogram_equalization_opti(frame)
                frame = common.adjustS(frame, adjustS_mark)
                print(adjustS_mark)
                out.write(frame)
            else:
                break
        window.pushButton_11.setText("Record/Save")
        out.release()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = PhVioEditor()
    window.show()
    sys.exit(app.exec_())