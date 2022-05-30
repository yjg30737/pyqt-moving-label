# pyqt-moving-label
PyQt label which is moving from left to right

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-moving-label`

## Detailed Description
This inherits the QLabel.

Good to use as an advertisement or notice tool.

You can create constructor like this - `MovingLabel('Moving Label', parent_class)`. Both two arguments are necessary.

### Method Overview
* `setDurationBasedOnWindowSize(f: bool)` - Set the duration based on window size. If you set this to `True`, The window gets bigger the moving speed gets faster. The window gets smaller the moving speed gets slower.
* `setDuration(milliseconds: int)` - Set the duration of label moving from left to right.

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
        # self.__label.setDurationBasedOnWindowSize(True)
        # self.__label.setDuration(5000)

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

