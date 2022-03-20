from PyQt5.QtWidgets import QListWidget, QWidget, QListWidgetItem


class ShowLongTextAsToolTipListWidget(QListWidget):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setMouseTracking(True)

    def addItem(self, text: str) -> None:
        item = QListWidgetItem(self)
        item.setText(text)
        self.setItemWidget(item, QWidget())
        item_width = self.fontMetrics().boundingRect(text).width()
        if item_width > self.width():
            item.setToolTip(text)