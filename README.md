# pyqt-tooltip-list-widget
PyQt QListWidget which shows text as tooltip longer than widget\'s size

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-tooltip-list-widget`

## Example
Code Sample

```python
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication
from pyqt_tooltip_list_widget import ToolTipListWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__listWidget = ToolTipListWidget()
        self.__listWidget.addItem(
            'Note: The selection rectangle will only be visible if the selection mode is in a mode where more than one item can be selected; i.e., it will not draw a selection rectangle if the selection mode is QAbstractItemView::SingleSelection.')
        self.__listWidget.addItem('B')
        self.__listWidget.addItem('C')

        lay = QGridLayout()
        lay.addWidget(self.__listWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = Widget()
    example.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/159149622-70896610-30c3-431d-859d-4f87b96267fe.png)

