import time

import gtts
import io
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
    async def genshinvoice_top_api(self, text):
        url = 'https://genshinvoice.top/api'

        genshinvoice_top = self.config.get("genshinvoice_top")

        params = {
            'speaker': genshinvoice_top['speaker'],
            'text': text,
            'format': genshinvoice_top['format'],
            'length': genshinvoice_top['length'],
            'noise': genshinvoice_top['noise'],
            'noisew': genshinvoice_top['noisew']
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    response = await response.read()
                    # voice_tmp_path = os.path.join(self.audio_out_path, 'genshinvoice_top_' + self.common.get_bj_time(4) + '.wav')
                    file_name = 'genshinvoice_top_' + self.common.get_bj_time(4) + '.wav'

                    voice_tmp_path = self.common.get_new_audio_path(self.audio_out_path, file_name)

                    with open(voice_tmp_path, 'wb') as f:
                        f.write(response)

                    return voice_tmp_path
        except aiohttp.ClientError as e:
            logging.error(f'genshinvoice.top请求失败: {e}')
        except Exception as e:
            logging.error(f'genshinvoice.top未知错误: {e}')

        return None
