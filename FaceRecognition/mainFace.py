from tkinter import*


class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Face Recognition By: Amrendra.")
        self.pack(fill=BOTH, expand=True)

        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)


        file = Menu(menu, tearoff=False)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        tool = Menu(menu)
        tool.add_command(label="Detection", command=self.faceDetection)
        tool.add_command(label="Show files", command=self.showFiles)
        menu.add_cascade(label="Tool", menu=tool)



    def client_exit(self):
        exit()

    def faceDetection(self):

        pass

    def showFiles(self):

        pass


root = Tk()
root.geometry("500x300") # To resize the main window.

app= Window(root)

root.mainloop()