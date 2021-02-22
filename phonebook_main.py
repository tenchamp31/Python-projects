from tkinter import *
import tkinter as tk



import phonebook_gui                            #importing other modules
import phonebook_func


class ParentWindow(Frame):                                  #primary tkinter object
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minisize(500,300)
        self.master.maximize(500,300)

        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook.ask_quit(self))
        arg = self.master


        phonebook_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
