import tkinter as tk
from tkinter import Label, Button, PhotoImage
from PIL import Image, ImageTk

    # Set up the grid configuration
def startScreen(start, order_click):
    # Column weights which dictate how prevalent each one is over each other
    start.columnconfigure(0, weight=1) 
    start.columnconfigure(1, weight=0)
    start.columnconfigure(2, weight=0)  

    # Title and button container with label and panel
    left_panel_container = tk.Frame(start, bg='white')
    left_panel_container.grid(row=0, column=0, rowspan=2, sticky='nw', padx=0, pady=0)

    title_label = Label(left_panel_container, text="CoffeeCreations", font=("Arial", 30), background="white")
    title_label.pack()

    title_panel = tk.Frame(left_panel_container, bg='white')
    title_panel.pack(side='top')

    button_panel = tk.Frame(left_panel_container, bg='white')
    button_panel.pack(side='top')

    order_button = Button(button_panel, text="Start order", font=('arial', 12), width=25,
                          command=order_click)
    order_button.pack(anchor='center')

    # Right-side container frame to hold both panels
    right_panel_container = tk.Frame(start)
    right_panel_container.grid(row=0, column=2, rowspan=3, sticky="ne", padx=0, pady=0)

    panel_gray = tk.Frame(right_panel_container, bg="gray", width=100, height=480)
    panel_gray.pack(side="left", fill="y")

    panel_blue = tk.Frame(right_panel_container, bg="light blue", width=100, height=480)
    panel_blue.pack(side="left", fill="y")

    # Uses the image class to open the image and then resizes it
    pil_image = Image.open("final_project/coffee.gif")
    pil_image = pil_image.resize((200, 200))
    start.coffeeImage = ImageTk.PhotoImage(pil_image)

    image_label = Label(start, image=start.coffeeImage, background="white")
    image_label.grid(row=2, column=0, sticky="sw", padx=10, pady=10)