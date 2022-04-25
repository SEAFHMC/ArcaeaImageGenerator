from .._RHelper import RHelper
import ujson as json
root = RHelper()
cwd = root._api_result

def get_user_b30():
    with open(cwd/("b30_data.json"), "r", encoding="UTF-8") as f:
        return json.loads(f.read())


def get_user_recent():
    with open(cwd/("recent_data.json"), "r", encoding="UTF-8") as f:
        return json.loads(f.read())
