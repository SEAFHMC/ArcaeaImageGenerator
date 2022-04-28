from image_generator.b30_image import draw_b30
from image_generator.request import get_user_b30


data = get_user_b30()



res = draw_b30(data)
res.show()