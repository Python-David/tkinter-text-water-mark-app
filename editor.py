from PIL import Image, ImageDraw, ImageFont
import os


class Editor:

    def __init__(self, filename):
        self.root_folder = "/Users/kingbarz/Desktop/wtp/"
        self.pic_name_ext = filename.replace(self.root_folder, "")
        self.pic_name = self.pic_name_ext.split(".")[0]

    def convert(self, filename):
        self.pic_name_ext = filename.replace(self.root_folder, "")
        # convert image
        size = (270, 480)
        image = Image.open(f"{self.root_folder}/{self.pic_name_ext}")
        self.pic_name = self.pic_name_ext.split(".")[0]
        image.resize(size)
        image.save(f"{self.root_folder}/{self.pic_name}.png")

    def add_water_mark(self, wm_text):
        opened_image = Image.open(f"{self.root_folder}/{self.pic_name_ext}")
        image_width, image_height = opened_image.size
        draw = ImageDraw.Draw(opened_image)

        font_size = int(image_width / 20)

        font = ImageFont.truetype("Arial.ttf", font_size)
        x, y = int(image_width / 2), int(image_height / 2)

        draw.text((x, y), wm_text, font=font, fill="#FFF", stroke_width=5, stroke_fill="#222", anchor="ms")

        opened_image.show()
        opened_image.save(f"{self.root_folder}/wtm_images/wtm-{self.pic_name_ext}")