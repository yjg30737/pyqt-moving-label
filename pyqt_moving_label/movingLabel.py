from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QLabel, QDesktopWidget


class MovingLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__setDurationBasedOnWindowSizeFlag = True

    def __initUi(self):
        self.__animation = QPropertyAnimation(self, b'move')
        self.__animation.setStartValue(-self.fontMetrics().boundingRect(self.text()).width())
        width = QDesktopWidget().availableGeometry().width()
        self.__animation.setEndValue(width)
        self.__animation.setDuration(3000)
        self.__animation.valueChanged.connect(self.__moving)
        self.__animation.start()

    def __moving(self, x):
        self.move(x, self.y())
        if self.window().visibleRegion().boundingRect().width() <= x:
            self.__animation.stop()
            self.__animation.start()

    def event(self, e):
        if e.type() == 17:
            self.move(self.__animation.startValue(), self.y())
        elif e.type() == 14:
            if self.__setDurationBasedOnWindowSizeFlag:
                pass
            else:
                self.__animation.setEndValue(self.window().visibleRegion().boundingRect().width())
        return super().event(e)

    def setDurationBasedOnWindowSize(self, f: bool):
        self.__setDurationBasedOnWindowSizeFlag = not f

    def setDuration(self, milliseconds: int):
        self.__animation.setDuration(milliseconds)