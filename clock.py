from tkinter import *
from gui import *

def main():
    """
    Method used to initialize GUI.
    :param window: Window of GUI.
    :param GUI: Graphical User Interface.
    """
    window = Tk()
    window.title('Digital Clock')
    GUI(window)
    mainloop()


if __name__ == '__main__':
    main()