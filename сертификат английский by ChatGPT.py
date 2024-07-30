import os
from enum import Enum
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw


class CoursesTypes(Enum):
    PRE_INTERMEDIATE = 'has completed Pre-intermediate English Course'
    ELEMENTARY = 'has completed Elementary English Course'
    ELEMENTARY_ONLINE = 'has completed Elementary (online) English Course'
    BEGINNERS = 'has completed Beginners English Course'
    WAY_AHEAD = 'has completed Way Ahead English Course'
    FIRST = 'has completed First English Course'
    ENJOY = 'has completed Enjoy English Course'


class CertificateGenerator:
    save_path = Path(r"C:\Users\Astana\Desktop\Client")
    template_path="Certificate english английский.jpg"
    font_to_name="fonts/cassandra.ttf"
    font_to_text="fonts/Ebrima.ttf"

    def __init__(self):
        pass

    def generate_certificate(self, name, course, date, output_path):
        with Image.open(self.template_path) as img:
            resized_image = img.resize((3507, 2480), resample=Image.Resampling.LANCZOS)
            draw = ImageDraw.Draw(resized_image)
            font_to_name = ImageFont.truetype(self.font_to_name, 120)
            font_to_text = ImageFont.truetype(self.font_to_text, 72)
            draw.text((1750, 1240), name, (51, 98, 105), font=font_to_name, anchor='mb')
            draw.text((1770, 1350), course, (51, 98, 105), font=font_to_text, anchor='mb')
            draw.text((1100, 2038), date, (51, 98, 105), font=font_to_text, anchor='ms')
            resized_image.save(Path(output_path, name + '.jpg'), 'JPEG', quality=100, dpi=(300, 300))

    def go_this(self, date, course:CoursesTypes):

        with open('names.txt', 'r') as file:
            names = file.read().splitlines()

        output_path = Path.joinpath(self.save_path, course.name)
        output_path.mkdir(parents=True, exist_ok=True)

        if len(names) == 1:
            names = names[0].split(', ')

        for name in names:
            self.generate_certificate(name, course.value, date, output_path)


if __name__ == '__main__':
    date = "May 2024"
    course = CoursesTypes.ENJOY
    sertificates = CertificateGenerator().go_this(date, course)
