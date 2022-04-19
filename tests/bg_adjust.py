from PIL import Image


adj = Image.new("RGBA", (2000, 4700), (0, 0, 0, 0))
bg = Image.open("./B30.png")
adj.alpha_composite(bg)
shadow = Image.new("RGBA", (2000, 1000))
for i in range(1000):
    im = Image.new("RGBA", (2000, 1), (100, 100, 150, int(i*255/1000)))
    shadow.alpha_composite(im, ((0, i)))
#shadow.show()
adj.alpha_composite(shadow, (0, 3700))
adj.save("./adj.png")