from typing import Union
from PIL import Image
from resource_manager import StaticPath
from ..utils import (
    open_img,
    choice_ptt_background,
    DataText,
    draw_text,
    player_time_format,
)
from schema import UserBest, UserInfo


def draw_single_song(data: Union[UserInfo, UserBest]):
    """
    没写完
    """
    # User Info
    account_info = data.content.account_info
    arcaea_id = account_info.code
    name = account_info.name
    #    character = account_info.character
    character = 54
    is_char_uncapped_override: bool = account_info.is_char_uncapped
    is_char_uncapped: bool = account_info.is_char_uncapped
    icon = (
        f"{character}u_icon.png"
        if is_char_uncapped ^ is_char_uncapped_override
        else f"{character}_icon.png"
    )
    #    rating = account_info.rating
    rating = 1260
    # Score Info
    if isinstance(data, UserInfo):
        score_info = data.content.recent_score[0]
    else:
        score_info = data.content.record
    song_id = score_info.song_id
    song_info = data.content.songinfo[0]
    song_name = song_info.name_en
    author_name = song_info.artist
    difficulty = score_info.difficulty
    score = score_info.score
    shiny_perfect_count = score_info.shiny_perfect_count
    perfect_count = score_info.perfect_count
    near_count = score_info.near_count
    miss_count = score_info.miss_count
    health = score_info.health
    song_rating = score_info.rating
    constant = song_info.rating / 10
    full_character = (
        f"{character}u.png"
        if is_char_uncapped ^ is_char_uncapped_override
        else f"{character}.png"
    )
    image = Image.new("RGBA", (1280, 720))
    background = open_img(StaticPath.recent_background)
    image.alpha_composite(background)
    icon = open_img(StaticPath.select_image("char", icon)).resize((130, 130))
    image.alpha_composite(icon, (575, -15))
    song_cover = open_img(StaticPath.select_image("song", song_id, "base.jpg")).resize(
        (375, 375)
    )
    image.alpha_composite(song_cover, (40, 290))
    track_info = open_img(
        StaticPath.is_failed(
            character=character, health=health, score=score, lost_count=miss_count
        )
    )
    origin_size_w, origin_size_h = track_info.size
    track_info = track_info.resize((545, int(545 / origin_size_w * origin_size_h)))
    image.alpha_composite(track_info, (365, 215))

    character = open_img(StaticPath.select_image("char", full_character)).resize(
        (1000, 1000)
    )
    image.alpha_composite(character, (600, 125))
    res_scoresection_high = open_img(StaticPath.res_scoresection_high)
    image.alpha_composite(res_scoresection_high, (441, 290))
    hp_bar_base = open_img(
        StaticPath.hp_base if difficulty != 3 else StaticPath.hp_beyond_marker
    ).resize((45, 397))
    image.alpha_composite(hp_bar_base, (410, 290))
    hb_bar = open_img(StaticPath.select_hp_bar_image(character)).resize((27, 375))
    hb_bar = hb_bar.crop((0, 0, 27, int(health / 100 * 375)))
    image.alpha_composite(hb_bar, (415, int(665 - health / 100 * 375)))
    hp_grid = open_img(StaticPath.hp_grid).resize((27, 375))
    image.alpha_composite(hp_grid, (415, 290))
    rating_image = open_img(
        StaticPath.select_rating_image(score=score, failed=(health == -1))
    )
    image.alpha_composite(rating_image, (595, 417))
    ptt = open_img(
        StaticPath.select_image("ptt", choice_ptt_background(rating))
    ).resize((75, 75))
    image.alpha_composite(ptt, (655, 50))

    write_player_name = DataText(
        (560 - len(name) * 20), 35, 40, name, StaticPath.andrea
    )
    image = draw_text(
        image, write_player_name, (96, 75, 84), stroke_fill=(96, 75, 84), stroke_width=1
    )
    write_arcaea_id = DataText(950, 40, 30, f"< {arcaea_id} >", StaticPath.exo_semibold)
    image = draw_text(
        image, write_arcaea_id, "white", stroke_fill="black", stroke_width=1
    )
    write_song_name = DataText(
        (640 - len(song_name) / 2 * 20),
        115,
        40,
        song_name.capitalize(),
        StaticPath.notosanscjksc_regular,
    )
    image = draw_text(image, write_song_name)
    write_author = DataText(
        (640 - len(author_name) / 2 * 12),
        165,
        24,
        author_name.capitalize(),
        StaticPath.notosanscjksc_regular,
    )
    image = draw_text(image, write_author)
    write_score = DataText(
        (640 - len(str(score)) / 2 * 30),
        310,
        55,
        format(score, ",").replace(",", "'"),
        StaticPath.geosans_light,
    )
    image = draw_text(image, write_score)
    write_difficulty = DataText(
        40,
        230,
        40,
        ["Past", "Present", "Future", "Beyond"][difficulty] + " " + str(int(constant)),
        StaticPath.kazesawa_regular,
    )
    diff_color = ((20, 165, 215), (120, 150, 80), (115, 35, 100), (166, 20, 49))[
        difficulty
    ]
    image = draw_text(image, write_difficulty, diff_color)
    write_recent_text = DataText(40, 35, 45, "Recent", StaticPath.andrea)
    image = draw_text(
        image, write_recent_text, (96, 75, 84), stroke_fill=(96, 75, 84), stroke_width=1
    )
    count = open_img(StaticPath.count)
    count.thumbnail((110, 110))
    image.alpha_composite(count, (560, 526))
    write_song_rating = DataText(
        660, 380, 25, str(round(song_rating, 2)), StaticPath.geosans_light
    )
    image = draw_text(image, write_song_rating)
    write_perfect_count = DataText(
        670 + (4 - len(str(perfect_count)) / 2 * 15),
        530,
        30,
        str(perfect_count),
        StaticPath.geosans_light,
    )
    image = draw_text(
        image,
        write_perfect_count,
        (137, 137, 137, 255),
        stroke_fill="white",
        stroke_width=2,
    )
    write_shiny_perfect_count = DataText(
        720, 530, 30, "+ " + str(shiny_perfect_count), StaticPath.geosans_light
    )
    image = draw_text(
        image,
        write_shiny_perfect_count,
        (137, 137, 137, 255),
        stroke_fill="white",
        stroke_width=2,
    )
    write_near_count = DataText(
        670 + (4 - len(str(near_count)) / 2 * 15),
        571,
        30,
        str(near_count),
        StaticPath.geosans_light,
    )
    image = draw_text(
        image, write_near_count, (110, 110, 110), stroke_fill="white", stroke_width=2
    )
    write_miss_count = DataText(
        670 + (4 - len(str(miss_count)) / 2 * 15),
        611,
        30,
        str(miss_count),
        StaticPath.geosans_light,
    )
    image = draw_text(
        image,
        write_miss_count,
        (137, 137, 137, 255),
        stroke_fill="white",
        stroke_width=2,
    )
    raw_ptt = f"{(rating/100):.2f}".split(".")
    write_ptt_head = DataText(
        690, 100, 30, raw_ptt[0], StaticPath.exo_semibold, anchor="rs"
    )
    image = draw_text(image, write_ptt_head, stroke_fill="Black", stroke_width=2)
    write_ptt_tail = DataText(
        690, 100, 20, "." + raw_ptt[1], StaticPath.exo_semibold, anchor="ls"
    )
    image = draw_text(image, write_ptt_tail, stroke_fill="Black", stroke_width=2)
    time_bg = open_img(StaticPath.time_bg).resize((314, 70))
    image.alpha_composite(time_bg, (1050, 690))
    write_played_time = DataText(
        1260,
        714,
        20,
        player_time_format(score_info.time_played),
        StaticPath.kazesawa_regular,
        "rb",
    )
    image = draw_text(image, write_played_time, "white")
    rating_up = open_img(StaticPath.rating_up).resize((215, 215))
    image.alpha_composite(rating_up, (695, -70))
    write_optential = DataText(800, 38, 28, "POTENTIAL", StaticPath.geosans_light, "ms")
    image = draw_text(image, write_optential, "white", 1, "grey")
    write_rating_up = DataText(800, 90, 30, "+12.60", StaticPath.exo_semibold, "ms")
    image = draw_text(image, write_rating_up, "white", 1, (35, 160, 200))
    return image
