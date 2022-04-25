from image_generator.utils import open_img, DataText, draw_text, choice_ptt_background, get_song_info
from image_generator.assets import StaticPath
from PIL import Image
from image_generator.b30_image import draw_score_detail, draw_b30
from image_generator.recent_image import draw_recent
from typing import Dict
from image_generator.request import get_user_b30, get_user_recent

data = get_user_recent()


res = draw_recent(data=data)
res.show()