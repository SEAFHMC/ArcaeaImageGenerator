from image_generator.b30_image import draw_b30
from image_generator._resolver.resolver import ApiResult

data = ApiResult()
data.get_b30()


res = draw_b30(data)
res.show()