from typing import Union
from ..AUA import AccountInfo, UserRecent, SongInfo, UserBest
from PIL import Image, ImageFilter
from ..utils import open_img, DataText, draw_text, player_time_format, StaticPath, choice_ptt_background

def draw_single_song(data: Union[UserRecent, UserBest]):
    # User Info
    account_info: AccountInfo = data.account_info
    arcaea_id: str = account_info.code
    name: str = account_info.name
    character = account_info.character
    is_char_uncapped_override: bool = account_info.is_char_uncapped
    is_char_uncapped: bool = account_info.is_char_uncapped
    icon: str = (
        f"{character}u_icon.png"
        if is_char_uncapped ^ is_char_uncapped_override
        else f"{character}_icon.png"
    )
    rating: str = account_info.rating
    # Score Info
    if isinstance(data, UserRecent):
        score_info = data.recent_score[0]
    else:
        score_info = data.record
    song_id: str = score_info.song_id
    song_info: SongInfo = data.songinfo[0]
    song_name: str = song_info.name_en
    difficulty: int = score_info.difficulty
    score: int = score_info.score
    shiny_perfect_count: int = score_info.shiny_perfect_count
    perfect_count: int = score_info.perfect_count
    near_count: int = score_info.near_count
    miss_count: int = score_info.miss_count
    health: int = score_info.health
    song_rating: float = score_info.rating
    constant: float = song_info.rating / 10
    # Back Ground
    cover_name = "3.jpg" if difficulty == 3 else "base.jpg"
    image = Image.new("RGBA", (600, 867), (0, 0, 0, 0))
    song_cover = open_img(StaticPath.select_image("song", song_id, cover_name))
    image.alpha_composite(song_cover.resize((868, 868)), (-134, 0))
    image = image.filter(ImageFilter.GaussianBlur(radius=10))
    fog = Image.new("RGBA", (600, 867), (255, 255, 255, 60))
    image.alpha_composite(fog)
    side = data.songinfo[0].side
    card = open_img(StaticPath.rawv3bg_0 if side == 0 else StaticPath.rawv3bg_1)
    image.alpha_composite(card)
    image.alpha_composite(song_cover.resize((256, 256)), (172, 245))
    # Draw User Info
    icon = open_img(StaticPath.select_image("char", icon)).resize((100, 100))
    image.alpha_composite(icon, (90, 90))
    ptt = open_img(
        StaticPath.select_image("ptt", choice_ptt_background(rating))
    ).resize((75, 75))
    image.alpha_composite(ptt, (135, 135))
    raw_ptt = f"{(rating/100):.2f}".split(".")
    write_ptt_head = DataText(
        170, 180, 25, raw_ptt[0], StaticPath.exo_semibold, anchor="rs"
    )
    image = draw_text(image, write_ptt_head, stroke_fill="Black", stroke_width=2)
    write_ptt_tail = DataText(
        170, 180, 20, "." + raw_ptt[1], StaticPath.exo_semibold, anchor="ls"
    )
    write_user_name = DataText(210, 110, 35, name, StaticPath.andrea)
    image = draw_text(image, write_user_name, "black")
    write_user_code = DataText(210, 155, 20, f"ArcID:  {arcaea_id}", StaticPath.andrea)
    image = draw_text(image, write_user_code, "black")
    image = draw_text(image, write_ptt_tail, stroke_fill="Black", stroke_width=2)
    # Draw Score Info
    write_PLAYPTT = DataText(65, 765, 20, "Play Ptt:", StaticPath.exo_regular)
    image = draw_text(image, write_PLAYPTT, (110, 110, 110))
    write_ptt = DataText(
        160, 768, 17, str(round(song_rating, 4)), StaticPath.exo_regular
    )
    image = draw_text(image, write_ptt, (110, 110, 110))
    write_PLAYTIME = DataText(65, 820, 20, "Play Time:", StaticPath.exo_regular)
    image = draw_text(image, write_PLAYTIME, (110, 110, 110))
    write_playtime = DataText(
        160, 823, 17, player_time_format(score_info.time_played), StaticPath.exo_regular
    )
    image = draw_text(image, write_playtime, (110, 110, 110))
    write_song_name = DataText(
        300, 520, 25, song_name, StaticPath.kazesawa_regular, "mt"
    )
    image = draw_text(image, write_song_name, "black")
    write_difficulty = DataText(
        300,
        560,
        25,
        ["Past", "Present", "Future", "Beyond"][difficulty] + " | " + str(constant),
        StaticPath.kazesawa_regular,
        "mt",
    )
    diff_color = ((20, 165, 215), (120, 150, 80), (115, 35, 100), (166, 20, 49))[
        difficulty
    ]
    image = draw_text(image, write_difficulty, diff_color)
    track_info = open_img(
        StaticPath.is_failed(
            character=character, health=health, score=score, lost_count=miss_count
        )
    )
    origin_size_w, origin_size_h = track_info.size
    track_info = track_info.resize((400, int(400 / origin_size_w * origin_size_h)))
    image.alpha_composite(track_info, (100, 615))
    clear_type = ("[TL]", "[NC]", "[FR]", "[PM]", "[EC]", "[HC]")[score_info.clear_type]
    write_score = DataText(
        300,
        680,
        40,
        format(score, ",").replace(",", "'") + "  " + clear_type,
        StaticPath.exo_regular,
        "mt",
    )
    image = draw_text(image, write_score, "black")
    write_PURE = DataText(380, 775, 20, "Pure", StaticPath.exo_medium, "ls")
    image = draw_text(image, write_PURE, "black")
    write_pure_count = DataText(
        450,
        775,
        17,
        f"{perfect_count}(+{shiny_perfect_count})",
        StaticPath.exo_medium,
        "ls",
    )
    image = draw_text(image, write_pure_count, "black")
    write_FAR = DataText(380, 810, 20, "Far", StaticPath.exo_medium, "ls")
    image = draw_text(image, write_FAR, "black")
    write_far_count = DataText(450, 810, 17, near_count, StaticPath.exo_medium, "ls")
    image = draw_text(image, write_far_count, "black")
    write_LOST = DataText(380, 845, 20, "Lost", StaticPath.exo_medium, "ls")
    image = draw_text(image, write_LOST, "black")
    write_lost_count = DataText(450, 845, 17, miss_count, StaticPath.exo_medium, "ls")
    image = draw_text(image, write_lost_count, "black")
    return image