from image_generator.single_song.arcaea_style import draw_single_song
from image_generator._api_result.request import get_user_recent
from image_generator.AUA.schema.api.v5 import UserRecent


resp = get_user_recent()
data = UserRecent(**resp["content"])
res= draw_single_song(data)
res.show()
