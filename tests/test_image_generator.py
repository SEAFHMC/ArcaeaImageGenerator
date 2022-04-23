from image_generator._resolver.resolver import ApiResult
from PIL import Image
from image_generator.utils import open_img, choice_ptt_background, DataText ,draw_text
from image_generator.assets import StaticPath

data = ApiResult()
data.get_recent()

def draw_recent(arcaea_id: str, data: ApiResult):
    name: str = data.name
    character: int = data.character
    icon = data.icon
    rating: int = data.rating
    song_id: str = data.song_id
    song_name: str = data.song_name
    author_name: str = data.author_name
    difficulty: int = data.difficulty
    score: int = data.score
    shiny_perfect_count: int = data.shiny_perfect_count
    perfect_count: int = data.perfect_count
    near_count: int = data.near_count
    miss_count: int = data.miss_count
    health: int = data.health
    song_rating: float = data.song_rating
    constant: float = data.constant
    full_character = data.full_character
    image = Image.new("RGBA", (1280, 720))
    background = open_img(StaticPath.recent_background)
    image.alpha_composite(background)
    icon = open_img(StaticPath.select_image(
        "char", icon)).resize((130, 130))
    image.alpha_composite(icon, (575, -15))
    song_cover = open_img(StaticPath.select_image(
        "song", song_id, "base.jpg")).resize((375, 375))
    image.alpha_composite(song_cover, (40, 290))
    track_info = open_img(StaticPath.is_failed(
        character=character, health=health, score=score, lost_count=miss_count))
    origin_size_w, origin_size_h = track_info.size
    track_info = track_info.resize((545, int(545/origin_size_w*origin_size_h)))
    image.alpha_composite(track_info, (365, 215))
        
    character = open_img(StaticPath.select_image("char", full_character
                                                    )).resize((1000, 1000))
    image.alpha_composite(character, (650, 125))
    res_scoresection_high = open_img(
        StaticPath.res_scoresection_high)
    image.alpha_composite(res_scoresection_high, (441, 290))
    hp_bar_base = open_img(StaticPath.hp_base if difficulty !=
                            3 else StaticPath.hp_beyond_marker).resize((45, 397))
    image.alpha_composite(hp_bar_base, (410, 290))
    hb_bar = open_img(StaticPath.select_hp_bar_image(
        character)).resize((27, 375))
    hb_bar = hb_bar.crop((0, 0, 27, int(health/100 * 375)))
    image.alpha_composite(hb_bar, (415, int(665 - health/100 * 375)))
    hp_grid = open_img(StaticPath.hp_grid).resize((27, 375))
    image.alpha_composite(hp_grid, (415, 290))
    rating_image = open_img(StaticPath.select_rating_image(
        score=score, failed=(health == -1)))
    image.alpha_composite(rating_image, (595, 417))
    ptt = open_img(StaticPath.select_image("ptt",
                                            choice_ptt_background(rating))).resize((75, 75))
    image.alpha_composite(ptt, (655, 50))


    write_player_name = DataText(
        (560 - len(name)*20), 20, 40, name, StaticPath.exo_regular)
    image = draw_text(image, write_player_name, (96, 75, 84, 255))
    write_arcaea_id = DataText(
        920, 20, 40, f"id: {arcaea_id}", StaticPath.exo_regular)
    image = draw_text(image, write_arcaea_id, (96, 75, 84, 255))
    write_song_name = DataText(
        (640 - len(song_name) / 2 * 20), 115, 40,
        song_name.capitalize(), StaticPath.notosanscjksc_regular)
    image = draw_text(image, write_song_name)
    write_author = DataText(
        (640 - len(author_name) / 2 * 12), 165, 24,
        author_name.capitalize(), StaticPath.notosanscjksc_regular)
    image = draw_text(image, write_author)
    write_score = DataText((640-len(str(score))/2 * 30), 310,
                            55, format(score, ",").replace(",", "'"), StaticPath.geosans_light)
    image = draw_text(image, write_score)
    write_difficulty = DataText(40, 230, 40, [
                                "Past", "Persent", "Future", "Beyond"][difficulty]+" " + str(int(constant)), StaticPath.geosans_light)
    image = draw_text(image, write_difficulty, (96, 75, 84, 255))
    write_recent_text = DataText(
        40, 20, 45, "Recent", StaticPath.exo_regular)
    image = draw_text(image, write_recent_text, (96, 75, 84, 255))
    pure = open_img(StaticPath.pure).resize((90, 90))
    image.alpha_composite(pure, (550, 500))
    far = open_img(StaticPath.far).resize((90, 90))
    image.alpha_composite(far, (550, 540))
    lost = open_img(StaticPath.lost).resize((90, 90))
    image.alpha_composite(lost, (550, 580))
    write_song_rating = DataText(660, 380, 25, str(
        round(song_rating, 2)), StaticPath.geosans_light)
    image = draw_text(image, write_song_rating)
    write_perfect_count = DataText(670+(4-len(str(perfect_count))/2 * 15), 530, 30, str(
        perfect_count), StaticPath.geosans_light)
    image = draw_text(image, write_perfect_count, (137, 137, 137, 255))
    write_shiny_perfect_count = DataText(720, 530, 30, "+ "+str(
        shiny_perfect_count), StaticPath.geosans_light)
    image = draw_text(image, write_shiny_perfect_count, (137, 137, 137, 255))
    write_near_count = DataText(670+(4-len(str(near_count))/2 * 15), 575, 30, str(
        near_count), StaticPath.geosans_light)
    image = draw_text(image, write_near_count, (137, 137, 137, 255))
    write_miss_count = DataText(670+(4-len(str(miss_count))/2 * 15), 610, 30, str(
        miss_count), StaticPath.geosans_light)
    image = draw_text(image, write_miss_count, (137, 137, 137, 255))
    raw_ptt = str(round(rating/100, 2)).split(".")
    write_ptt_head = DataText(690, 100, 30, raw_ptt[0], StaticPath.exo_semibold, anchor="rs")
    image = draw_text(image, write_ptt_head, stroke_fill="Black", stroke_width=2)
    write_ptt_tail = DataText(690, 100, 20, "."+raw_ptt[1], StaticPath.exo_semibold, anchor="ls")
    image = draw_text(image, write_ptt_tail, stroke_fill="Black", stroke_width=2)
    return image

res = draw_recent(arcaea_id="123456798", data=data)
res.show()