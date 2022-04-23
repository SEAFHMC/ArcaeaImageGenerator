from image_generator._resolver.resolver import ApiResult
from image_generator import draw_recent

data = ApiResult()
data.get_recent()

res = draw_recent(arcaea_id="123456798", data=data)
res.show()