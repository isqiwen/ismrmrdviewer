#!/usr/bin/env python
import argparse
import logging
import sys

from PySide6 import QtWidgets

import ismrmrdviewer.ui as ui


def main():
    logging.basicConfig(
        format='[%(levelname)s] %(message)s',
        level='INFO'
    )

    parser = argparse.ArgumentParser(description="Simple ISMRMRD data file viewer.")
    parser.add_argument('file', type=str, nargs='?', help="ISMRMRD data file.")
    args = parser.parse_args()

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("ismrmrdviewer")

    main = ui.MainWindow()
    main.showMaximized()

    if args.file:
        main.open_file(args.file)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
