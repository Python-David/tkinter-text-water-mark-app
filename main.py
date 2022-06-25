# from tkinter import *
# from tkinter import filedialog
# from PIL import Image, ImageDraw, ImageFont
#
# window = Tk()
# window.title("Water Mark Pro")
# window.config(pady=20, padx=20)
#
#
#
#
# def action():
#     filename = filedialog.askopenfilename(initialdir=wtm_folder, title="Select an image:")
#
#     return filename
#
#
# def add_water_mark(image, wm_text):
#     opened_image = Image.open(image)
#     image_width, image_height = opened_image.size
#     draw = ImageDraw.Draw(opened_image)
#
#     font_size = int(image_width / 20)
#
#     font = ImageFont.truetype("Arial.ttf", font_size)
#     x, y = int(image_width / 2), int(image_height / 2)
#
#     draw.text((x, y), wm_text, font=font, fill="#FFF", stroke_width=5, stroke_fill="#222", anchor="ms")
#
#     opened_image.show()
#     opened_image.save(f"{wtm_folder}/wtm_images/2.png")
#
#
# def add():
#     add_water_mark(action(), entry.get())


# canvas = Canvas(width=540, height=960 / 2)
# bg_image = PhotoImage(file="wmp2.png")
# canvas.create_image(540 / 2, 960 / 2, image=bg_image)
# canvas.grid(column=0, row=0, columnspan=2)

# button = Button(text="Select Image", command=action, width=20)
# button.grid(column=0, row=1)

# entry = Entry(width=59)
# entry.insert(END, string="Enter watermark text.")
# entry.grid(column=0, row=1)
#
# button = Button(text="Select Image/Add Water Mark", command=add, width=56)
# button.grid(column=0, row=2, columnspan=2)
#
# window.mainloop()

# calls action() when pressed

from ui import UI

ui = UI()