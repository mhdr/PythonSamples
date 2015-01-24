from PyQt5.QtCore import *
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

player=QMediaPlayer()

path=QUrl.fromLocalFile("/home/mahmood/MPLS.mp4")
media=QMediaContent(path)

playlist=QMediaPlaylist()
playlist.addMedia(media)
playlist.setCurrentIndex(1)
player.setPlaylist(playlist)


video=QVideoWidget()
player.setVideoOutput(video)
video.show()

player.play()

app.exec_()

# no completed