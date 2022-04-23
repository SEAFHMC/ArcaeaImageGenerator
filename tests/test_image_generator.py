from image_generator._resolver.resolver import ApiResult
from image_generator import draw_recent, draw_b30

data = ApiResult()
data.get_b30()

res = draw_b30(arcaea_id="123456798", data=data)
res.show()