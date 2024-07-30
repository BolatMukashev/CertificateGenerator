import os
from enum import Enum
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw


# path = "C:/Windows/Fonts"
# fonts = os.listdir(path)
# print(fonts)


class CoursesTypes(Enum):
    PRE_INTERMEDIATE = 'has completed Pre-intermediate English Course'
    ELEMENTARY = 'has completed Elementary English Course'
    ELEMENTARY_ONLINE = 'has completed Elementary (online) English Course'
    BEGINNERS = 'has completed Beginners English Course'
    WAY_AHEAD = 'has completed Way Ahead English Course'
    FIRST = 'has completed First English Course'
    ENJOY = 'has completed Enjoy English Course'


class CertificateGenerator:
    def __init__(self, template_path, font_to_name, font_to_text, output_path):
        self.template_path = template_path
        self.font_to_name = font_to_name
        self.font_to_text = font_to_text
        self.output_path = output_path

    def generate_certificate(self, name, course, date):
        with Image.open(self.template_path) as img:
            resized_image = img.resize((3507, 2480), resample=Image.Resampling.LANCZOS)
            draw = ImageDraw.Draw(resized_image)
            font_to_name = ImageFont.truetype(self.font_to_name, 120)
            font_to_text = ImageFont.truetype(self.font_to_text, 72)
            draw.text((1750, 1240), name, (51, 98, 105), font=font_to_name, anchor='mb')
            draw.text((1770, 1350), course, (51, 98, 105), font=font_to_text, anchor='mb')
            draw.text((1100, 2038), date, (51, 98, 105), font=font_to_text, anchor='ms')
            resized_image.save(Path(self.output_path, name + '.jpg'), 'JPEG', quality=100, dpi=(300, 300))

with open('names.txt', 'r') as file:
    names = file.read().splitlines()

course = CoursesTypes.ELEMENTARY_ONLINE
date = "June 2023"

save_path = Path(r"C:\Users\Astana\Desktop\Client", course.name)
save_path.mkdir(parents=True, exist_ok=True)

if len(names) == 1:
    names = names[0].split(', ')


certificate_generator = CertificateGenerator(
    template_path="Certificate english английский.jpg",
    font_to_name="fonts/cassandra.ttf",
    font_to_text="fonts/Ebrima.ttf",
    output_path=save_path
)

for name in names:
    certificate_generator.generate_certificate(name, course.value, date)
