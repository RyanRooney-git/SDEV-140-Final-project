import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from coffeecreations_settings_window import windowSettings
from coffeecreations_startscreen import startScreen

class CoffeeCreations(tk.Tk):
    """A simple GUI which shows different widgets, buttons, and visuals in order to order coffee."""
    def __init__(self):
        super().__init__()
        windowSettings(self)
        self.frontPage()
        self.TOTAL = 0
        self.coffee_order = ''

    # When the start order method is called, it destroys the front page widgets and then starts the coffee ordering process
    def frontPage(self):
        def startOrder():
            for new_screen in self.winfo_children():
                new_screen.destroy() # Destroys the current windows widgets but not the total value to start off with a new visual state. Otherwise, it would become clunky and buggy
            self.coffeeOrder(self.toppingsPage) # Passes the self.toppings page method every time a button is pressed for the starting coffee choice        
        startScreen(self, startOrder) # Calls the start order instance

    # Back button for checking another type of coffee
    def back_button(self):
        for new_screen in self.winfo_children():
            new_screen.destroy()
        self.TOTAL = 0 # Resets the total to 0 after you click back to insure the price is accurate
        self.coffee_order = ''
        self.coffeeOrder(self.toppingsPage) # Calls the toppings page back which lets you go back to the previous page visually
        
    # Starts the coffee order when called
    def coffeeOrder(self, total_topping):
        self.columnconfigure(0, weight=1) 
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        # Coffee label
        coffee_label = Label(text="Coffee type", font=("Arial", 16, 'bold'), background='white')
        coffee_label.grid(row=0, column=0, rowspan=2, sticky='n')

        # Radio buttons and frame
        radio_frame = tk.Frame(self, bg='white')
        radio_frame.grid(row=1, column=0, sticky='n')

        # Creates a string variable to check for when the item is in the dictionary
        self.coffee_types = tk.StringVar(value='')
        self.coffee_price = {'Normal': 2,
                        'Mocha': 5,
                        'Cappucino': 6,
                        'Espresso': 5,
                        'Frappucino': 3}

        # Creates radio buttons using a for loop
        for coffee, price in self.coffee_price.items():
            # Radio buttons variable which uses the radio frame, then adds the text and price key value pair from self.coffee_price
            radio_buttons = tk.Radiobutton(radio_frame, text=f"{coffee}: ${price}", value=coffee, 
                                        variable=self.coffee_types, bg='light gray', indicatoron=0, 
                                        width=13, command=total_topping)
            radio_buttons.pack(side='top', fill='y', pady=5)


        # Right-side container frame to hold both panels
        right_panel_container = tk.Frame(self)
        right_panel_container.grid(row=0, column=2, rowspan=3, sticky="ne", padx=0, pady=0)

        panel_gray = tk.Frame(right_panel_container, bg="gray", width=100, height=480)
        panel_gray.pack(side="left", fill="y")

        panel_blue = tk.Frame(right_panel_container, bg="light blue", width=100, height=480)
        panel_blue.pack(side="left", fill="y")
    
    # The toppings sections of the app
    def toppingsPage(self):
        # Gets the coffee type value and then checks with a for loop
        coffee_type = self.coffee_types.get()
        for coffee, value in self.coffee_price.items():
            if coffee == coffee_type:
                self.coffee_order += f"{coffee}: ${value}"
                self.TOTAL += value
            for new_screen in self.winfo_children():
                new_screen.destroy()

        self.columnconfigure(0, weight=1) 
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        # Back button, total button
        back_total_frame = tk.Frame(self, bg='white')
        back_total_frame.grid(row=1, column=0, sticky='nw', pady=20)

        back_button = Button(back_total_frame, text='Back', font=('Arial', 8, 'bold'), command=self.back_button)
        back_button.pack(side='left')

        total_button = Button(back_total_frame, text='Total', font=('Arial', 8, 'bold'), command=self.total_check)
        total_button.pack(side='left', padx=5)

        # Toppings checklist and frame
        toppings_label = Label(text="Toppings", font=("Arial", 16, 'bold'), background='white')
        toppings_label.grid(row=0, column=0, sticky='n')

        toppings_frame = tk.Frame(self, bg='white')
        toppings_frame.grid(row=2, column=0, sticky='nw')

        # Toppings dictionary holds the topping name as the key and price as the value
        self.toppings = {'Milk': 1,
                        'Sugar': 0.5,
                        'Marshmallow': 2,
                        'Whipped cream': 1,
                        'Caramel sauce': 2,
                        'Vanilla extract': 0.75}
        
        # Empty dictonary to contain the state of each checkbox
        self.toppings_state = {}

        # For loop which creates the dictionary containing the check list toppings key values
        for toppings, price in self.toppings.items():
            on_off = tk.IntVar()
            toppings_check_boxes = tk.Checkbutton(toppings_frame, text=f"{toppings}: ${price}", 
                                                  variable=on_off, bg='white', pady=3)
            toppings_check_boxes.grid(sticky='w')
            self.toppings_state[toppings] = on_off # Check to see if 0 or 1. 1 is when it is checked and count all with a for loop comparing this value

        # Right-side container frame to hold both panels
        right_panel_container = tk.Frame(self)
        right_panel_container.grid(row=0, column=2, rowspan=3, sticky="ne", padx=0, pady=0)

        panel_gray = tk.Frame(right_panel_container, bg="gray", width=100, height=480)
        panel_gray.pack(side="left", fill="y")

        panel_blue = tk.Frame(right_panel_container, bg="light blue", width=100, height=480)
        panel_blue.pack(side="left", fill="y")

    # Checks the total which goes to the next total screen
    def total_check(self):
        self.total_price = {}
        for item, value in self.toppings_state.items():
            topping_checked = value.get() # Gets the on_off variable and if it's a 1
            if topping_checked == 1:
                for topping, price in self.toppings.items(): # A nested for loop which checks the first for loop to see the item name
                    if topping == item: # And compares to see if the topping name is the item name. And if it is, it adds to the total
                        self.TOTAL += price
                        self.total_price[topping] = price
        self.total_window() # Calls the total_window method which brings up a second window

    # Total window which shows the order and price
    def total_window(self):
        # New total object which associates for the total window
        total = tk.Toplevel()
        total.title("Total summary")
        total.geometry("360x240")
        total.resizable(False, False)
        total.configure(background="light gray")

        total.columnconfigure(0, weight=0)
        total.columnconfigure(1, weight=1) 
        total.rowconfigure(0, weight=1)
        total.grab_set() # Makes this window the only window the user can interact with

        # Exit method call which exits the current window
        def exit_execution():
            self.destroy()

        # Shows the user the coffee after pressing confirm
        def total_Shown():
            total_panel = Text(total_container, bg='silver') # height width changes box
            total_panel.pack(side='top', pady=2) # prevent users from typing in input box

            # List named lines that appends the information into one large list
            lines =[f"Coffee order"]
            lines.append('')
            lines.append(f"-{self.coffee_order}")
            for total, shown in self.total_price.items():
                lines.append(f"-{total}: ${shown}")
            lines.append('')
            lines.append(f"Total = ${self.TOTAL}")

            for index, line in enumerate(lines, start=1):
                total_panel.insert(f"{index}.0", line + "\n")
            
            # Makes sure the size of the text box is at max the largest len of the width of the lines
            num_lines = len(lines)
            line_width = 0
            for line in lines:
                if len(line) > line_width:
                    line_width = len(line)
            input_box = line_width
            # Configures the text panel to the height of the number of lines and width from earlier
            total_panel.config(height=num_lines, width=input_box, state=DISABLED) # Disabled state prevents typing inside

        # After clicking the order button destoys the previous window and shows the user a thank you with a coffee image
        def ordered():
            for thank_you in total.winfo_children():
                thank_you.destroy()

            total.columnconfigure(0, weight=0)
            total.columnconfigure(1, weight=1) 
            total.rowconfigure(0, weight=1)
            total.rowconfigure(1, weight=1)

            # Since the total_window has used total.grab_set() earlier, this method lets the user exit and then it closes the entire app 
            def close():
                self.destroy()

            # Without the close method, the app would close just the total window 
            total.protocol("WM_DELETE_WINDOW", close)
            
            # Title container with Thank you shown
            total_title_container = tk.Frame(total, bg='light gray')
            total_title_container.grid(row=0, column=1, rowspan=2, columnspan=2, sticky='nsew')

            title_label = tk.Label(total_title_container, text="Thank you!", font=("Arial", 16, 'bold'), background="light gray")
            title_label.pack()

            # Image for the final thank you page
            pil_image = Image.open("final_project/coffee_total_page.gif")
            pil_image = pil_image.resize((150, 150))
            self.thankyouCoffee = ImageTk.PhotoImage(pil_image)

            image_label = Label(total, image=self.thankyouCoffee, background="light gray")
            image_label.grid(row=1, column=1, sticky="nsew")

        # Title and button container with label and panel
        total_title_container = tk.Frame(total, bg='light gray')
        total_title_container.grid(row=0, column=0, sticky='w')

        title_label = tk.Label(total_title_container, text="Total:", font=("Arial", 16, 'bold'), background="light gray")
        title_label.pack()

        title_panel = tk.Frame(total_title_container, bg='light gray')
        title_panel.pack(side='top')

        button_panel = tk.Frame(total_title_container, bg='light gray')
        button_panel.pack(side='top')

        # Total cost shown to user
        total_container = tk.Frame(total, bg='light gray')
        total_container.grid(row=0, column=1)
            
        # Exit and order buttons
        order_button = Button(button_panel, text="Order", font=('arial', 8),
                          bg='green', width=4, command=ordered) # Runs the ordered method
        order_button.pack(side='left', padx=3)

        exit_button = Button(button_panel, text="Exit", font=('arial', 8),
                          bg='red', width=4, command=exit_execution) # Runs the exit_execution method
        exit_button.pack(side='left', padx=2)
        total_Shown()

# Loops over the application so it runs
def main():
    cc = CoffeeCreations()
    cc.mainloop()

if __name__ == "__main__":
    main()