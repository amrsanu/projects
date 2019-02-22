from tkinter import*

root = Tk()

one = Label(root, text="one", bg="red")
two = Label(root, text="two", bg="yellow")
three = Label(root, text="three", bg="blue")

one.pack()
two.pack(fill=X)
three.pack(side=LEFT, fill=Y)

root.mainloop()