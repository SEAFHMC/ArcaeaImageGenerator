from image_generator._api_result.request import get_user_recent
from image_generator.b30_image import draw_b30
from image_generator.recent_image import draw_recent
from image_generator.request import get_user_b30
from image_generator.AUA import SongInfo, UserRecent, AccountInfo
from image_generator.utils import DataText, draw_text, open_img, player_time_format, choice_ptt_background, StaticPath
from PIL import Image
from typing import Dict


data = get_user_recent()


res = draw_recent(data)
res.show()