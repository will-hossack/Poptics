#from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication


from poptics.gui import KnifeViewer


def main():
    app = QApplication([])
    ex = KnifeViewer() #LensViewer(lens)
    ex.show()
    app.exec_()

main()
