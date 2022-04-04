from PyQt5.QtWidgets import QListWidget, QWidget, QListWidgetItem


class ShowLongTextAsToolTipListWidget(QListWidget):

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
        item_width = self.fontMetrics().boundingRect(text).width()
        if item_width > self.width():
            item.setToolTip(text)

    def __showToolTip(self, item: QListWidgetItem):
        item_width = self.visualItemRect(item).width()
        width = self.width()
        if item_width > width:
            item.setToolTip(item.text())
        else:
            item.setToolTip('')