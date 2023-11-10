import blivedm
from core import DataSource
import blivedm.models.web as web_models

class BilibiliLiveClient:
class BilibiliHandlerImpl(blivedm.BaseHandler):

    # add dependency live2d generator and tts

    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        print(f'[{client.room_id}] {message.uname}：{message.msg}')
        print(f'receive message: {message}')