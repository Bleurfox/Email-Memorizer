import tkinter as tk
# https://www.youtube.com/watch?v=k_ToCC4-pe8 used this video to learn about tkinter

root = tk.Tk()

    
root.title("Email Memorizer") # Sets the title
height = 720 # Window Size
width =  1280 # Window Size
screenheight = root.winfo_screenheight()
screenwidth = root.winfo_screenwidth()
alignstr = "%dx%d+%d+%d" % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
root.geometry(alignstr)
root.resizable(width = True, height = True)
tk.Label(root, text = "Emails").pack()


root.mainloop()