from image_generator._api_result.request import get_user_b30, get_user_recent
from image_generator.AUA.schema.basemodel import Base
from image_generator.AUA.schema.api.v5 import AccountInfo, SongScore, account_info, song_score

from typing import Dict, List, Optional
from pydantic import validator

data = get_user_b30()
data = data

class UserBest30(Base):
    best30_avg: float
    recent10_avg: float
    account_info: AccountInfo
    best30_list: List[SongScore]
    best30_overflow: List[SongScore]


ur = UserBest30(**data["content"])
print(ur.account_info.character)