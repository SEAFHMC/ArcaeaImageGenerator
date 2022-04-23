from PIL import Image, ImageEnhance
from typing import Tuple, Dict
from .assets import StaticPath
from .utils import (
    text_image,
    open_img,
    get_song_info,
    get_average_color,
    is_dark,
    player_time_format,
    DataText,
    draw_text,
    choice_ptt_background,
)
from ._resolver.resolver import ApiResult


def draw_score_bg(
    average_color: Tuple[int, int, int], song_cover: Image.Image, mask: Image.Image
) -> Image.Image:
    invisible_bg = Image.new("RGBA", (560, 270), (0, 0, 0, 0))
    score_bg = Image.new("RGBA", (560, 270))
    score_bg.alpha_composite(song_cover, (290, 0))
    left = Image.new("RGBA", (290, 270), average_color)
    score_bg.alpha_composite(left)
    for i in range(230):
        score_bg.alpha_composite(
            Image.new(
                "RGBA",
                (1, 270),
                (
                    average_color[0],
                    average_color[1],
                    average_color[2],
                    255 - int(1.2 * i),
                ),
            ),
            (290 + i, 0),
        )
    out = Image.composite(score_bg, invisible_bg, mask)
    return out


def draw_score_detail(data: Dict, rank: int, song_id: str, mask: Image.Image) -> Image.Image:
    # Frame
    song_info = get_song_info(song_id)
    diff = data["difficulty"]
    cover_name = "3.jpg" if diff == 3 else "base.jpg"
    song_background = open_img(StaticPath.song_dir/data["song_id"]/cover_name).resize((270, 270))
    average_color = get_average_color(song_background)
    contrast_degree = 7 if is_dark(average_color) else 0.3
    image = draw_score_bg(average_color, song_background, mask)
    diff_background = open_img(StaticPath.diff_dir/["PST.png", "PRS.png", "FTR.png", "BYD.png"][diff]).resize((14, 48))
    image.alpha_composite(diff_background, (24, 24))
    song_name = song_info["title_localized"]["en"]
    song_name = song_name if len(song_name) < 19 else song_name[:18]+"…"
    text_overlay = Image.new("RGBA", (560, 270), (0, 0, 0, 0))
    write_song_name = DataText(45, 32, 40, song_name, StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_song_name, average_color)
    write_score = DataText(45, 80, 40, f'{data["score"]:,}', StaticPath.exo_medium)
    text_overlay = draw_text(text_overlay, write_score, average_color)
    write_ranking = DataText(490, 20, 30, f'#{rank + 1}', StaticPath.exo_medium)
    image = draw_text(image, write_ranking, (255, 255, 255, 255), 1)
    # Table
    table = open_img(StaticPath.table)
    image.alpha_composite(table)
    write_P = DataText(50, 130, 35, "P", StaticPath.andrea)
    text_overlay = draw_text(text_overlay, write_P, average_color, 1, average_color)
    write_F = DataText(50, 175, 35, "F", StaticPath.andrea)
    text_overlay = draw_text(text_overlay, write_F, average_color, 1, average_color)
    write_L = DataText(50, 220, 35, "L", StaticPath.andrea)
    text_overlay = draw_text(text_overlay, write_L, average_color, 1, average_color)
    write_PTT = DataText(250, 130, 25, "PTT", StaticPath.exo_medium)
    text_overlay = draw_text(text_overlay, write_PTT, average_color)
    write_DATE = DataText(250, 200, 25, "DATE", StaticPath.exo_medium)
    text_overlay = draw_text(text_overlay, write_DATE, average_color)
    write_arrow = DataText(300, 150, 50, ">", StaticPath.andrea)
    text_overlay = draw_text(text_overlay, write_arrow, average_color)
    # Count
    write_p_count = DataText(75, 130, 30, str(data["perfect_count"]), StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_p_count, average_color)
    write_sp_count = DataText(155, 130, 20, f'+{data["shiny_perfect_count"]}', StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_sp_count, average_color)
    write_near_count = DataText(75, 175, 30, str(data["near_count"]), StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_near_count, average_color)
    write_miss_count = DataText(75, 220, 30, str(data["miss_count"]), StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_miss_count, average_color)
    write_time = DataText(250, 230, 25, player_time_format(data["time_played"]), StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_time, average_color)
    write_constant = DataText(250, 165, 25, f'{song_info["difficulties"][data["difficulty"]]["rating"]:.1f}', StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_constant, average_color)
    write_rating = DataText(320, 148, 25, f'{data["rating"]:.3f}', StaticPath.kazesawa_regular)
    text_overlay = draw_text(text_overlay, write_rating, average_color)
    contrast_enhancer = ImageEnhance.Contrast(text_overlay)
    contrast_img = contrast_enhancer.enhance(contrast_degree)
    image.alpha_composite(contrast_img)
    return image


def draw_b30(arcaea_id: str, data: ApiResult):
    B30_bg = open_img(StaticPath.B30_bg)
    # User Info
    name: str = data.name
    rating: str = data.rating
    best: float = data.best
    recent: float = data.recent
    icon: str = data.icon
    icon = open_img(StaticPath.char_dir/icon).resize((250, 250))
    B30_bg.alpha_composite(icon, (75, 130))
    ptt_background = open_img(StaticPath.ptt_dir/choice_ptt_background(rating)).resize((150, 150))
    B30_bg.alpha_composite(ptt_background, (200, 280))
    raw_ptt = str(round(rating/100, 2)).split(".")
    write_ptt_head = DataText(270, 370, 50, raw_ptt[0], StaticPath.exo_medium, anchor="rs")
    B30_bg = draw_text(B30_bg, write_ptt_head, stroke_fill="Black", stroke_width=2)
    write_ptt_tail = DataText(270, 370, 40, "."+raw_ptt[1], StaticPath.exo_medium, anchor="ls")
    B30_bg = draw_text(B30_bg, write_ptt_tail, stroke_fill="Black", stroke_width=2)
    write_arcname = DataText(355, 280, 100, name,
                             StaticPath.exo_medium, anchor="lb")
    B30_bg = draw_text(B30_bg, write_arcname)
    write_arcaea_id = DataText(
        380, 360, 60, f"ID:{arcaea_id}", StaticPath.exo_medium, anchor="lb")
    B30_bg = draw_text(B30_bg, write_arcaea_id)
    write_r10 = DataText(
        1000, 560, 100, f"Recent 10: {recent:.3f}", StaticPath.exo_medium, anchor="lb")
    B30_bg = draw_text(B30_bg, write_r10)
    write_b30 = DataText(
        200, 560, 100, f"Best 30: {best:.3f}", StaticPath.exo_medium, anchor="lb")
    B30_bg = draw_text(B30_bg, write_b30)
    # Score Info
    score_info_list = data.score_info_list
    divider = open_img(StaticPath.divider).resize((2000, 50))
    background_y = 640
    background_x = 0
    mask = Image.open(StaticPath.mask)
    for num, value in enumerate(score_info_list):
        if num == 39:
            break
        if num % 3 == 0:
            background_y += 300 if num != 0 else 0
            background_x = 100
        else:
            background_x += 620
        if num / 3 == 10:
            background_y += 100
            B30_bg.alpha_composite(divider, (0, background_y-87))
        B30_bg.alpha_composite(draw_score_detail(value, rank=num, song_id=value["song_id"], mask=mask), (background_x, background_y))
    return B30_bg