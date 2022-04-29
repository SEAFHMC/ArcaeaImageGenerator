from typing import Dict
from image_generator.AUA import UserRecent, AccountInfo, SongInfo
from image_generator.request import get_user_recent
from image_generator.utils import DataText, draw_text, open_img, StaticPath, player_time_format, choice_ptt_background
from PIL import Image, ImageFilter
from image_generator.andreal_style_v3 import draw_user_recent

data = get_user_recent()
res= draw_user_recent(data)
res.show()