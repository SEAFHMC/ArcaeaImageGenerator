from PIL import Image
from image_generator.utils import DataText, draw_text, StaticPath

image = Image.new("RGBA", (114, 160), (0, 0, 0, 0))
write_PURE = DataText(114, 5, 40, "PURE", StaticPath.kazesawa_regular, "rt")
image = draw_text(image, write_PURE, (35, 160, 200), stroke_fill="white", stroke_width=1)
write_FAR = DataText(114, 65, 40, "FAR", StaticPath.kazesawa_regular, "rt")
image = draw_text(image, write_FAR, (110, 110, 110), stroke_fill="white", stroke_width=1)
write_LOST = DataText(114, 125, 40, "LOST", StaticPath.kazesawa_regular, "rt")
image = draw_text(image, write_LOST, (110, 110, 110), stroke_fill="white", stroke_width=1)
image.save("./count.png")