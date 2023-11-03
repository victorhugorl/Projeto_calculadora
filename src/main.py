import sys

from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH
from buttons import ButtonsGrid

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')
        # Arbitrary string

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
