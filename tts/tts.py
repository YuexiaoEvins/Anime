import time

import aiohttp
import gtts

import pygame

class TTS:
    # ttsImpl: gtts.gTTS
    lang: str

    # todo configure me
    generated_mp3_file_path: str

    def __init__(self, lang="zh-cn"):
        self.lang = lang

    def text_to_speech(self, input_text: str):
        # todo 定时删除临时的mp3文件
        demo_file = "test.mp3"
        tts = gtts.gTTS(text=input_text, lang=self.lang)
        tts.save(demo_file)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(demo_file)
        pygame.mixer.music.play()

        # wait for music play done.
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # todo 希望通过ipc的方式，跟live2d的进程通信，让其进行人物的动作变更
        # todo 调研：https://www.2bboy.com/archives/147.html
        # todo: 还有这个: https://blog.csdn.net/starvapour/article/details/108887044

    # 请求genshinvoice.top的api
    # async def genshin_voice_top_api(self, text):
    #     url = 'https://genshinvoice.top/api'
    #
    #     params = {
    #         'speaker': '神里绫华',
    #         'text': text,
    #         'format': 'mp3',
    #         'length': '1.25',
    #         'noise': '0.2',
    #         'noisew': '0.9'
    #     }
    #
    #     try:
    #         async with aiohttp.ClientSession() as session:
    #             async with session.get(url, params=params) as response:
    #                 response = await response.read()
    #                 file_name = 'genshin_voice_top_' + 'demo' + '.mp3'
    #
    #                 voice_tmp_path = file_name
    #
    #                 with open(voice_tmp_path, 'wb') as f:
    #                     f.write(response)
    #
    #                 return voice_tmp_path
    #     except aiohttp.ClientError as e:
    #         print(f'genshinvoice.top请求失败: {e}')
    #     except Exception as e:
    #         print(f'genshinvoice.top未知错误: {e}')
    #
    #     return None
