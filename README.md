# pyqt-moving-label
PyQt label which is moving from left to right

Good to use as an advertisement or notice tool.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-moving-label`

## Example
Code Sample
```python
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QTextEdit, QWidget
from pyqt_moving_label.movingLabel import MovingLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__label = MovingLabel('Moving Label', self)

        lay = QVBoxLayout()
        lay.addWidget(self.__label)
        lay.addWidget(QTextEdit())

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/170969527-91c80a06-b6eb-4aaf-a305-421479bd7139.mp4

