import sys
import os
import random
from PyQt5 import QtWidgets, QtGui, QtCore

BASE_PATH = os.path.join(os.path.dirname(__file__), "Deskpet")

class DeskPet(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.childPets = []
        self.isDragging = False
        self.isMoving = False
        self.change = False

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(500, 500, 130, 130)
        self.currentAction = self.startIdle
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.changeDirectionTimer = QtCore.QTimer(self)
        self.changeDirectionTimer.timeout.connect(self.changeDirection)
        self.startIdle()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        self.setMouseTracking(True)
        self.dragging = False

    def loadImages(self, relative_path):
        full_path = os.path.join(BASE_PATH, relative_path)
        print(f"[DEBUG] Looking for images in: {full_path}")
        if not os.path.exists(full_path):
            print(f"[ERROR] Path does not exist: {full_path}")
            return []
        images = [
            QtGui.QPixmap(os.path.join(full_path, f))
            for f in os.listdir(full_path)
            if f.lower().endswith('.png')
        ]
        if not images:
            print(f"[WARNING] No images loaded from: {full_path}")
        return images


    def startIdle(self):
        self.setFixedSize(130, 130)
        self.currentAction = self.startIdle
        self.images = self.loadImages("nothing")
        self.currentImage = 0
        self.timer.start(100)
        self.moveSpeed = 0
        self.movingDirection = 0
        if self.changeDirectionTimer.isActive():
            self.changeDirectionTimer.stop()

    def startWalk(self):
        self.setFixedSize(130, 130)
        if not self.isDragging:
            self.currentAction = self.startWalk
            direction = random.choice(["left", "right"])
            self.images = self.loadImages(f"walk/{direction}")
            self.currentImage = 0
            self.movingDirection = -1 if direction == "left" else 1
            self.moveSpeed = 10
            self.timer.start(100)
            self.changeDirectionTimer.start(3000)

    def movePet(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        new_x = self.x() + self.movingDirection * self.moveSpeed
        if new_x < 10:
            new_x = 10
            if self.currentAction == self.startWalk:
                self.movingDirection *= -1
                self.timer.stop()
                self.images = []
                if self.movingDirection == -1:
                    self.images = self.loadImages("walk/left")
                else:
                    self.images = self.loadImages("walk/right")
                self.currentImage = 0
                self.timer.start(100)
        elif new_x > screen.width() - self.width() - 10:
            new_x = screen.width() - self.width() - 10
            if self.currentAction == self.startWalk:
                self.movingDirection *= -1
                self.timer.stop()
                self.images = []
                if self.movingDirection == -1:
                    self.images = self.loadImages("walk/left")
                else:
                    self.images = self.loadImages("walk/right")
                self.currentImage = 0
                self.timer.start(100)
        self.move(new_x, self.y())

    def stopOtherActions(self):
        self.timer.stop()
        if self.currentAction == self.startWalk:
            self.changeDirectionTimer.stop()
        self.startIdle()
    def updateAnimation(self):
        if not self.images:
            print("[ERROR] No images to display.")
            return
        pixmap = self.images[self.currentImage].scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio,
                                                       QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.currentImage = (self.currentImage + 1) % len(self.images)
        if hasattr(self, 'movingDirection'):
            self.movePet()
