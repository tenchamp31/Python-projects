clclass ParentWindow(Frame):
    def __init__ (self)
    Frame.__init__ (self)

    sef.master = master
    self.master.resizable(width=False, height=False)
    self.master.geometry('()x()'.format(700,400))
    self.master.title("Learning Tkinter!")

    self.varFName = StringVar()
    self.varLName = StringVar()
    self.varFName.set('Bob')
    self.varLName.set('Smith')

    print(self.varFName.get())
    print(self.varLName.get())

    self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16) )











if _name_ == "_main_":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
