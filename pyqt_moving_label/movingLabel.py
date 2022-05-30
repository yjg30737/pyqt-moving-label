from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QLabel


class MovingLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        self.__animation = QPropertyAnimation(self, b'move')
        self.__animation.setStartValue(-self.fontMetrics().boundingRect(self.text()).width())
        self.__animation.setEndValue(10000)
        self.__animation.setDuration(100000)
        self.__animation.valueChanged.connect(self.__moving)
        self.__animation.start()

    def __moving(self, x):
        self.move(x, self.y())
        if self.window().visibleRegion().boundingRect().width() < x:
            self.__animation.stop()
            self.__animation.start()

    def event(self, e):
        if e.type() == 17:
            self.move(self.__animation.startValue(), self.y())
        return super().event(e)