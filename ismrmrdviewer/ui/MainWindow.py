
import logging
import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Signal, Slot

from .FileWidget import FileWidget


class MainWindow(QtWidgets.QMainWindow):

    open = Signal(str)

    def __init__(self):
        super().__init__()

        self.setUnifiedTitleAndToolBarOnMac(True)

        self.fileMenu = super().menuBar().addMenu("&File")
        self.fileMenu.addAction("&Open", self.open_file_dialog)

        self.placeholder = self._create_placeholder()
        self.setCentralWidget(self.placeholder)
        self.open.connect(self.open_file)

    @Slot()
    def open_file_dialog(self):

        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open ISMRMRD Data File",
            os.getcwd(),
            "ISMRMRD Data Files (*.h5 *.mrd);;All Files (*)"
        )

        if not file_name:
            return

        self.open.emit(file_name)

    def open_file(self, file_name):
        logging.info(f"Opening file: {file_name}")
        self.setWindowFilePath(file_name)
        self.setCentralWidget(FileWidget(self, file_name))

    def _create_placeholder(self):
        placeholder = QtWidgets.QWidget(self)
        placeholder.setObjectName("placeholderRoot")
        layout = QtWidgets.QVBoxLayout(placeholder)
        layout.setContentsMargins(80, 80, 80, 80)
        layout.setSpacing(32)

        card = QtWidgets.QFrame(placeholder)
        card.setObjectName("placeholderCard")
        card_layout = QtWidgets.QHBoxLayout(card)
        card_layout.setContentsMargins(48, 48, 48, 48)
        card_layout.setSpacing(32)
        card.setMinimumWidth(720)
        shadow = QtWidgets.QGraphicsDropShadowEffect(card)
        shadow.setBlurRadius(35)
        shadow.setColor(QtGui.QColor(15, 23, 42, 60))
        shadow.setOffset(0, 18)
        card.setGraphicsEffect(shadow)

        icon_label = QtWidgets.QLabel(card)
        icon_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        icon = card.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_FileIcon)
        icon_label.setPixmap(icon.pixmap(96, 96))
        card_layout.addWidget(icon_label)

        text_layout = QtWidgets.QVBoxLayout()
        text_layout.setSpacing(16)

        title = QtWidgets.QLabel("Welcome to ISMRMRD Viewer", card)
        title_font = QtGui.QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #1f2933;")

        description = QtWidgets.QLabel(
            "A cross-platform tool for exploring ISMRMRD/MRD MRI datasets, "
            "including headers, reconstructed images, acquisitions, and waveforms.",
            card
        )
        description.setWordWrap(True)
        description.setStyleSheet("color: #4b5563; font-size: 14px;")

        tips_container = QtWidgets.QWidget(card)
        tips_layout = QtWidgets.QVBoxLayout(tips_container)
        tips_layout.setContentsMargins(0, 0, 0, 0)
        tips_layout.setSpacing(8)
        tips = [
            "Use the button below or File → Open in the menu to choose a data file.",
            "Both .h5 and .mrd files are supported; the tree on the left lists the contents.",
            "Viewers on the right switch automatically based on the selected content."
        ]
        for tip in tips:
            row = QtWidgets.QHBoxLayout()
            row.setContentsMargins(0, 0, 0, 0)
            bullet = QtWidgets.QLabel("•", tips_container)
            bullet.setStyleSheet("color: #2563eb; font-size: 16px; font-weight: bold;")
            bullet.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            text = QtWidgets.QLabel(tip, tips_container)
            text.setWordWrap(True)
            text.setStyleSheet("color: #6b7280; font-size: 13px;")
            row.addWidget(bullet, 0, QtCore.Qt.AlignmentFlag.AlignTop)
            row.addWidget(text, 1)
            tips_layout.addLayout(row)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        open_button = QtWidgets.QPushButton("Choose Data File", card)
        open_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        open_button.setMinimumWidth(180)
        open_button.setIcon(card.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogOpenButton))
        open_button.clicked.connect(self.open_file_dialog)
        button_layout.addWidget(open_button)
        button_layout.addStretch()

        text_layout.addWidget(title)
        text_layout.addWidget(description)
        text_layout.addWidget(tips_container)
        text_layout.addLayout(button_layout)

        card_layout.addLayout(text_layout, stretch=1)

        layout.addStretch()
        layout.addWidget(card, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        placeholder.setStyleSheet(
            """
            #placeholderRoot {
                background-color: #f3f4f6;
            }
            #placeholderCard {
                border-radius: 16px;
                background: #ffffff;
                border: 1px solid #d0d7de;
            }
            """
        )

        return placeholder
