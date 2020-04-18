from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import urllib.request
import pafy
import humanize
import os



ui, _ = loadUiType("Main.ui")
class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handle_Buttons()



    def InitUI(self):
        # contain all ui changes in loading
        self.tabWidget.tabBar().setVisible(False)
        self.DarkOrange_style()
        self.Move_box_1()
        self.Move_box_2()
        self.Move_box_3()
        self.Move_box_4()


    def Handle_Buttons(self):
        # handle all buttons in app
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handle_Browse)
        self.pushButton_8.clicked.connect(self.Get_Video_Data)
        self.pushButton_3.clicked.connect(self.Save_Browse)
        self.pushButton_4.clicked.connect(self.Download_Video)
        self.pushButton_5.clicked.connect(self.PlayList_Download)
        self.pushButton_6.clicked.connect(self.Playlist_Save_Browse)
        self.pushButton_9.clicked.connect(self.Open_Home)
        self.pushButton_12.clicked.connect(self.Open_Download)
        self.pushButton_11.clicked.connect(self.Open_Youtube)
        self.pushButton_10.clicked.connect(self.Open_settings)
        self.pushButton_13.clicked.connect(self.DarkOrange_style)
        self.pushButton_14.clicked.connect(self.Qdark_style)
        self.pushButton_15.clicked.connect(self.QdarkGray_style)
        self.pushButton_20.clicked.connect(self.Darkblu_Style)
        self.pushButton_7.clicked.connect(self.Open_About)
        self.pushButton_21.clicked.connect(self.Close)




    def Handle_Progress(self, blocknum, blocksize, totalsize):
        # calculate the progress
        readed_data = blocknum * blocksize

        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()




    def Handle_Browse(self):
        # enable us to browse, and pick a location to save the file
        save_location = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files(*.*)")

        self.lineEdit_2.setText(str(save_location[0]))



    def Download(self):
        # downloading any file
        print("starting download")
        download_url = self.lineEdit.text()
        save_location =self.lineEdit_2.text()
        if download_url == "" or save_location == "":
            QMessageBox.warning(self, "Data Error", "Provide a valid URL or save location")
        else:
            try:
                urllib.request.urlretrieve(download_url, save_location, self.Handle_Progress)
            except Exception:
                QMessageBox.warning(self, "Download Error ", "Provide a valid URL or save location")
                return
        # Need a modification information pops up everytime. fix it using if statement
        QMessageBox.information(self, "Download Completed", "File Downloaded Successfully!")

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.progressBar.setValue(0)





    def Save_Browse(self):
        # to save location in edit line, after we browse
        pass




##############################################################################################
##################### Download for youtube single video#####################################
    def Save_Browse(self):
        # to save location in edit line, after we browse
        save_location = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files(*.*)")

        self.lineEdit_4.setText(str(save_location[0]))

    def Get_Video_Data(self):
        # it will get video data (data includes video qualities)
        video_url = self.lineEdit_3.text()
        if video_url == "" :
            QMessageBox.warning(self, "URL Error", "Provide a valid URL!")
        else:
            video = pafy.new(video_url)
            print(video.title)
            print(video.duration)
            print(video.author)
            print(video.length)
            print(video.viewcount)
            print(video.likes)
            print(video.dislikes)

            video_streams = video.streams
            for stream in video_streams:
                size = humanize.naturalsize(stream.get_filesize())
                data = "{} {} {} {}".format(stream.mediatype, stream.extension, stream.quality, size)
                self.comboBox_2.addItem(data)








    def Download_Video(self):
        # it will download video of selected video Quality
        video_url = self.lineEdit_3.text()
        save_location = self.lineEdit_4.text()
        if video_url == "" or save_location == "":
            QMessageBox.warning(self, "Data Error", "Provide a valid Video URL or save location")
        else:
            video = pafy.new(video_url)
            video_stream = video.streams
            video_quality = self.comboBox_2.currentIndex()
            download = video_stream[video_quality].download(filepath=save_location , callback=self.Video_Progress)





    def Video_Progress(self, total, recieved, ratio, rate, time):
        #progress bar for downloading video
        read_data = recieved
        if total > 0 :
            download_percentage = read_data * 100 / total
            self.progressBar_2.setValue(download_percentage)
            time_remaining = round(time/60, 2)
            self.label_5.setText(str("{} remaining minutes".format(time_remaining)))
            QApplication.processEvents()




    ######################################################################################################
    ################################### YouTube Playlist Download

    def PlayList_Download(self):
        global current_video_in_download, quality
        playlist_url = self.lineEdit_5.text()
        save_location = self.lineEdit_6.text()

        if playlist_url == '' or save_location == '':
            QMessageBox.warning(self, "Data Error", "Provide a valid Playlist URL or save location")

        else:
            playlist = pafy.get_playlist(playlist_url)
            playlist_videos = playlist['items']

            self.lcdNumber_2.display(len(playlist_videos))

        os.chdir(save_location)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))

        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        current_video_in_download = 1
        quality = self.comboBox_2.currentIndex()

        QApplication.processEvents()

        for video in playlist_videos:
            current_video = video['pafy']
            current_video_stream = current_video.streams
            self.lcdNumber.display(current_video_in_download)
            download = current_video_stream[quality].download(callback=self.Playlist_Progress)
            QApplication.processEvents()

            current_video_in_download += 1

    def Playlist_Progress(self, total, recieved, ratio, rate, time):
        # progress bar for downloading video
        read_data = recieved

        if total > 0:
            download_percentage = read_data * 100 / total
            self.progressBar_3.setValue(download_percentage)
            time_remaining = round(time / 60, 2)
            self.label_6.setText(str("{} remaining minutes".format(time_remaining)))
            QApplication.processEvents()
    def Playlist_Save_Browse(self):
        playlist_save_location = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_6.setText(playlist_save_location)

    #####################################################################3
    ########### UI changes methods

    def Open_Home(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Download(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Youtube(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_settings(self):
        self.tabWidget.setCurrentIndex(3)
    def Open_About(self):
        self.tabWidget.setCurrentIndex(4)


    ###################################################################3
    ################### App themes methods

    def Darkblu_Style(self):
        style = open("themes/darkblu.css", "r")
        style = style.read()
        self.setStyleSheet(style)

    def Qdark_style(self):
        style = open("themes/qdark.css", "r")
        style = style.read()
        self.setStyleSheet(style)
    def QdarkGray_style(self):
        style = open("themes/qdarkgray.css", "r")
        style = style.read()
        self.setStyleSheet(style)

    def DarkOrange_style(self):
        style = open("themes/darkorange.css", "r")
        style = style.read()
        self.setStyleSheet(style)


    ########################################################################
    ######################### App Animation

    def Move_box_1(self):
        animation_box1 = QPropertyAnimation(self.groupBox, b"geometry")
        animation_box1.setDuration(2000)
        animation_box1.setStartValue(QRect(0, 0, 0, 0))
        animation_box1.setEndValue(QRect(50, 40, 321, 121))
        animation_box1.start()
        self.animation_box1 = animation_box1



    def Move_box_2(self):
        animation_box2 = QPropertyAnimation(self.groupBox_2, b"geometry")
        animation_box2.setDuration(2000)
        animation_box2.setStartValue(QRect(0, 0, 0, 0))
        animation_box2.setEndValue(QRect(410, 40, 331, 121))
        animation_box2.start()
        self.animation_box2 = animation_box2



    def Move_box_3(self):
        animation_box3 = QPropertyAnimation(self.groupBox_3, b"geometry")
        animation_box3.setDuration(2000)
        animation_box3.setStartValue(QRect(0, 0, 0, 0))
        animation_box3.setEndValue(QRect(50, 220, 321, 121))
        animation_box3.start()
        self.animation_box3 = animation_box3




    def Move_box_4(self):
        animation_box4 = QPropertyAnimation(self.groupBox_4, b"geometry")
        animation_box4.setDuration(2000)
        animation_box4.setStartValue(QRect(0, 0, 0, 0))
        animation_box4.setEndValue(QRect(410, 220, 331, 121))
        animation_box4.start()
        self.animation_box4 = animation_box4


    ##########################################################################
    ########## Adding about program and programmer and adding a close button to terminate program completely

    def Close(self):
        exit()



def main():
    app = QApplication(sys.argv)
    windows = MainApp()
    windows.show()
    app.exec_()
if __name__ == "__main__":
    main()

