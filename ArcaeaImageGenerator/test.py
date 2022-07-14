from image_message import UserArcaeaInfo
import asyncio

img = asyncio.run(UserArcaeaInfo.draw_user_recent(arcaea_id="ToasterKoishi"))
img.show()
