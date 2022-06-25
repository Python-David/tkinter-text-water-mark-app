from tkinter import *
from tkinter import filedialog
from editor import Editor


class UI:
    def __init__(self):
        self.filename = None
        self.window = Tk()
        self.window.title("Water Mark Pro")
        self.window.config(pady=20, padx=20)
        self.wtm_folder = "/Users/kingbarz/Desktop/wtp"

        self.canvas = Canvas(width=540, height=960 / 2)
        self.bg_image = PhotoImage(file="wmp2.png")
        self.canvas.create_image(540 / 2, 960 / 2, image=self.bg_image)
        self.canvas.grid(column=0, row=0, columnspan=2)

        # self.entry = Entry(width=59)
        # self.entry.insert(END, string="Enter watermark text.")
        # self.entry.grid(column=0, row=1)
        #
        # self.button = Button(text="Select Image/Add Water Mark", command=self.select_image, width=56)
        # self.button.grid(column=0, row=2, columnspan=2)

        self.button = Button(text="Select Image", command=self.select_image, width=56)
        self.button.grid(column=0, row=2, columnspan=2)

        self.window.mainloop()

    def select_image(self):
        self.filename = filedialog.askopenfilename(initialdir=self.wtm_folder, title="Select an image:")
        # convert and resize image to png
        editor = Editor(self.filename)
        editor.convert(self.filename)
        pic_name = editor.pic_name
        self.bg_image = PhotoImage(file=f"{self.wtm_folder}/{pic_name}.png")
        self.canvas.create_image(540 / 2, 960 / 2, image=self.bg_image)

        # Text, Text Size, Color, Font

        self.entry = Entry(width=59)
        self.entry.insert(END, string="Enter watermark text.")
        self.entry.grid(column=0, row=3)

        self.button = Button(text="Add Water Mark", command=lambda: editor.add_water_mark(self.entry.get()), width=56)
        self.button.grid(column=0, row=4, columnspan=2)
