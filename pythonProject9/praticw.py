from breezypythongui import EasyFrame


def main():
    LabelDemo().mainloop()


class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addlabel(text = "hello world!", row = 0, column = 0)

    if __name__ == "main":
        main()
