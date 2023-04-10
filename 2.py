import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0
        self.total_label_text = tk.StringVar()
        self.total_label_text.set(self.total)
        self.total_label = tk.Label(master, textvariable=self.total_label_text)

        self.label = tk.Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = tk.Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = tk.Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = tk.Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = tk.Button(master, text="Reset", command=lambda: self.update("reset"))

        # Laying out the widgets using grid
        self.label.grid(row=0, column=0, sticky="W")
        self.total_label.grid(row=0, column=1)
        self.entry.grid(row=1, column=0, columnspan=2, sticky="WE", pady=5)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=3, column=0, columnspan=2, sticky="WE", pady=5)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
