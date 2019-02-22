from tkinter import*
import cv2
from tkinter import filedialog
import dlib
import numpy
from skimage import io
from PIL import Image, ImageTk
import face_recognition


width, height = 800, 600

class FaceRecognition(Tk):
    def __init__(self):

        Tk.__init__(self)
        Tk.iconbitmap(self, default="icon.ico")
        Tk.wm_title(self, "Face Recognition BY: Amrendra")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu = Menu(container)

        file = Menu(container, tearoff=False)
        file.add_command(label="Settings", command=self.faceDetection)
        file.add_command(label="Exit", command=quit)
        menu.add_cascade(label="File", menu=file)

        # tool = Menu(container, tearoff=False)
        # tool.add_command(label="NewTest")
        # tool.add_command(label="Exit", command=quit)
        # menu.add_cascade(label="Tool", menu=tool)

        Tk.config(self, menu=menu)

        self.frames = {}
        for F in (StartPage, faceRecognition):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") # NSEW=North South East West
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def client_exit(self):
        exit()

    def faceDetection(self):

        pass

    def showFiles(self):
        pass

########################################################################################################################


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Start Page.", font="LARGE_FONT")
        label.grid(column = 0, row=1, sticky=W+E+N+S, padx=5, pady=5)

        button1 = Button(self, text="Face Recognition", command=lambda: controller.show_frame(faceRecognition))
        button1.grid(column=0, row=3, sticky=W + E + N + S, padx=5, pady=5)

        button2 = Button(self, text="Camera", command=self.camera)
        button2.grid(column = 0, row=4, sticky=W+E+N+S, padx=5, pady=5)

        button3 = Button(self, text="Choose photo", command=self.show_image)
        button3.grid(column=0, row=5, sticky=W + E + N + S, padx=5, pady=5)


    def show_image(self):

        name = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                                          filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
                                          title="Choose a file."
                                          )

        while name is None:
            pass

        load = Image.open(name)
        print(load)
        load.thumbnail((720, 480), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img_frame = Label(self, image=render)
        img_frame.image = render

        img_frame.grid(column=1, row=1, rowspan=40, sticky=W + E + N + S, padx=5, pady=5, )

    def open_image(self):

        name = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                               filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
                               title="Choose a file."
                               )
        print(name)

    def camera(self, video_source=0):

        capture = cv2.VideoCapture(video_source)

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        while True:
            ret, frame = capture.read()
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()


class faceRecognition(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="FaceRecognition", font="LARGE_FONT")
        label.grid(column=0, row=1, sticky=W + E + N + S, padx=5, pady=5, columnspan=2)

        button1 = Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
        button1.grid(column=0, row=2, sticky=W + E + N + S, padx=5, pady=5)

        button2 = Button(self, text="Recognise", command=self.recognise)
        button2.grid(column=0, row=3, sticky=W + E + N + S, padx=5, pady=5)

        button3 = Button(self, text="Using image", command=self.recognise_in_image)
        button3.grid(column=0, row=4, sticky=W + E + N + S, padx=5, pady=5)

    def recognise(self):
        video_capture = cv2.VideoCapture(0)
        amrendra_image = face_recognition.load_image_file("amrendra.jpg")
        amrendra_face_encoding = face_recognition.face_encodings(amrendra_image)[0]
        ankit_image = face_recognition.load_image_file("ankit.jpg")
        ankit_face_encoding = face_recognition.face_encodings(ankit_image)[0]
        known_face_encodings = [
            amrendra_face_encoding,
            ankit_face_encoding
        ]
        known_face_names = [
            "Amrendra !",
            "Ankit !"
        ]

        while True:
            ret, frame = video_capture.read()
            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def recognise_in_image(self):

        amrendra_image = face_recognition.load_image_file("amrendra.jpg")
        amrendra_face_encoding = face_recognition.face_encodings(amrendra_image)[0]
        ankit_image = face_recognition.load_image_file("ankit.jpg")
        ankit_face_encoding = face_recognition.face_encodings(ankit_image)[0]
        known_face_encodings = [
            amrendra_face_encoding,
            ankit_face_encoding
        ]
        known_face_names = [
            "Amrendra !",
            "Ankit !"
        ]

        name = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                                          filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
                                          title="Choose a file."
                                          )

        while name is None:
            pass

        frame = face_recognition.load_image_file(name)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 50, 255), 4)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        out_frame = cv2.resize(frame, (960, 540))
        cv2.imshow('Video', out_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()


app = FaceRecognition()
app.geometry("1000x600")
app.mainloop()