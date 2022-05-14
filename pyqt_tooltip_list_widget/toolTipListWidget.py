from PyQt5.QtWidgets import QListWidget, QWidget, QListWidgetItem


class ToolTipListWidget(QListWidget):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setMouseTracking(True)
        self.itemEntered.connect(self.__showToolTip)

    def addItem(self, aitem) -> None:
        item = ''
        text = ''
        if isinstance(aitem, str):
            item = QListWidgetItem()
            text = aitem
            item.setText(text)
        elif isinstance(aitem, QListWidgetItem):
            item = aitem
            text = item.text()
        self.setItemWidget(item, QWidget())
        super().addItem(item)

    def __showToolTip(self, item: QListWidgetItem):
        text = item.text()
        text_width = self.fontMetrics().boundingRect(text).width()
        width = self.width()
        if text_width > width:
            item.setToolTip(text)
        else:
            item.setToolTip('')