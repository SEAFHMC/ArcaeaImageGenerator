from PIL import Image, ImageDraw
from image_generator.assets import StaticPath


image = Image.new("RGBA", (560, 270), (255, 255, 255, 0))
table_P= Image.new("RGBA", (2000, 100), 0)
draw = ImageDraw.Draw(table_P)
draw.rounded_rectangle((0, 0, 2000, 100), radius=0, fill=(34, 168, 255, 255))
image.alpha_composite(table_P.resize((100, 10)), (45, 145))
table_Pp= Image.new("RGBA", (2000, 100), 0)
draw = ImageDraw.Draw(table_Pp)
draw.rounded_rectangle((0, 0, 2000, 100), radius=0, fill=(65, 220, 220, 255))
image.alpha_composite(table_Pp.resize((60, 5)), (145, 150))
table_F= Image.new("RGBA", (2000, 100), 0)
draw = ImageDraw.Draw(table_F)
draw.rounded_rectangle((0, 0, 2000, 100), radius=0, fill=(194, 176, 126, 255))
image.alpha_composite(table_F.resize((100, 10)), (45, 190))
table_L= Image.new("RGBA", (2000, 100), 0)
draw = ImageDraw.Draw(table_L)
draw.rounded_rectangle((0, 0, 2000, 100), radius=0, fill=(99, 67, 142, 255))
image.alpha_composite(table_L.resize((100, 10)), (45, 240))
image.save("./table.png")