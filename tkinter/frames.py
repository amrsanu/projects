### individual container to contain different things

from tkinter import*

root = Tk()
frame = Frame(root, width=300, height=300)

button1 = Button(frame, text="Buttton 1")
button2 = Button(frame, text="Buttton 2")
button3 = Button(frame, text="Buttton 3")

button1.pack(side=LEFT)
button2.pack()
button3.pack()
frame.pack()

bottomFrame = Frame(root)
button4 = Button(bottomFrame, text="Button 4")
button4.pack()

bottomFrame.pack(side=BOTTOM)


root.mainloop()