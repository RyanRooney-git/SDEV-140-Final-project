from breezypythongui import EasyFrame

class coffeeCreations(EasyFrame):
    """A simple GUI which shows different widgets, buttons, and visuals in order to order coffee."""
    def __init__(self):
        EasyFrame.__init__(self,
                        title = "CoffeeCreations",
                        width = 720,
                        height = 480)
        self.addLabel("CoffeeCreations",
                    row = 0,
                    column = 0,
                    font = ("Arial", 20),
                    columnspan = 3,
                    rowspan = 1,
                    background = "gray",
                    sticky = "NSEW")
        self.addButton("Order coffee",
                    row = 1,
                    column = 0,
                    columnspan = 3)
        # checklist = self.addPanel(
        #                     row=2,
        #                     column=1,)
        # checklist.addCheckbutton(text = "Test1", row=0, column=0, sticky="E")
        # checklist.addCheckbutton(text = "Test2", row=1, column=0, sticky="E")
        # checklist.addCheckbutton(text = "Test3", row=2, column=0, sticky="E")


def main():
    """Instantiate and pop up the window."""
    coffeeCreations().mainloop()

if __name__ == "__main__":
    main()