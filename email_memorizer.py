import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

# Start of implementing frame switching
class SampleApp(tk.Tk):
            
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Email Memorizer")
        self.title_font = tkFont.Font(size = 18, weight = "bold", slant = "italic")
        height = 720 # Window Size
        width =  1280 # Window Size
        screenheight = self.winfo_screenheight()
        screenwidth = self.winfo_screenwidth()
        alignstr = "%dx%d+%d+%d" % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
        self.geometry(alignstr)
        self.resizable(width = True, height = True)
        

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        for F in (Home, EmailOne, EmailTwo):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Home(tk.Frame):

    def __init__(self, parent, controller):
       
           
        
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Home")
        label.pack(side = "top", fill = "x", pady = 10) 
        
        button_one = tk.Button(self, text = "Email One", command = lambda : controller.show_frame("EmailOne"))
        button_two = tk.Button(self, text = "Email Two", command = lambda : controller.show_frame("EmailTwo"))

        button_one.pack()
        button_two.pack()

class EmailOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Email One")
        label.pack(side = "top", fill = "x", pady = 10)
        button = tk.Button(self, text = "Home", command = lambda : controller.show_frame("Home"))

        button.pack()

class EmailTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Email Two")
        label.pack(side = "top", fill = "x", pady = 10)
        button = tk.Button(self, text = "Home", command = lambda : controller.show_frame("Home"))

        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
