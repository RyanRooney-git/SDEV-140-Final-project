from breezypythongui import EasyFrame
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk

class coffeeCreations(EasyFrame):
    """A simple GUI which shows different widgets, buttons, and visuals in order to order coffee."""
    def __init__(self):
        EasyFrame.__init__(self,
                        title = "CoffeeCreations",
                        width = 720, height = 480,
                        resizable=False)
        self.addLabel("CoffeeCreations",
                    row = 0, column = 0,
                    font = ("Arial", 30),
                    columnspan = 1, sticky = "NW")
        self.addPanel(row=0,column=2,rowspan=2,background="light blue")
        self.addPanel(row=0,column=1,background="gray")
        self.addButton("Order coffee", row = 0, column = 0,columnspan=1)

        # Coffee image and resizing
        pil_image = Image.open("pictures/coffee.gif")
        pil_image = pil_image.resize((200, 200))

        self.coffeeImage = ImageTk.PhotoImage(pil_image)

        imageLabel = Label(self, image=self.coffeeImage, background="white")
        imageLabel.grid(row=0, column=0, sticky="SW")

def main():
    """Instantiate and pop up the window."""
    coffeeCreations().mainloop()

if __name__ == "__main__":
    main()



