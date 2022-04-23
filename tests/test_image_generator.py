from image_generator._resolver.resolver import ApiResult
from PIL import Image
from image_generator.utils import open_img, choice_ptt_background
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
    return image

res = draw_recent(arcaea_id="123456798", data=data)
res.show()