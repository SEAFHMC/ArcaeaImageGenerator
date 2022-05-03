from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from .assets import StaticPath
from .AUA import UserBest30


def draw_user_b30(obj_in: UserBest30) -> Image.Image:
    img = Image.open(StaticPath.bg)
    draw = ImageDraw.ImageDraw(img)
    ft_normal = ImageFont.truetype(StaticPath.roboto_bold, 18)
    ft_low = ImageFont.truetype(StaticPath.roboto_regular, 14)
    ft_title = ImageFont.truetype(StaticPath.roboto_regular, 25)
    title_color = (230, 230, 230)
    inner_gap = [20, 52, 52]
    userptt = obj_in.best30_avg * 0.75 + obj_in.recent10_avg * 0.25
    b30_songids = [i.song_id for i in obj_in.best30_list]
    b30_scores = [i.score for i in obj_in.best30_list]
    b30_ratings = [i.rating for i in obj_in.best30_list]
    b30_difficulties = [i.difficulty for i in obj_in.best30_list]
    b30_len = len(obj_in.best30_list)
    for i in range(min(b30_len, 15)):
        # 绘制左边 15 条数据，数据不足 15 条可以兼容
        ylen = 60 * i
        draw.text((150, ylen + inner_gap[0]), f'{b30_songids[i]} [{["PST", "PRS", "FTR", "BYD"][b30_difficulties[i]]}]', title_color, font=ft_title)
        draw.text((150, ylen + inner_gap[1]), f'Score: {b30_scores[i]}', (255, 255, 255), font=ft_normal)
        draw.text((400, ylen + inner_gap[2]), f'PTT: {b30_ratings[i]:.2f}', (255, 255, 255), font=ft_normal)
    if b30_len > 15:
        # 当数据数量大于 15 时，绘制右边 `b30_len` - 15 条数据，兼容数据不满 30 条但是满了 15 条的情况
        for i in range(b30_len - 15):
            ylen = 60 * i
            draw.text((600, ylen + inner_gap[0]), f'{b30_songids[i + 15]} [{["PST", "PRS", "FTR", "BYD"][b30_difficulties[i]]}]', title_color, font=ft_title)
            draw.text((600, ylen + inner_gap[1]), f'Score: {b30_scores[i + 15]}', (255, 255, 255), font=ft_normal)
            draw.text((850, ylen + inner_gap[2]), f'PTT: {b30_ratings[i + 15]:.2f}', (255, 255, 255), font=ft_normal)
    info_draw = f'Player PTT: {userptt:.2f}   b30_avg: {obj_in.best30_avg:.2f}   r10_avg: {obj_in.recent10_avg:.2f}'
    draw.text((800, 930), info_draw, (200, 200, 200), font=ft_low)
    author_draw = datetime.now().strftime("%F %X") + "   Powered by iyume"
    draw.text((20, 930), author_draw, (200, 200, 200), font=ft_low)
    return img
