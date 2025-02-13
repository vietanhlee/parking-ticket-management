from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2
from OcrPlate import OcrPlate
from check_and_save_img import CheckAndSaveImg
import numpy as np

path_plate = 'model/best_plate.pt'
path_ocr = 'model/best_ocr.pt'

class Main(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self, MainWindow= MainWindow)

        self.cap = cv2.VideoCapture(r'test.MOV')
        if not self.cap.isOpened():
            print("Không thể mở camera")
            return
        
        self.OJ = CheckAndSaveImg()
        self.timer = QTimer()
        
        self.timer.start(8)
        self.digit_plate = None
        self.image_in = np.array([])

        self.ocr_plate = OcrPlate(path_model_detect_plate= path_plate, path_model_ocr= path_ocr)
       
        self.button_check_in.clicked.connect(self.check_in)
        self.button_check_out.clicked.connect(self.check_out)
        self.timer.timeout.connect(self.start_predict)

    def check_in(self):
        # print(1)
        if self.digit_plate != None and self.image_in.shape != (0, ):
            if not self.OJ.check_exists(label= self.digit_plate):
                self.OJ.save_image(image_array= self.image_in, label= self.digit_plate)
    def check_out(self):
        # print(2)
        if self.digit_plate != None and self.OJ.check_exists(label= self.digit_plate):
            self.OJ.delete_image(label= self.digit_plate)

    def start_predict(self):
        ret, frame = self.cap.read()
        if ret:
            frame_in = frame.copy()
            self.ocr_plate.set_data(imgage_input= frame)
            frame_main = self.convert_qimg(cv2.cvtColor(self.ocr_plate.image_output, cv2.COLOR_BGR2RGB))
            
            digits = self.ocr_plate.digit_out
            if(digits != 'unknow'):
                self.digit_plate = digits
                self.image_in = self.ocr_plate.image_input

                xyxy = self.ocr_plate.box_xyxy[-1]
                x, y, x1, y1 = map(int, xyxy)
                frame_cut = frame_in[y:y1, x:x1]
                frame_plate = self.convert_qimg(frame_cut)

                if self.OJ.check_exists(label= digits):
                    time, image_in = self.OJ.get_data(label= digits)
                    image_in = self.convert_qimg(cv2.cvtColor(image_in, cv2.COLOR_BGR2RGB))
                    self.label_time.setText(time)
                    self.label_in.setPixmap(QPixmap.fromImage(image_in).scaled(self.label_in.size()))
                    self.label_status.setText('Đã trong bãi')
                else:
                    self.label_time.setText('Không tồn tại xe')
                    self.label_in.setText('Không tồn tại xe')
                    self.label_status.setText('Không tồn tại xe')
                    self.label_price.setText('Không tồn tại xe')

                self.label_plate.setPixmap(QPixmap.fromImage(frame_plate).scaled(self.label_plate.size()))
                self.label_digits.setText(f'{str(digits)}')
                self.label_price.setText('3000 VND')
            else:
                self.digit_plate = None
                self.image_in = np.array([])

                self.label_plate.setText('Không nhận dạng được')
                self.label_digits.setText('Không nhận dạng được')
                self.label_time.setText('Không nhận dạng được')
                self.label_price.setText('Không nhận dạng được')
                self.label_status.setText('Không nhận dạng được')
                self.label_in.setText('Không nhận dạng được')
            
            self.label_main.setPixmap(QPixmap.fromImage(frame_main).scaled(self.label_main.size()))
            
        else:
            print("Không đọc được ảnh")
    
    def closeEvent(self, event):
        if self.cap.isOpened():
            self.cap.release()
        self.timer.stop()
        event.accept()

    def convert_qimg(self, image):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        # Chuyển numpy array về dạng bytes trước khi tạo QImage
        res = QImage(image.tobytes(), w, h, bytes_per_line, QImage.Format_RGB888)
        return res

import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Main(MainWindow)
MainWindow.show()
sys.exit(app.exec_())