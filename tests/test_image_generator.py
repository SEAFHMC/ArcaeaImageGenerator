from loguru import logger
from image_generator._api_result.request import get_user_b30, get_user_recent
from image_generator.AUA.schema.basemodel import Base
from image_generator.AUA.schema.api.v5 import AccountInfo, SongScore, UserRecent, UserBest30
from image_generator.utils import get_song_info

from typing import Dict, List, Optional
from pydantic import validator

data = get_user_recent()
data = data


res = UserRecent(**data["content"])
logger.info(res.recent_score[0].rating)
