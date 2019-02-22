from tkinter import*
import cv2
from tkinter import filedialog
import dlib
from skimage import io
from PIL import Image, ImageTk


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

        tool = Menu(container, tearoff=False)
        tool.add_command(label="NewTest")
        tool.add_command(label="Exit", command=quit)
        menu.add_cascade(label="Tool", menu=tool)

        Tk.config(self, menu=menu)

        self.frames = {}
        for F in (StartPage, FaceLandmarks):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") # NSEW=North South East West
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def client_exit(self):
        exit()

########################################################################################################################


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Start Page.", font="LARGE_FONT")
        label.grid(column = 0, row=1, sticky=W+E+N+S, padx=5, pady=5)

        button = Button(self, text="Face Landmarks", command=lambda: controller.show_frame(FaceLandmarks))
        button.grid(column = 0, row=2, sticky=W+E+N+S, padx=5, pady=5)

        button2 = Button(self, text="Camera", command=self.camera)
        button2.grid(column = 0, row=3, sticky=W+E+N+S, padx=5, pady=5)

        button3 = Button(self, text="Choose photo", command=self.show_image)
        button3.grid(column=0, row=4, sticky=W + E + N + S, padx=5, pady=5)

    def show_image(self):
        """To show the image in frame"""
        name = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                                          filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
                                          title="Choose a file."
                                          )
        load = Image.open(name)
        print(load)
        load.thumbnail((720, 480), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img_frame = Label(self, image=render)
        img_frame.image = render
        img_frame.grid(column=1, row=1, rowspan=40, sticky=W + E + N + S, padx=5, pady=5, )

    def camera(self, video_source=0):
        """To open camera"""
        self.capture = cv2.VideoCapture(video_source)
        while True:
            ret, frame = self.capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.capture.release()
        cv2.destroyAllWindows()


########################################################################################################################

class FaceLandmarks(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="FaceLandmarks", font="LARGE_FONT")
        label.grid(column=0, row=1, sticky=W+E+N+S, padx=5, pady=5, columnspan=2)

        button1 = Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
        button1.grid(column = 0, row=2, sticky=W+E+N+S, padx=5, pady=5)

        button2 = Button(self, text="Choose Image", command=self.open_image)
        button2.grid(column=0, row=3, sticky=W+E+N+S, padx=5, pady=5)

        button4 = Button(self, text="Find Landmarks", command=self.face_landmarks)
        button4.grid(column=0, row=4, sticky=W + E + N + S, padx=5, pady=5)


    def open_image(self):
        self.name = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                                               filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
                                               title="Choose a file."
                                               )
        print(self.name)


    def face_landmarks(self):

        predictor_model = "shape_predictor_68_face_landmarks.dat"
        face_detector = dlib.get_frontal_face_detector()
        face_pose_predictor = dlib.shape_predictor(predictor_model)

        win = dlib.image_window()
        image = io.imread(self.name)
        detected_faces = face_detector(image, 1)

        print("Found {} faces in the image file {}".format(len(detected_faces), self.name))
        win.set_image(image)

        for i, face_rect in enumerate(detected_faces):
            print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(),
                                                                                     face_rect.top(),
                                                                                     face_rect.right(),
                                                                                     face_rect.bottom()))
        while True:
            for i, face_rect in enumerate(detected_faces):
                win.add_overlay(face_rect)
                pose_landmarks = face_pose_predictor(image, face_rect)
                win.add_overlay(pose_landmarks)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()