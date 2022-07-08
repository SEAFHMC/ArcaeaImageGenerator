from PIL import Image, ImageDraw


mask = Image.new("L", (5600, 2700), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle((0, 0, 5600, 2700), radius=200, fill=255)
out = mask.resize((560, 270))
out.save("./mask_560_270.png")
