__author__ = 'habeeb'

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *


class Talk(QObject):
    def __init__(self, file, parent=None):
        super(Talk, self).__init__(parent)
        self.file = file
        self._path = os.getcwd() + "\\resources\\audio\\"

        self.play()

    def createSoundFile(self):
        try:
            filename = self._path + self.file + ".wav"
            self.audioFile = QSound(filename)
        except IOError as e:
            print(str(e))

    def play(self):
        try:
            #self.createSoundFile()
            #self.audioFile.play()
            #Sfile = self.file + ".wav"
            s = QSound("0.wav", self)
            s.play()
            """sourceFile = QFile()
            sourceFile.setFileName("0.wav")
            if sourceFile.open(QIODevice.ReadOnly):
                print("Opened")

            formatt = QAudioFormat()
            formatt.setSampleRate(8000)
            formatt.setChannelCount(1)
            formatt.setSampleSize(32)
            formatt.setCodec("audio/pcm")
            formatt.setByteOrder(QAudioFormat.LittleEndian)
            formatt.setSampleType(QAudioFormat.Float)

            info = QAudioDeviceInfo(QAudioDeviceInfo.defaultOutputDevice())
            dev = QAudioDeviceInfo.defaultOutputDevice()
            if (not info.isFormatSupported(formatt)):
                qWarning("Raw audio format not supported by backend, cannot play audio.")
                formatt = info.nearestFormat(formatt)

            audio = QAudioOutput(dev, formatt)
            audio.stateChanged.connect(self.handleStateChanged)
            audio.start(sourceFile)
            #print(audio.error())
            print(audio.state())"""
        except Exception as e:
            print(str(e))

    def handleStateChanged(self, state):
        qWarning("state = " + self.stateMap.get(state, "Unknown"))


def main():
    app = QApplication(sys.argv)
    win = Talk("wait")
    app.exec_()

if __name__ == "__main__":
    """info = QAudioDeviceInfo()
    print(info.defaultOutputDevice().deviceName())
    print(info.availableDevices(QAudio.AudioOutput))"""

    main()