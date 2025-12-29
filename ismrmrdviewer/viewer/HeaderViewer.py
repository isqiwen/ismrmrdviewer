import logging
import xml.etree.ElementTree as ET

from PySide6 import QtCore, QtWidgets


class HeaderViewer(QtWidgets.QTreeWidget):

    PARAMETER_COLUMN = 0
    _parameter_width = None

    def __init__(self, container):
        super().__init__()

        self.container = container

        dom = container.header.toDOM()
        xml = dom.toprettyxml(indent=4 * ' ')
        root = ET.fromstring(xml)

        item = QtWidgets.QTreeWidgetItem(self)
        item.setText(0, root.tag)
        self.addTopLevelItem(item)
        item.setExpanded(True)
        self.populate(item, root)
        self.setColumnCount(2)
        self.setHeaderLabels(("Parameter", "Value"))
        self.header().setStretchLastSection(True)
        self.header().sectionResized.connect(self._remember_parameter_width)
        QtCore.QTimer.singleShot(0, self._apply_parameter_width)

    def populate(self, item, node):
        for child in node:
            child_item = QtWidgets.QTreeWidgetItem(item)
            child_item.setText(0, child.tag[30:])
            if (len(child) == 0):
                child_item.setData(1, QtCore.Qt.EditRole, child.text)
                item.addChild(child_item)
                child_item.setExpanded(True)
            else:
                item.addChild(child_item)
                self.populate(child_item, child)
                child_item.setExpanded(True)

    def _apply_parameter_width(self):
        hint = max(300, self.sizeHintForColumn(self.PARAMETER_COLUMN))
        stored = HeaderViewer._parameter_width or hint
        self.header().resizeSection(self.PARAMETER_COLUMN, stored)
        HeaderViewer._parameter_width = stored

    def _remember_parameter_width(self, logical_index, _old, new):
        if logical_index == self.PARAMETER_COLUMN:
            HeaderViewer._parameter_width = new
