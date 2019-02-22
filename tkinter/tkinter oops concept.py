import tkinter as tk

class FaceRecognition(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew") # NSEW=North South East West

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def pr(string):
    print(string)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page.", font="LARGR_FONT")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: pr("Amrendra"))
        button1.pack()



if __name__ == '__main__':
    app = FaceRecognition()
    app.mainloop()
